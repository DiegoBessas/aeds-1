import re

def validar_email(email: str) -> bool:
    """
    Verifica se uma string é um e-mail válido conforme as regras:
    - nome: letras, números, ., -, _
    - domínio: letras, números, hífens
    - formato: nome@dominio.extensao
    """
    padrao = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

# Solicita o e-mail ao usuário
email_usuario = input("Digite um e-mail para validar: ")
if validar_email(email_usuario):
    print("E-mail válido.")
else:
    print("E-mail inválido.")