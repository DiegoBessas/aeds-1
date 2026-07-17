def data(dia, mes, ano, por_extenso=False):
    meses_por_extenso = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    
    if por_extenso:
        mes_extenso = meses_por_extenso[int(mes) - 1]
        print(f"{dia} de {mes_extenso} de {ano}")
    else:
        print(f"{dia}/{mes}/{ano}")

# Exemplos de uso:
data("29", "04", "1989")          # Saída: 29/04/1989
data("29", "04", "1989", True)   # Saída: 29 de abril de 1989