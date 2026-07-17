nome = input('Digite seu nome: ')
nome_maiusculo = nome.upper()

def inverter(nome):
    return nome[::-1]

nome_invertido = inverter(nome_maiusculo)
print(nome_invertido)