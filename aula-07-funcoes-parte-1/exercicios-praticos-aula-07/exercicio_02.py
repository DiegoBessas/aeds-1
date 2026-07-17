tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]

def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(linha)

def proxima_jogada(jogador):
    global numero_jogadas, jogador_1
    linha = int(input(f"Jogador {jogador}, escolha a linha para a próxima jogada: "))
    coluna = int(input(f"Jogador {jogador}, escolha a coluna para a próxima jogada: "))
    if tabuleiro[linha-1][coluna-1] == "":
        tabuleiro[linha-1][coluna-1] = "X" if jogador == 1 else "0"
        numero_jogadas += 1
        jogador_1 = not jogador_1
    else:
        print("Posição já ocupada. Tente novamente.")

numero_jogadas = 0
jogador_1 = True

while numero_jogadas < 9:
    mostrar_tabuleiro()
    if jogador_1:
        proxima_jogada(1)
    else:
        proxima_jogada(2)