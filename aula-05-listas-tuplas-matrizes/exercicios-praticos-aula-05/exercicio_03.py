num1=int(input('Informe um número: '))
num2=int(input('Informe um número: '))
num3=int(input('Informe um número: '))
num4=int(input('Informe um número: '))
num5=int(input('Informe um número: '))
num6=int(input('Informe um número: '))
num7=int(input('Informe um número: '))
num8=int(input('Informe um número: '))
num9=int(input('Informe um número: '))
num10=int(input('Informe um número: '))

vetor=[num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
vetor_par=[]
vetor_impar=[]
for i in vetor:
    if i%2==0:
        vetor_par.append(i)
    else:
        vetor_impar.append(i)
print('Números pares: ', vetor_par)
print('Números ímpares: ', vetor_impar)
print('Vetor completo: ', vetor)