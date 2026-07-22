import tensorflow as tf

# Criando dois tensores
tensor_a = tf.constant([[1, 2], [3, 4]])
tensor_b = tf.constant([[10, 20], [30, 40]])

# Soma elemento a elemento
soma = tf.add(tensor_a, tensor_b)
print("--- Soma dos Tensores ---")
print(soma.numpy())

# Calculando a transposta da Matriz A
transposta_a = tf.transpose(tensor_a)
print("\n--- Transposta da Matriz A ---")
print(transposta_a.numpy())