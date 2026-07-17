numero1=int(input("Insira o primeiro número: "))
numero2=int(input("Insira o segundo número: "))
if numero1>numero2:
    menor=numero2
    maior=numero1
else:
    menor=numero1
    maior=numero2
for numero in range(menor,maior+1):
    print(numero)