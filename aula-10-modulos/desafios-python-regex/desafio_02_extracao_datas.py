import re

def extrair_datas(texto):
    # Padrão para datas no formato dd/mm/aaaa
    dia = r'(0[1-9]|[12][0-9]|3[01])'      # 01 a 31
    mes = r'(0[1-9]|1[0-2])'               # 01 a 12
    ano = r'(19[0-9]{2}|20[0-9]{2})'       # 1900 a 2099
    padrao = rf'\b{dia}/{mes}/{ano}\b'
    return [m.group(0) for m in re.finditer(padrao, texto)]

# Solicita o texto ao usuário
texto = input("Digite o texto: ")
print(extrair_datas(texto))