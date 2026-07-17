import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

def carregar_planilha():
    arquivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if arquivo:
        try:
            df = pd.read_excel(arquivo)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo Excel:\n{e}")
            return
        
        # Limpa colunas e dados antigos da Treeview
        tree.delete(*tree.get_children())
        tree["columns"] = list(df.columns)
        
        # Configura as colunas dinamicamente
        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")

        # Insere os dados
        for _, row in df.iterrows():
            tree.insert("", "end", values=list(row))

# Cria a janela principal
root = tk.Tk()
root.title("Leitor Dinâmico de Planilhas Excel")
root.geometry("800x400")

# Botão para carregar a planilha
btn_carregar = tk.Button(root, text="Carregar Planilha Excel", command=carregar_planilha)
btn_carregar.pack(pady=10)

# Treeview para mostrar a tabela, inicialmente vazia
tree = ttk.Treeview(root, show='headings')
tree.pack(expand=True, fill='both')

# Barra de Scroll vertical
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')
tree.configure(yscrollcommand=scrollbar.set)

root.mainloop()

