import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, simpledialog


class GestaoInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Inventário")
        self.root.geometry("1000x600")

        self.df = None

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10, fill='x')

        self.btn_carregar = tk.Button(
            btn_frame, text="Carregar Planilha de Inventário", command=self.carregar_planilha)
        self.btn_carregar.pack(side="left", padx=5)

        self.btn_adicionar = tk.Button(
            btn_frame, text="Adicionar Item", command=self.adicionar_item, state='disabled')
        self.btn_adicionar.pack(side="left", padx=5)

        self.btn_atualizar = tk.Button(
            btn_frame, text="Atualizar Item", command=self.atualizar_estoque, state='disabled')
        self.btn_atualizar.pack(side="left", padx=5)

        self.btn_remover = tk.Button(
            btn_frame, text="Remover Item", command=self.remover_item, state='disabled')
        self.btn_remover.pack(side="left", padx=5)

        search_frame = tk.Frame(root)
        search_frame.pack(fill='x', padx=10)

        tk.Label(search_frame, text="Buscar:").pack(side='left')
        self.entry_busca = tk.Entry(search_frame)
        self.entry_busca.pack(side='left', fill='x', expand=True, padx=5)
        self.entry_busca.bind("<KeyRelease>", self.filtrar)

        # Treeview para exibir dados
        self.tree = ttk.Treeview(root, show="headings")
        self.tree.pack(expand=True, fill="both")
        self.tree.bind('<<TreeviewSelect>>', self.on_item_select)

        scrollbar = ttk.Scrollbar(
            root, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Label somatório
        self.label_total = tk.Label(root, text="Total Valor em Estoque: R$ 0,00", font=(
            "Arial", 12, "bold"), anchor="e")
        self.label_total.pack(fill="x", padx=10, pady=10)

        self.colunas = []  # Guarda colunas atualizadas da tabela
        self.coluna_valor = None  # Nome da coluna valor estoque

        # Dados atuais filtrados (índices para reexibir)
        self.dados_filtrados = []

    def carregar_planilha(self):
        arquivo = filedialog.askopenfilename(
            filetypes=[("Arquivos Excel", "*.xlsx;*.xls")],
            title="Selecione a planilha de inventário"
        )
        if not arquivo:
            return
        try:
            df = pd.read_excel(arquivo)
        except Exception as e:
            messagebox.showerror(
                "Erro", f"Não foi possível abrir o arquivo:\n{e}")
            return

        self.df = df.copy()
        self.colunas = list(df.columns)
        self.tree["columns"] = self.colunas

        # Configura colunas
        for col in self.colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130, anchor="center")

        self.atualizar_tabela(df)

        # Tenta identificar a coluna "Valor em estoque"
        self.coluna_valor = None
        for col in self.colunas:
            if col.lower().strip() in ["valor em estoque", "valor estoque"]:
                self.coluna_valor = col
                break

        self.atualizar_somatorio()
        self.btn_adicionar.config(state='normal')
        self.btn_atualizar.config(state='disabled')
        self.btn_remover.config(state='disabled')

    def atualizar_tabela(self, df_display):
        self.tree.delete(*self.tree.get_children())
        for _, row in df_display.iterrows():
            valores = [row[col] for col in self.colunas]
            self.tree.insert("", "end", values=valores)
        self.dados_filtrados = df_display.index.tolist()

    def atualizar_somatorio(self):
        total_estoque = 0.0
        if self.coluna_valor and self.df is not None:
            for val in self.df[self.coluna_valor].astype(str).values:
                v = val.replace("R$", "").replace(
                    ".", "").replace(",", ".").strip()
                try:
                    total_estoque += float(v)
                except:
                    continue
            texto = f"Total Valor em Estoque: R$ {total_estoque:,.2f}"
            texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
            self.label_total.config(text=texto)
        else:
            self.label_total.config(
                text="Coluna 'Valor em estoque' não encontrada.")

    def on_item_select(self, event):
        selecionados = self.tree.selection()
        if selecionados:
            self.btn_atualizar.config(state='normal')
            self.btn_remover.config(state='normal')
        else:
            self.btn_atualizar.config(state='disabled')
            self.btn_remover.config(state='disabled')

    def adicionar_item(self):
        self.janela_edicao(novo=True)

    def atualizar_estoque(self):
        selecionados = self.tree.selection()
        if not selecionados:
            messagebox.showwarning(
                "Aviso", "Selecione um item para atualizar.")
            return
        item = selecionados[0]
        valores = self.tree.item(item, "values")
        self.janela_edicao(novo=False, item=item, valores=valores)

    def remover_item(self):
        selecionados = self.tree.selection()
        if not selecionados:
            messagebox.showwarning("Aviso", "Selecione um item para remover.")
            return
        resp = messagebox.askyesno(
            "Remover", "Tem certeza que deseja remover o item selecionado?")
        if resp:
            item = selecionados[0]
            valores = self.tree.item(item, "values")
            if self.df is not None:
                # remove do dataframe
                df_idx = self.dados_filtrados[self.tree.index(item)]
                self.df = self.df.drop(df_idx).reset_index(drop=True)
                self.buscar_apos_remover()
            self.tree.delete(item)
            self.atualizar_somatorio()
            self.btn_atualizar.config(state='disabled')
            self.btn_remover.config(state='disabled')

    def buscar_apos_remover(self):
        # Reexibe dados filtraods depois da remoção
        termo = self.entry_busca.get().lower()
        if termo.strip() == "":
            self.atualizar_tabela(self.df)
        else:
            self.filtrar()

    def filtrar(self, event=None):
        if self.df is None:
            return
        termo = self.entry_busca.get().lower()
        if termo.strip() == "":
            df_filtrado = self.df.copy()
        else:
            mask = pd.Series(False, index=self.df.index)
            for col in self.colunas:
                mask = mask | self.df[col].astype(
                    str).str.lower().str.contains(termo)
            df_filtrado = self.df.loc[mask]
        self.atualizar_tabela(df_filtrado)

    def janela_edicao(self, novo=True, item=None, valores=None):
        janela_ed = tk.Toplevel(self.root)
        janela_ed.title("Adicionar Item" if novo else "Atualizar Item")
        janela_ed.geometry("500x350")
        entries = {}

        for i, col in enumerate(self.colunas):
            tk.Label(janela_ed, text=col).grid(
                row=i, column=0, sticky="e", padx=5, pady=5)
            ent = tk.Entry(janela_ed, width=40)
            ent.grid(row=i, column=1, padx=5, pady=5)
            if not novo and valores:
                ent.insert(0, valores[i])
            entries[col] = ent

        def salvar():
            dados = {}
            for col in self.colunas:
                val = entries[col].get().strip()
                # Converte valores para tipos apropriados
                if col in ["Quantidade", "Qte. Minima"]:
                    dados[col] = int(val) if val.isdigit() else 0
                elif col in ["Preço", "Valor em estoque"]:
                    dados[col] = float(val.replace("R$", "").replace(
                        ".", "").replace(",", ".")) if val else 0.0
                else:
                    dados[col] = val

            # Atualiza dataframe e treeview
            if novo:
                # Usando pd.concat para adicionar um novo item
                novo_df = pd.DataFrame([dados])
                self.df = pd.concat(
                    [self.df, novo_df], ignore_index=True) if self.df is not None else novo_df
            else:
                if item is not None:
                    idx = self.dados_filtrados[self.tree.index(item)]
                    for col in self.colunas:
                        self.df.at[idx, col] = dados[col]
            self.atualizar_tabela(self.df)
            self.atualizar_somatorio()
            janela_ed.destroy()

        btn_salvar = tk.Button(janela_ed, text="Salvar", command=salvar)
        btn_salvar.grid(row=len(self.colunas), column=0, columnspan=2, pady=10)


def main():
    root = tk.Tk()
    app = GestaoInventario(root)
    root.mainloop()


if __name__ == "__main__":
    main()
