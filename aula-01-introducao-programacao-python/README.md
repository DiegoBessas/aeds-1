# Aula 01 — Introdução à Programação e Python

## Contexto

Primeira aula da disciplina de Algoritmos e Estruturas de Dados I, com foco na introdução aos conceitos fundamentais de lógica de programação e na apresentação da linguagem Python como ferramenta de ensino.

## Conceitos teóricos abordados

- **Algoritmo:** conjunto de regras e procedimentos lógicos, bem definidos, que levam à solução de um problema em um número finito de etapas.
- **Código-fonte, compilador e interpretador:**
  - *Compilador*: traduz todo o código-fonte para código de máquina antes da execução, gerando um executável independente (ex.: GCC, javac).
  - *Interpretador*: executa o código-fonte diretamente, linha por linha, sem uma fase prévia de compilação (ex.: Python/CPython, JavaScript, Ruby).
  - A aula trouxe uma comparação direta entre os dois quanto a processo de execução, geração de executável, desempenho, depuração e portabilidade.
- **Depuração (debugging):** processo de localizar e corrigir erros (bugs) no código-fonte.
- **A linguagem Python:** criada por Guido van Rossum em 1991, é apresentada como uma linguagem popular, versátil e de fácil aprendizado, aplicável a desenvolvimento web, Data Science, Machine Learning, IA e automação de processos.
- **Variáveis:**
  - Nome simbólico associado a uma posição de memória do computador.
  - Regras de nomenclatura: podem conter letras (a-z, A-Z), números (0-9) e underscore (_); devem começar com letra ou underscore (nunca com número); são *case sensitive*.
  - Exemplos válidos: `name_1`, `_database_connection`. Exemplos inválidos: `1tomany`, `my-number`, `my number`.
- **Tipos de dados básicos em Python:**
  - `string` — sequência de caracteres entre aspas (ex.: `nome = 'Marcus'`)
  - `boolean` — verdadeiro ou falso (ex.: `aprovado = True`)
  - `int` — valor inteiro (ex.: `idade = 34`)
  - `float` — valor com casas decimais (ex.: `nota = 9.8`)
  - Uso da função `type()` para identificar o tipo de uma variável, e de funções como `int()` para conversão entre tipos.
- **Entrada e saída de dados:** uso das funções `print()` (exibição de dados na tela) e `input()` (leitura de dados informados pelo usuário).

## Atividades práticas

### Desafio 1 — Cálculo de juros compostos

**Enunciado:** uma aplicação oferece um rendimento de 1% de juros ao mês durante um ano. Qual será o valor total a ser resgatado ao final do período, se for investido R$ 100,00, R$ 8.000,00 ou R$ 50.000,00?

A pasta [`desafio-01-juros-compostos`](./desafio-01-juros-compostos/) contém duas versões do programa, refletindo a evolução da solução:

- **`programa_a_rascunho.py`** — versão inicial, na qual o valor é lido e o juro de 1% é aplicado manualmente 12 vezes (uma para cada mês), mas sem uma instrução final de exibição do resultado.
- **`programa_b_final.py`** — versão final, idêntica em lógica à anterior, mas com a adição de um `print()` formatado (`'{:.2f}'.format(conta)`) para exibir o valor final do investimento com duas casas decimais.

> Nota: a solução aplica o juro manualmente 12 vezes em sequência (uma linha por mês), já que a aula ainda não havia introduzido estruturas de repetição — conteúdo previsto para a aula seguinte.

### Lista de Exercícios 01

A pasta [`lista-exercicios-01`](./lista-exercicios-01/) contém a resolução de 4 exercícios básicos de entrada/saída de dados e operações aritméticas:

1. Programa que lê dois números e imprime a soma.
2. Programa que lê o raio de um círculo e calcula sua área (A = π r², com π = 3,14).
3. Programa que lê o valor do salário/hora e o número de horas trabalhadas no mês, calculando o salário mensal.
4. Programa que lê 2 números inteiros e 1 número real, calculando:
   - a) o produto do dobro do primeiro com a metade do segundo;
   - b) a soma do triplo do primeiro com o terceiro;
   - c) o terceiro elevado ao cubo.

## Como executar

```bash
python3 desafio-01-juros-compostos/programa_b_final.py
python3 lista-exercicios-01/lista_exercicios_01.py
```

## Referência

Material teórico baseado no slide "AEDS - Aula 1", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
