#Importar a biblioteca random
import random
#Criar um programa que simule o jogo pedra, papel e tesoura
minha_acao=input("Digite PE(pedra), PA (papel) ou T(tesoura): ")
acao_oponente=random.choice(["PE","PA","T"])
print(f'A sua ação foi {minha_acao} e a ação do oponente foi {acao_oponente}')
#Criar as condições para o jogo
if minha_acao==acao_oponente:
    print("Empate")
elif minha_acao=="PE" and acao_oponente=="T":
    print("Você ganhou")
elif minha_acao=="PA" and acao_oponente=="PE":
    print("Você ganhou")
elif minha_acao=="T" and acao_oponente=="PA":
    print("Você ganhou")
else:
    print("Você perdeu")
