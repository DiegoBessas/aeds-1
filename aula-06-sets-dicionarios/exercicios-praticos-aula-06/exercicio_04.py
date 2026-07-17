N = 50  # Gerar o dicionário com os quadrados de 1 a 50
resultado = {i: i**2 for i in range(1, N + 1)}

# Exibir os quadrados dos valores solicitados
valores = [5, 15, 28, 36, 47]
for valor in valores:
    print(f"O quadrado de {valor} é {resultado[valor]}")