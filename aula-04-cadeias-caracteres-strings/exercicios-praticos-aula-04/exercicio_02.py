nome = str(input("Digite seu nome: "))
nome = nome.upper()

for i in range(1, len(nome) + 1):
    print(nome[:i])