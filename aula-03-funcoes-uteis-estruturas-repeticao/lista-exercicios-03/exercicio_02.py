n=int(input('Digite a quantidade de pessoas na turma: '))
soma_idades=0
for i in range(n):
    idade=int(input('Digite a idade da pessoa: '))
    soma_idades+=idade
media=soma_idades/n
print('A média de idade da turma é: ',media)
round(media,2)
if 0 <= media <= 25:
    print("Turma jovem")
elif 26 <= media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")