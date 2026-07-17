conta=float(input('Informe o valor da operação: '))
tempo=int(input('Informe o tempo da aplicação em anos: '))
for contador in range(tempo*12):conta=conta*1.01
print(contador)
print('Conta: '+str(round(conta,2)))
