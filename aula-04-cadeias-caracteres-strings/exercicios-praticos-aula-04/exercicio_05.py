def eh_palindromo(sequencia):
    sequencia = sequencia.replace(" ", "").lower()
    return sequencia == sequencia[::-1]

sequencia = input("Digite uma sequência de caracteres: ")
print(f"A sequência digitada foi: {sequencia}")

if eh_palindromo(sequencia):
    print("A sequência é um palíndromo.")
else:
    print("A sequência não é um palíndromo.")