carros = []  # Lista para armazenar os carros cadastrados
quantidade = int(input("Informe a quantidade de carros a serem cadastrados: "))

for i in range(quantidade):
    print(f"\nCadastro do carro {i + 1}:")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    quilometragem = int(input("Quilometragem: "))
    preco_venda = float(input("Preço de venda: "))

    # Adiciona o carro como um dicionário na lista
    carro = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "quilometragem": quilometragem,
        "preco_venda": preco_venda
    }
    carros.append(carro)

# Exibe todos os carros cadastrados
print("\nCarros cadastrados:")
for carro in carros:
    print(carro)