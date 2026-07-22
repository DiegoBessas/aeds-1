# Solicita ao usuário que digite um número
n = int(input("Digite um número: "))

# Inicializa a variável soma com 0
soma = 0

# Itera sobre todos os números de 1 até n-1
for i in range(1, n):
    # Verifica se i é um divisor de n
    if n % i == 0:
        # Se for, adiciona i à soma
        soma += i

# Verifica se a soma dos divisores é igual ao número
if soma == n:
    print(f"{n} é um número perfeito")
else:
    print(f"{n} não é um número perfeito")
