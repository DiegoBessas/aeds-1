import pandas as pd

# Series (coluna única)
s = pd.Series([1, 3, 5, 7, 9])

# DataFrame (cria a tabela )
df = pd.DataFrame({
    'Nome': ['Ana', 'João', 'Maria'],
    'Idade': [25, 30, 28],
    'Salário': [5000.0, 4500.5, 6000.0]
})

print(s)# Imprime uma lista em formato de coluna
print(df)#Imprime o dataFrame em formato de tabela
