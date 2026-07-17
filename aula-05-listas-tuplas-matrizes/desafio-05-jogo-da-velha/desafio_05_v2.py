tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]
for linha in tabuleiro:
    print(linha)

numero_jogadas = 0
jogador_1 = True
while numero_jogadas < 9:
    if jogador_1:
        linha = int(input("Jogador 1, escolha a linha da próxima jogada: "))
        coluna = int(input("Jogador 1, selecione a coluna da próxima jogada: "))
        if tabuleiro[linha-1][coluna-1] == "":
            numero_jogadas += 1
            jogador_1 = False
            tabuleiro[linha-1][coluna-1] = "X"
        else:
            linha = int(input("Jogador 2, escolha a linha da próxima jogada: "))
            coluna = int(input("Jogador 2, selecione a coluna da próxima jogada: "))
            if tabuleiro[linha-1][coluna-1] == "":
                numero_jogadas += 1
                jogador_1 = True
                tabuleiro[linha-1][coluna-1] = "O"
        for linha in tabuleiro:
            print(linha)