#Inserir as notas que o aluno tirou:
nota1=float(input('Informe a 1ª nota: '))
nota2=float(input('Informe 2ª nota: '))
nota3=float(input('Informe 3ª nota: '))
nota4=float(input('Informe 4ª nota: '))
nota5=float(input('Informe 5ª nota: '))
#Calcular a média das notas:
soma=(nota1+nota2+nota3+nota4+nota5)
media=(soma/5)
print(media)
#Verificar se a média é maior ou igual a 7:
if(media>=0)and(media<7):print('Reprovado.')
elif(media==10):print('Aprovado com Distinção!')
elif(media>=7)and(media<10):print('Aprovado.')
else:print('Valor inválido!')
#Fim do programa