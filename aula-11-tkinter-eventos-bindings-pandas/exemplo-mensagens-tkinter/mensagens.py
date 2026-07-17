import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog


def mostrar_info():
    messagebox.showinfo("Título", "Mensagem informativa")


def mostrar_aviso():
    messagebox.showwarning("Aviso", "Cuidado!")


def mostrar_erro():
    messagebox.showerror("Erro", "Algo deu errado")


def confirmar():
    resposta = messagebox.askyesno("Confirmação", "Deseja continuar?")
    if resposta:
        messagebox.showinfo("Resposta", "Você escolheu continuar!")
    else:
        messagebox.showinfo("Resposta", "Você escolheu não continuar.")


def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])
    if arquivo:
        messagebox.showinfo("Arquivo Selecionado",
                            f"Você selecionou: {arquivo}")


def entrada_dados():
    valor = simpledialog.askinteger("Entrada", "Digite um número")
    if valor is not None:
        messagebox.showinfo("Valor Digitado", f"Você digitou: {valor}")


# Criando a janela principal
root = tk.Tk()
root.title("Exemplo de Mensagens")
root.geometry("300x300")

# Botões para cada funcionalidade
btn_info = tk.Button(root, text="Mostrar Info", command=mostrar_info)
btn_info.pack(pady=10)

btn_aviso = tk.Button(root, text="Mostrar Aviso", command=mostrar_aviso)
btn_aviso.pack(pady=10)

btn_erro = tk.Button(root, text="Mostrar Erro", command=mostrar_erro)
btn_erro.pack(pady=10)

btn_confirmar = tk.Button(root, text="Confirmar", command=confirmar)
btn_confirmar.pack(pady=10)

btn_abrir = tk.Button(root, text="Abrir Arquivo", command=abrir_arquivo)
btn_abrir.pack(pady=10)

btn_entrada = tk.Button(root, text="Entrada de Dados", command=entrada_dados)
btn_entrada.pack(pady=10)

# Iniciando o loop da interface
root.mainloop()
