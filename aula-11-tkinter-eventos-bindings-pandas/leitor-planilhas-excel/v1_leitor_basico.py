import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def carregar_planilha():
    # Abre um diálogo para selecionar o arquivo Excel
    arquivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if arquivo:
        # Lê a planilha usando pandas
        df = pd.read_excel(arquivo)
        
        # Limpa a árvore de dados
        for i in tree.get_children():
            tree.delete(i)
        
        # Adiciona os dados à árvore
        for index, row in df.iterrows():
            tree.insert("", "end", values=list(row))

# Cria a janela principal
root = tk.Tk()
root.title("Leitor de Planilhas Excel")

# Cria um botão para carregar a planilha
btn_carregar = tk.Button(root, text="Carregar Planilha", command=carregar_planilha)
btn_carregar.pack(pady=10)

# Cria uma árvore para exibir os dados
tree = ttk.Treeview(root, columns=("Coluna1", "Coluna2", "Coluna3"), show='headings')
tree.heading("Coluna1", text="Coluna 1")
tree.heading("Coluna2", text="Coluna 2")
tree.heading("Coluna3", text="Coluna 3")
tree.pack(pady=20)

# Inicia o loop da interface gráfica
root.mainloop()
