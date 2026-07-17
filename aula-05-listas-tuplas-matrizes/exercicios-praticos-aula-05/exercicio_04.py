import random

# Vetor para armazenar os resultados dos lançamentos
resultados = []

# Vetor de contadores para os valores de 1 a 6
contadores = [0, 0, 0, 0, 0, 0]

# Simula 20 lançamentos do dado
for _ in range(20):
    lado = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6
    resultados.append(lado)      # Armazena o resultado no vetor
    contadores[lado - 1] += 1    # Incrementa o contador correspondente

# Exibe os resultados
print("Execuções:", resultados)
print("Contadores:", contadores)

