def inserir(fila, elemento):
    fila.append(elemento)

def remover(fila):
    if not filaVazia(fila):
        return fila.pop(0)  # Remove o primeiro elemento da fila
    else:
        return "Erro: Fila vazia"

def frente(fila):
    if not filaVazia(fila):
        return fila[0]  # Retorna o primeiro elemento da fila
    else:
        return "Erro: Fila vazia"

def filaVazia(fila):
    return len(fila) == 0

def tamanho(fila):
    return len(fila)

def imprimir(fila):
    return str(fila)

def main():  # Função para inicializar nosso app.
    fila = []

    ##---------------------------- Lógica do APP ---------------------------
    
    while True:
        print("\nMenu:")
        print("1. Adicionar elemento (enqueue)")
        print("2. Remover elemento (dequeue)")
        print("3. Ver elemento da frente (front)")
        print("4. Verificar se a fila está vazia")
        print("5. Ver tamanho da fila")
        print("6. Ver fila")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            elemento = input("Digite o elemento a ser adicionado: ")
            inserir(fila, elemento)
            print(f"Elemento '{elemento}' adicionado à fila.")
        
        elif escolha == '2':
            resultado = remover(fila)
            print(f"Elemento removido: {resultado}")
        
        elif escolha == '3':
            resultado = frente(fila)
            print(f"Elemento da frente: {resultado}")
        
        elif escolha == '4':
            if filaVazia(fila):
                print("A fila está vazia.")
            else:
                print("A fila não está vazia.")
        
        elif escolha == '5':
            print(f"Tamanho da fila: {tamanho(fila)}")
        
        elif escolha == '6':           
            print(f"Listando a fila: {imprimir(fila)}")
        
        elif escolha == '7':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
