import numpy as np

# Notas dos alunos da FANS
notas = np.array([8.5, 5.0, 7.5, 9.0, 6.5, 4.0, 8.0])

print("--- Estatísticas da Turma ---")
print(f"Média: {np.mean(notas):.2f}")
print(f"Desvio Padrão: {np.std(notas):.2f}")
print(f"Maior Nota: {np.max(notas)}")
print(f"Menor Nota: {np.min(notas)}")

# Filtrando o array com uma condição booleana (aprovados)
aprovados = notas[notas >= 7]
print(f"\nNotas acima da média (Aprovados): {aprovados}")