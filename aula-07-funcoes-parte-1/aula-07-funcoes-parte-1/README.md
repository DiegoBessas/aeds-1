# Aula 07 — Funções (Parte 1)

## Contexto

Sétima aula da disciplina, dedicada à introdução de funções em Python. O ponto alto da aula é didaticamente interessante: em vez de exercícios isolados, os 5 exercícios práticos formam uma **sequência evolutiva única**, partindo da implementação "crua" do Jogo da Velha (a mesma base do Desafio 5, da [Aula 05](../aula-05-listas-tuplas-matrizes/)) e refatorando-a passo a passo, introduzindo um novo conceito de função a cada etapa.

## Conceitos teóricos abordados

- **Função:** parte do programa responsável por executar uma tarefa específica e, opcionalmente, retornar um valor; usada para "montar" o programa em blocos reutilizáveis, independentemente da linguagem. Em Python, definida com a palavra-chave `def`.
- **Vantagens de funções:** reuso de código (definir uma vez, usar várias vezes), manutenibilidade (código mais compreensível e conciso) e abstração de implementações (permite focar no que ainda não foi implementado).
- **Funções embutidas (built-in):** exemplos revisados — `print()`, `len()`, `input()`, `range()`.
- **Parâmetros e retorno de valores:** funções podem receber parâmetros (alterando seu comportamento a cada chamada) e podem devolver um valor com `return`.
- **Escopo de variáveis:** variáveis declaradas dentro de uma função só são visíveis dentro dela; variáveis declaradas no escopo global são visíveis a todas as funções chamadas a partir do ponto de declaração. A aula demonstrou casos onde a ordem de declaração de uma variável global afeta se ela estará ou não disponível dentro de uma função no momento em que é chamada.

## Atividades práticas — evolução do Jogo da Velha

A pasta [`exercicios-praticos-aula-07`](./exercicios-praticos-aula-07/) contém as 5 versões incrementais do jogo, cada uma introduzindo uma nova função sobre a versão anterior:

1. **`exercicio_01.py`** — ponto de partida: a implementação original do Jogo da Velha (idêntica em lógica à base usada no Desafio 5), agora com a exibição do tabuleiro extraída para uma função própria: `mostrar_tabuleiro()`.
2. **`exercicio_02.py`** — extrai a lógica de uma jogada para a função `proxima_jogada(jogador)`, que recebe o jogador atual como parâmetro e atualiza o tabuleiro e as variáveis de controle (usando `global` para acessar `numero_jogadas` e `jogador_1` a partir da função).
3. **`exercicio_03.py`** — adiciona a função `jogada_valida(linha, coluna)`, que retorna `True`/`False` conforme a posição escolhida seja válida (dentro dos limites do tabuleiro e ainda vazia). Quando a jogada é inválida, a tela é limpa (`os.system`) e o tabuleiro é reexibido antes de pedir uma nova jogada ao mesmo jogador.
4. **`exercicio_04.py`** — adiciona a função `vencedor(jogada)`, verificando explicitamente todas as linhas, colunas e as duas diagonais do tabuleiro após cada jogada; se houver um vencedor, o jogo é encerrado com uma mensagem.
5. **`exercicio_05.py`** — reescreve `vencedor(jogada)` de forma mais concisa, combinando a verificação de linhas, colunas e diagonais em uma única expressão usando `any()`/`all()` com *generator expressions*, no lugar dos laços explícitos da versão anterior.

## Como executar

```bash
python3 exercicios-praticos-aula-07/exercicio_05.py
```

> Os programas são interativos (jogo da velha via terminal) — as versões 4 e 5 já identificam o vencedor.

## Referência

Material teórico baseado no slide "AEDS - Aula 7", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
