import pandas as pd

# Criando a base de dados
dados = {
    'Produto': ['Teclado Mecânico', 'Mouse Gamer', 'Monitor 144Hz', 'Cadeira Ergonomica', 'Mousepad'],
    'Categoria': ['Periféricos', 'Periféricos', 'Monitores', 'Móveis', 'Periféricos'],
    'Preço': [250.0, 120.0, 1100.0, 950.0, 60.0]
}
df = pd.DataFrame(dados)

# Filtrando apenas os produtos da categoria 'Periféricos'
perifericos = df[df['Categoria'] == 'Periféricos']
print("--- Apenas Periféricos ---")
print(perifericos)

# Calculando o preço médio agrupado por Categoria
preco_medio = df.groupby('Categoria')['Preço'].mean()
print("\n--- Preço Médio por Categoria ---")
print(preco_medio)