conta=float(input("Digite o valor da conta: "))
tempo=int(input("Digite o tempo em anos: "))
contador=1
while contador<=(tempo*12):
    conta=conta*1.01
    contador=contador+1
    print('Conta: '+str(round(conta,2)))