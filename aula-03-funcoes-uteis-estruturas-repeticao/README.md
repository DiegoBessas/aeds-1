# Aula 03 — Funções Úteis e Estruturas de Repetição

## Contexto

Terceira aula da disciplina. Inicia com a revisão do Desafio 2 (dia da semana), apresenta um conjunto de funções nativas úteis do Python e introduz as estruturas de repetição (`for` e `while`), fechando com uma aula prática em laboratório.

## Conceitos teóricos abordados

- **Funções úteis do Python:**
  - `range(n)` — gera uma sequência de números
  - `.lower()` / `.upper()` — conversão de caixa em strings
  - `round(valor, casas)` — arredondamento de números decimais
  - `len(...)` — tamanho de uma string ou coleção
- **Estruturas de repetição:** motivação central — quando não se sabe a priori quantas vezes um bloco de instruções deve ser executado (ex.: somar os números de 1 a N, sendo N informado dinamicamente pelo usuário), usa-se uma estrutura de repetição em vez de repetir instruções manualmente.
  - **`while`:** repete um bloco enquanto uma condição permanecer verdadeira; controle manual do contador (incremento feito explicitamente pelo programador). Foi demonstrada a mecânica de rastreamento de estado a cada iteração (tabela de valores de `contador` e `resultado`), incluindo um exemplo didático de **loop infinito** (quando o contador é decrementado em vez de incrementado, a condição nunca se torna falsa).
  - **`for`:** itera diretamente sobre uma sequência gerada por `range(...)`, sem necessidade de incrementar o contador manualmente.
  - **Comparativo FOR x WHILE:** o `for` não exige incremento manual do contador e usa `range`; o `while` exige controle manual do contador e tem maior risco de loop infinito se mal implementado.
- Os arquivos [`exemplos-teoricos-for-while/comando_for.py`](./exemplos-teoricos-for-while/comando_for.py) e [`comando_while.py`](./exemplos-teoricos-for-while/comando_while.py) reproduzem o exemplo de sala de aula (soma dos números de 1 a N) nas duas versões, `for` e `while`.

## Atividades práticas

### Desafio 3 — Validação de dados cadastrais

**Enunciado:** ler e validar as seguintes informações, pedindo novamente ao usuário sempre que o valor informado for inválido:
- Nome: maior que 3 caracteres
- Idade: entre 0 e 150
- Salário: maior que zero
- Sexo: `'f'` ou `'m'`
- Estado civil: `'s'`, `'c'`, `'v'` ou `'d'`

Ver [`desafio-03-validacao-dados/desafio_03.py`](./desafio-03-validacao-dados/desafio_03.py) — implementado com uma sequência de laços `while True` com `break` condicional, um padrão comum para repetir a solicitação de um dado até que ele seja válido.

### Exercícios práticos da Aula 03

A pasta [`exercicios-praticos-aula-03`](./exercicios-praticos-aula-03/) contém a resolução dos 6 exercícios propostos em laboratório:

1. **Juros compostos com `for` e `while`** (`exercicio_01_for.py` / `exercicio_01_while.py`) — cálculo do valor resgatado após N anos de investimento com 1% de juros ao mês, implementado nas duas abordagens para comparação.
2. **`exercicio_02.py`** — impressão dos números de 1 a 20, primeiro um por linha e depois lado a lado (uso do parâmetro `end` do `print`).
3. **`exercicio_03.py`** — leitura de 5 números e identificação do maior, usando a função `max()`.
4. **`exercicio_04.py`** — leitura de dois números inteiros e impressão de todo o intervalo entre eles.
5. **`exercicio_05.py`** — cálculo do número médio de alunos por turma, com validação (`while`) garantindo que nenhuma turma tenha mais de 40 alunos.
6. **`exercicio_06.py`** — cadastro de usuário e senha, impedindo que a senha seja igual ao nome de usuário (repete a solicitação em caso de erro).

### Lista de Exercícios 03

A pasta [`lista-exercicios-03`](./lista-exercicios-03/) contém a resolução de 4 exercícios:

1. **Soma e média de 5 números**, resolvido com `for` (`exercicio_01_for.py`) e com `while` (`exercicio_01_while.py`).
2. **`exercicio_02.py`** — leitura da idade de N pessoas de uma turma, cálculo da média e classificação da turma como "jovem" (0–25), "adulta" (26–60) ou "idosa" (acima de 60).
3. **`exercicio_03_tabuada.py`** — gerador de tabuada para um número entre 1 e 10, informado pelo usuário. Esta solução vai além do conteúdo estritamente visto em aula até este ponto: encapsula a lógica em uma função (`def gerar_tabuada()`), usa `try/except` para tratar entradas inválidas (não numéricas) e o padrão `if __name__ == "__main__":`.
4. **`exercicio_04_quadrado.py`** — impressão de um quadrado de asteriscos (`*`) de tamanho configurável (1 a 20), também estruturado como função com validação via `try/except`.

## Como executar

```bash
python3 desafio-03-validacao-dados/desafio_03.py
python3 exercicios-praticos-aula-03/exercicio_01_for.py
python3 lista-exercicios-03/exercicio_03_tabuada.py
```

## Referência

Material teórico baseado no slide "AEDS - Aula 3", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
