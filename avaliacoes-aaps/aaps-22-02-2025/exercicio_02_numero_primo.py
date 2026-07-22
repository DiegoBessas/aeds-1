# Solicitar um número inteiro positivo
numero = int(input("Digite um número inteiro positivo para verificar se é primo: "))

# Função para verificar se um número é primo
def num_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Verificar se o número é primo e exibir o resultado
if num_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")