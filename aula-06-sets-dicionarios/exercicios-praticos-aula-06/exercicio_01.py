entrada = input("Digite os números separados por vírgula: ")
lista1 = [int(num) for num in entrada.split(",")]  # Converte a entrada em uma lista de inteiros

# Verifica se há duplicatas comparando o tamanho da lista original com o conjunto
tem_duplicatas = len(lista1) != len(set(lista1))

print(f"Existe pelo menos um número repetido? {tem_duplicatas}")