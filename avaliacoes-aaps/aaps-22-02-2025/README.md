# AAPS — 22/02/2025 — Exercícios Práticos de Algoritmos e Estruturas de Dados

## Contexto

Avaliação prática aplicada no início do semestre, reunindo 8 exercícios clássicos de lógica de programação, cobrindo desde cálculos matemáticos simples até um pequeno jogo. Pela data (bem no começo do período letivo), essa atividade foi resolvida em paralelo às primeiras aulas da disciplina, exercitando conceitos como laços de repetição, condicionais, funções e o módulo `random`.

## Exercícios

1. **`exercicio_01_fatorial.py`** — calcula o fatorial de um número inteiro positivo informado pelo usuário, usando um laço `for`.
2. **`exercicio_02_numero_primo.py`** — verifica se um número é primo, testando divisibilidade até a raiz quadrada do número (função `num_primo`).
3. **`exercicio_03_media_notas.py`** — lê 5 notas, calcula a média e classifica como aprovado, reprovado ou aprovado com distinção.
   > **Observação:** o enunciado exemplifica a saída no formato `Média: 7.0 - Aprovado`; a implementação exibe a média e o resultado da classificação em `print`s separados (`7.0` seguido de `Aprovado.`), o que transmite a mesma informação, mas em formato diferente do exemplificado.
4. **`exercicio_04_fibonacci.py`** — gera os N primeiros termos da sequência de Fibonacci, usando uma lista e um laço `while`.
5. **`exercicio_05_numero_perfeito.py`** — verifica se um número é perfeito (a soma de seus divisores próprios é igual a ele mesmo), com o exemplo clássico de 28 (1 + 2 + 4 + 7 + 14 = 28).
6. **`exercicio_06_pedra_papel_tesoura.py`** — jogo de pedra, papel e tesoura contra o computador, com a jogada do computador sorteada via `random.choice(...)`.
7. **`exercicio_07_piramide_numerica.py`** — desenha uma pirâmide numérica com N linhas, usando dois laços `for` aninhados.
   > **Observação:** o enunciado exemplifica a saída como números concatenados sem espaço em cada linha (`1`, `12`, `123`, `1234`, `12345`); a implementação imprime os números separados por espaço em cada linha (`1`, `1 2`, `1 2 3`, `1 2 3 4`, `1 2 3 4 5`), formando a mesma pirâmide crescente, porém com espaçamento diferente do exemplo.
8. **`exercicio_08_conversor_base.py`** — converte um número decimal para binário e hexadecimal, usando as funções embutidas `bin()` e `hex()`.

Todos os exercícios foram testados e produzem os resultados esperados (à exceção das duas diferenças de formatação de saída pontuadas acima, que não afetam a lógica da solução).

## Como executar

```bash
python3 exercicio_01_fatorial.py
python3 exercicio_06_pedra_papel_tesoura.py
```

## Referência

Enunciado: "Exercícios Práticos de Algoritmos e Estruturas de Dados - AAPS", FANS, 22/02/2025.
