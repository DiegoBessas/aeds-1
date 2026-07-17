#Inserir variável com o número de telefone (com e sem traço):
numero_tel = input("Digite seu número de telefone: ")
numero_sem_traco = numero_tel.replace("-", "")
#Verificar se o número de telefone é válido:
if len(numero_sem_traco) == 8:
    numero_sem_traco = '9' + numero_sem_traco
    if '-' in numero_tel:
        numero_tel = numero_sem_traco[:5] + '-' + numero_sem_traco[5:]
    else:
        numero_tel = numero_sem_traco
    print(numero_tel)
elif len(numero_sem_traco) == 9:
    print(numero_tel)
else:
    print("Número inválido")