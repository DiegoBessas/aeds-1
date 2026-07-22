# Solicitar um número inteiro positivo
N = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é positivo
if N <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    # Inicializar a lista com os dois primeiros termos da sequência de Fibonacci
    fibonacci = [0, 1]
    
    # Gerar a sequência de Fibonacci até ter N termos
    while len(fibonacci) < N:
        # Adicionar o próximo termo da sequência de Fibonacci à lista
        fibonacci.append(fibonacci[-1] + fibonacci[-2])  # Soma os dois últimos termos e adiciona à lista
    
    # Exibir os N primeiros termos da sequência de Fibonacci
    print(f"Os {N} primeiros termos da sequência de Fibonacci são: {fibonacci[:N]}")