import re

def buscar_palavras(texto):
    return re.findall(r'\b\w*ção\b', texto, re.IGNORECASE)

texto = input("Digite o texto: ")
print(buscar_palavras(texto))