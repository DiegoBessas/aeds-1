tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]
for linha in tabuleiro:
    print(linha)

numero_jogadas = 0
jogador_1 = True
while numero_jogadas < 9:
    if jogador_1:
        print("Vez do jogador 1 (X)")
        simbolo = "X"
    else:
        print("Vez do jogador 2 (O)")
        simbolo = "O"

    linha = int(input("Escolha a linha (0, 1 ou 2): "))
    coluna = int(input("Escolha a coluna (0, 1 ou 2): "))

    if tabuleiro[linha][coluna] == "":
        tabuleiro[linha][coluna] = simbolo
        numero_jogadas += 1
    else:
        print("Essa posição já está ocupada! Tente novamente.")
        continue

    for linha in tabuleiro:
        print(linha)

    jogador_1 = not jogador_1