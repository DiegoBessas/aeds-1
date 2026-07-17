tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]

def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(linha)

numero_jogadas = 0
jogador_1 = True

while numero_jogadas < 9:
    mostrar_tabuleiro()
    if jogador_1:
        linha=int(input("Jogador 1, escolha a linha proxima jogada: "))
        coluna=int(input("Jogador 1, escolha a coluna proxima jogada: "))     
        if tabuleiro[linha-1][coluna-1] == "":
            numero_jogadas = numero_jogadas + 1
            jogador_1 = False
            tabuleiro[linha-1][coluna-1] = "X"
    else:
        linha=int(input("Jogador 2, escolha a linha proxima jogada: "))
        coluna=int(input("Jogador 2, escolha a coluna proxima jogada: "))
        if tabuleiro[linha-1][coluna-1] == "":
            numero_jogadas = numero_jogadas + 1
            jogador_1 = True
            tabuleiro[linha-1][coluna-1] = "0"