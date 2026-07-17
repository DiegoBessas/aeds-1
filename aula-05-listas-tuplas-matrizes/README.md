# Aula 05 — Listas, Tuplas e Matrizes

## Contexto

Quinta aula da disciplina, dedicada aos tipos de dados compostos (collections) do Python: listas, tuplas e matrizes (listas de listas). É a primeira aula em que os desafios/exercícios exigem estruturar e manipular coleções de dados, em vez de trabalhar apenas com variáveis individuais.

## Conceitos teóricos abordados

- **Listas (vetores):** armazenam múltiplos itens em uma única variável, mantendo a ordem e permitindo valores duplicados e do tipo misto (strings, números, booleanos).
  - Acesso por índice (incluindo índices negativos, ex.: `lista[-1]` para o último item) e por *slicing* (`lista[1:3]`, `lista[:3]`, `lista[2:]`).
  - Funções e métodos: `len()`, `type()`, atribuição direta a um índice ou fatia, `in` (para verificar pertencimento), `for` para iterar sobre os itens, `insert()`, `append()`, `extend()`, `remove()`, `pop()`, `clear()`, `sort()` (incluindo `reverse=True`), `reverse()`.
  - **Cópia de listas:** três formas comparadas — atribuição direta (`lista2 = lista1`, que cria uma referência à mesma lista, então alterações em uma afetam a outra), `lista1.copy()` e `list(lista1)` (ambas criam uma cópia independente).
- **Tuplas:** semelhantes às listas (mantêm ordem, permitem duplicados), mas **imutáveis** após a criação, com melhor performance do que listas.
- **Comparação entre collections:** lista (ordenada, mutável, com duplicados), tupla (ordenada, imutável, com duplicados), set (não ordenado, não indexado, imutável, sem duplicados) e dicionário (ordenado, mutável, sem chaves duplicadas).
- **Matrizes (listas de listas):** uma lista cujos elementos são, eles próprios, listas — usada, por exemplo, para associar a cada aluno (uma posição da lista externa) uma lista com nome e notas. Acesso feito com dupla indexação (`matriz[linha][coluna]`).

## Atividades práticas

### Exercícios práticos da Aula 05

A pasta [`exercicios-praticos-aula-05`](./exercicios-praticos-aula-05/) contém a resolução dos 6 exercícios propostos:

1. **`exercicio_01.py`** — lê um vetor de 10 números e o exibe na ordem inversa, usando `.reverse()`.
2. **`exercicio_02.py`** — lê 4 notas, armazena em uma lista e calcula a média.
3. **`exercicio_03.py`** — lê 10 números inteiros e separa em dois vetores (pares e ímpares).
4. **`exercicio_04.py`** — simula 20 lançamentos de um dado (`random.randint`), armazenando os resultados em um vetor e contabilizando a frequência de cada valor (1 a 6) em um vetor de contadores.
5. e 6. **`exercicios_05_e_06.py`** — cadastro de alunos com notas em 3 etapas (utilizando uma lista de tuplas `(nome, nota1, nota2, nota3, nota_total)`), cálculo da nota total de cada aluno, da média da turma e listagem dos alunos abaixo da média.

### Desafio 5 — Jogo da Velha

**Enunciado:** representar um Jogo da Velha usando uma matriz 3×3, em que cada posição pode conter `"X"` (jogador 1), `"O"` (jogador 2) ou `""` (vazia). O programa deve encerrar quando todas as posições estiverem ocupadas (não é necessário identificar o vencedor). Assume-se que os jogadores sempre escolhem jogadas válidas.

A pasta [`desafio-05-jogo-da-velha`](./desafio-05-jogo-da-velha/) contém duas versões da solução:

- **`desafio_05_v1.py`** — implementação com um laço `while` controlando o número de jogadas, alternando entre os dois jogadores a cada rodada (`jogador_1 = not jogador_1`). Verifica se a posição escolhida já está ocupada e, nesse caso, usa `continue` para pedir uma nova jogada ao mesmo jogador, sem avançar o contador. Os índices de linha/coluna são usados diretamente como digitados (0, 1 ou 2).
- **`desafio_05_v2.py`** — segunda versão, com uma abordagem diferente: os índices informados pelo usuário são tratados como base 1 (subtraindo 1 internamente, ou seja, o jogador digita 1, 2 ou 3). Aqui, se a posição escolhida pelo jogador 1 já estiver ocupada, o programa não pede uma nova jogada ao mesmo jogador — em vez disso, solicita a jogada diretamente ao jogador 2, sem exibir mensagem de posição ocupada.

## Como executar

```bash
python3 exercicios-praticos-aula-05/exercicio_04.py
python3 desafio-05-jogo-da-velha/desafio_05_v1.py
```

## Referência

Material teórico baseado no slide "AEDS - Aula 5", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
