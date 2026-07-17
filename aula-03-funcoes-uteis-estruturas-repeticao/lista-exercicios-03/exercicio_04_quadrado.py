def imprimir_quadrado():
    while True:
        try:
            tamanho = int(input("Informe o tamanho do lado do quadrado (entre 1 e 20): "))
            if 1 <= tamanho <= 20:
                break
            else:
                print("Por favor, informe um número entre 1 e 20.")
        except ValueError:
            print("Entrada inválida. Por favor, informe um número inteiro.")

    for i in range(tamanho):
        print('*' * tamanho)

if __name__ == "__main__":
    imprimir_quadrado()