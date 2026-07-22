from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Criando um modelo com uma camada extra
modelo = Sequential([
    Dense(16, activation='relu', input_shape=(8,)), # Camada de entrada
    Dense(8, activation='relu'),                    # Nova camada oculta
    Dense(1, activation='sigmoid')                  # Camada de saída (ex: classificação binária)
])

# Compilando o modelo com otimizador SGD
modelo.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

print("--- Resumo da Arquitetura da Rede Neural ---")
modelo.summary()