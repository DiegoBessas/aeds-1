def media(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / len(numeros)
    return media

print(media(1, 2, 3))
print(media(1, 2, 3, 4, 5, 6))
print(media(-1, 4, 2, -3, 10))