frase = input("Digite uma frase: ")

print(f"A frase digitada foi: {frase}")
print(f"Quantidade de espaços em branco: {frase.count(' ')}")

vogais = "aeiou"
total_vogais = sum(frase.lower().count(vogal) for vogal in vogais)

print(f"Quantidade total de vogais: {total_vogais}")