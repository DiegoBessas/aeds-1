import re

def validar_senha(senha):
    # Pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    # Pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False
    # Pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False
    # Pelo menos um número
    if not re.search(r'\d', senha):
        return False
    # Pelo menos um caractere especial
    if not re.search(r'[@#$%^&*]', senha):
        return False
    return True

# Input do usuário
senha_usuario = input("Digite uma senha para validar: ")
if validar_senha(senha_usuario):
    print("Senha forte!")
else:
    print("Senha fraca!")