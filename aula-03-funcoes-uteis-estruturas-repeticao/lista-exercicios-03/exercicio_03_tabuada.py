def gerar_tabuada():
    while True:
        try:
            numero = int(input("Informe um número inteiro entre 1 e 10 para ver a tabuada: "))
            if 1 <= numero <= 10:
                break
            else:
                print("Por favor, informe um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, informe um número inteiro.")

    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

if __name__ == "__main__":
    gerar_tabuada()