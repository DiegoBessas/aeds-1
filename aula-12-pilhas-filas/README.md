# Aula 12 — Pilhas e Filas

## Contexto

Décima segunda aula da disciplina, introduzindo duas estruturas de dados lineares fundamentais: pilhas e filas, ambas implementadas em Python usando listas como estrutura de suporte.

## Conceitos teóricos abordados

- **Pilha (Stack) — princípio LIFO (*Last In, First Out*):** o último elemento adicionado é o primeiro a ser removido, análoga a uma pilha de pratos. Operações principais:
  - `Push` — adiciona um elemento ao topo da pilha
  - `Pop` — remove o elemento do topo da pilha
  - `Peek` (ou `Top`) — retorna o elemento do topo sem removê-lo
  - `isEmpty` — verifica se a pilha está vazia
- **Fila (Queue) — princípio FIFO (*First In, First Out*):** o primeiro elemento adicionado é o primeiro a ser removido, análoga a uma fila de pessoas em um caixa. Operações principais:
  - `Enqueue` — adiciona um elemento ao final da fila
  - `Dequeue` — remove o elemento do início da fila
  - `Front` (ou `Peek`) — retorna o elemento do início sem removê-lo
  - `isEmpty` — verifica se a fila está vazia
- A aula apresentou o pseudocódigo de cada operação antes da implementação em Python.

## Atividades práticas

Ambos os programas implementam a estrutura de dados sobre uma lista Python nativa e oferecem um menu interativo em loop para testar todas as operações.

### Pilha interativa

Ver [`pilha-interativa/pilha_01.py`](./pilha-interativa/pilha_01.py) — implementa `inserir` (push), `remover` (pop), `topo` (peek), `pilhaVazia` (isEmpty), `tamanho` e `imprimir`, usando `pilha.append()` para inserir e `pilha.pop()` (sem índice, removendo o último elemento) para remover — o que reproduz corretamente o comportamento LIFO.

### Fila interativa

Ver [`fila-interativa/fila_01.py`](./fila-interativa/fila_01.py) — implementa `inserir` (enqueue), `remover` (dequeue), `frente` (front), `filaVazia` (isEmpty), `tamanho` e `imprimir`, usando `fila.append()` para inserir e `fila.pop(0)` para remover o primeiro elemento — reproduzindo o comportamento FIFO.

> Nota técnica: ambas as implementações usam uma lista Python padrão como estrutura de suporte. Isso é didaticamente claro e correto, mas vale mencionar que `pilha.pop()` é uma operação eficiente (O(1)) enquanto `fila.pop(0)` tem custo O(n), pois desloca todos os elementos restantes uma posição para trás — para uma fila mais eficiente, a biblioteca padrão do Python oferece `collections.deque`, otimizada para remoções em ambas as extremidades.

## Como executar

```bash
python3 pilha-interativa/pilha_01.py
python3 fila-interativa/fila_01.py
```

## Referência

Material teórico baseado no slide "AEDS - Aula 12 - Filas e Pilhas", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
