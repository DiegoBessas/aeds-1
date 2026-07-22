from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Carregando o dataset embutido sobre vinhos
wine = load_wine()
X = wine.data
y = wine.target

# Criando e treinando o modelo KNN (K-Nearest Neighbors)
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

# Fazendo previsões nos próprios dados de treino (para fins de teste prático)
previsoes = modelo.predict(X)

# Calculando a acurácia
acuracia = accuracy_score(y, previsoes)
print(f"Acurácia do modelo KNN nos dados de treino: {acuracia * 100:.2f}%")