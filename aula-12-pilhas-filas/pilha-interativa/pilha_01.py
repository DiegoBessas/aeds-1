def inserir(pilha, elemento):
    pilha.append(elemento)

def remover(pilha):
    if not pilhaVazia(pilha):
        return pilha.pop()
    else:
        return "Erro: Pilha vazia"

def topo(pilha):
    if not pilhaVazia(pilha):
        return pilha[-1]
    else:
        return "Erro: Pilha vazia"

def pilhaVazia(pilha):
    return len(pilha) == 0

def tamanho(pilha):
    return len(pilha)

def imprimir(pilha):
    return str(pilha)

def main():# Função para inicializar nosso app.
    pilha = []

##---------------------------- Lógica do APP ---------------------------
    
    while True:
        print("\nMenu:")
        print("1. Adicionar elemento (push)")
        print("2. Remover elemento (pop)")
        print("3. Ver elemento do topo (peek)")
        print("4. Verificar se a pilha está vazia")
        print("5. Ver tamanho da pilha")
        print("6. Ver pilha")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            elemento = input("Digite o elemento a ser adicionado: ")
            inserir(pilha, elemento)
            print(f"Elemento '{elemento}' adicionado à pilha.")
        
        elif escolha == '2':
            resultado = remover(pilha)
            print(f"Elemento removido: {resultado}")
        
        elif escolha == '3':
            resultado = topo(pilha)
            print(f"Elemento do topo: {resultado}")
        
        elif escolha == '4':
            if pilhaVazia(pilha):
                print("A pilha está vazia.")
            else:
                print("A pilha não está vazia.")
        
        elif escolha == '5':
            print(f"Tamanho da pilha: {tamanho(pilha)}")
        
        elif escolha == '6':           
            print(f"Listando a pilha: {imprimir(pilha)}")
        
        elif escolha == '7':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
