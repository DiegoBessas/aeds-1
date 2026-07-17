import os

tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]

def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(linha)

def jogada_valida(linha, coluna):
    if 1 <= linha <= 3 and 1 <= coluna <= 3 and tabuleiro[linha-1][coluna-1] == "":
        return True
    return False

def vencedor(jogada):
    # Verifica linhas, colunas e diagonais em uma única estrutura
    return any(
        all(tabuleiro[i][j] == jogada for j in range(3)) or  # Linha
        all(tabuleiro[j][i] == jogada for j in range(3))     # Coluna
        for i in range(3)
    ) or all(tabuleiro[i][i] == jogada for i in range(3)) or all(tabuleiro[i][2-i] == jogada for i in range(3))

def proxima_jogada(jogador):
    global numero_jogadas, jogador_1
    while True:
        linha = int(input(f"Jogador {jogador}, escolha a linha para a próxima jogada: "))
        coluna = int(input(f"Jogador {jogador}, escolha a coluna para a próxima jogada: "))
        if jogada_valida(linha, coluna):
            jogada = "X" if jogador == 1 else "0"
            tabuleiro[linha-1][coluna-1] = jogada
            numero_jogadas += 1
            if vencedor(jogada):
                mostrar_tabuleiro()
                print(f"Jogador {jogador} venceu!")
                exit()
            jogador_1 = not jogador_1
            break
        else:
            print("Jogada inválida. Tente novamente.")
            os.system('cls' if os.name == 'nt' else 'clear')
            mostrar_tabuleiro()

numero_jogadas = 0
jogador_1 = True

while numero_jogadas < 9:
    mostrar_tabuleiro()
    if jogador_1:
        proxima_jogada(1)
    else:
        proxima_jogada(2)