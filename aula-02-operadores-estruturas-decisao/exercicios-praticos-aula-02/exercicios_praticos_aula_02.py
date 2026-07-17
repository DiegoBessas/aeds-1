print('EXERCÍCIO 1:')
print('Olá')
print('Meu primeiro programa')

print('EXERCÍCIO 2:')
nome=input('Informe seu nome: ')
print('Olá, '+nome+'!')

print('EXCERCICIO 3:')
numero_1=int(input('Informe o número 1: '))
numero_2=int(input('Informe o número 2: '))
numero_3=int(input('Informe o número 3: '))
soma=numero_1+numero_2+numero_3
media = soma / 3
print(media)

print('EXCERCÍCIO 4:')
conta=float(input('Informe o valor do investimento: '))
conta=1.01*conta
conta=1.01*conta
conta=1.01*conta
print('O valor do resgate será igual a:')
print(conta)

print('EXCERCÍCIO 5')
idade = int(input('Informe a idade: '))
if(idade >= 18):print('Você é maior de idade.')
else:print('Você é menor de idade.')

print('EXCERCÍCIO 6')
F=int(input("Informe a temperatura em graus Fahrenheit: "))
C=5*((F-32)/9)
print('O valor em ºC é:')
print("C = "+str(C))

print('EXCERCÍCIO 7')
numero1=int(input("Inserir 1º número: "))
numero2=int(input("Inserir 2º número: "))
numero3=int(input("Inserir 3º número: "))
if (numero1 > numero2):print("1º número é maior")
elif(numero1 > numero3):print("1º número é maior")
elif(numero2 > numero3):print("2º número é maior")
else:print("3º número é maior")

print('EXCERCÍCIO 8')
numero=int(input('Informe o número: '))
if(numero%2==0):print('O número é par.')
else:print('O número é ímpar.')

print('EXCERCÍCIO 9')
mes=int(input("Informe o mês escolhendo um número de 1 a 12: "))
if mes==1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:print('O número de dias é igual a 31')
elif mes == 11 or mes == 9 or mes == 6 or mes == 4:print('O número de dias é igual a 30')
elif mes == 2:print('O número de dias é igual a 28')
else:print('O mês informado é inválido!')
