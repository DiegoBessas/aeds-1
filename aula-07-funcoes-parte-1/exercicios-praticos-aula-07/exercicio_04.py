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
    # Verifica linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] == jogada:
            return True
    # Verifica colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogada:
            return True
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogada:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogada:
        return True
    return False

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