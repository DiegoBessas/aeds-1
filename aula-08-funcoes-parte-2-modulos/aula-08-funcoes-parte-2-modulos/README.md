# Aula 08 — Funções (Parte 2) e Módulos

## Contexto

Oitava aula da disciplina, dando continuidade ao estudo de funções (formas mais avançadas de passar parâmetros) e introduzindo o conceito de módulos em Python. É a última aula antes do início da Prova 1 / trabalho prático maior.

## Conceitos teóricos abordados

- **Múltiplos parâmetros definidos:** o que acontece quando uma função espera mais argumentos do que os que são efetivamente passados na chamada (gera erro).
- **Parâmetros arbitrários (`*args`):** quando não se sabe de antemão a quantidade de argumentos, usa-se `*nome` na definição da função — os argumentos chegam como uma tupla dentro da função.
- **Parâmetros por chave/valor:** argumentos podem ser passados nomeados (`funcao(sobrenome="Santos", nome="Marcus")`), dispensando a ordem posicional.
- **Parâmetros arbitrários como dicionário (`**kwargs`):** análogo ao `*args`, mas usando `**nome` para receber um número arbitrário de argumentos nomeados como um dicionário.
- **Parâmetros com valor padrão (default):** é possível definir um valor padrão para um parâmetro, tornando seu preenchimento opcional na chamada da função.
- **Módulos:** um módulo é a implementação de uma "biblioteca" Python — um arquivo `.py` com funções (e/ou variáveis) que pode ser importado e reutilizado em outras partes da aplicação com `import nome_do_modulo`. A pasta [`exemplos-teoricos-modulos`](./exemplos-teoricos-modulos/) reproduz os exemplos de sala: `meumodulo.py`/`meuexemplo.py` (função de saudação importada de outro arquivo) e `meumodulo2.py`/`meuexemplo2.py` (uma variável do tipo dicionário definida em um módulo e acessada a partir de outro arquivo).

## Atividades práticas

A pasta [`exercicios-praticos-aula-08`](./exercicios-praticos-aula-08/) contém a resolução dos 4 exercícios propostos:

1. **`exercicio_01.py`** — função `media(*numeros)`, que aceita uma quantidade arbitrária de números e retorna sua média.
2. **`exercicio_02.py`** — função `data(dia, mes, ano, por_extenso=False)`, que exibe uma data no formato `dd/mm/aaaa` por padrão, ou por extenso (`dd de mês de aaaa`) quando o parâmetro opcional `por_extenso` é `True`.
3. **[`exercicio-03-manipulador-strings`](./exercicios-praticos-aula-08/exercicio-03-manipulador-strings/)** — primeiro exercício de criação de um módulo próprio: `manipulador_strings.py` implementa as funções `maiusculo`, `minusculo`, `frase_para_lista`, `tamanho` (conta palavras) e `contador_palavras(*palavras)`, todas testadas em `exercicio_03.py` a partir de `import manipulador_strings`.
4. **[`exercicio-04-calculadora`](./exercicios-praticos-aula-08/exercicio-04-calculadora/)** — segundo módulo próprio: `calculadora.py` implementa `soma(*nums)` e `multiplicacao(*nums)` (aceitando quantidade arbitrária de números, com validação de que ao menos 2 sejam informados), além de `subtracao(num_1, num_2)` e `divisao(num_1, num_2)` (com tratamento para divisão por zero). Testado em `exercicio_04.py`.

> Nota: os arquivos `.pyc` gerados automaticamente pelo Python ao importar os módulos (pasta `__pycache__`) não foram incluídos no repositório — são artefatos de compilação, não código-fonte.

## Contexto adicional — Trabalho Final da disciplina

O material desta aula também apresenta o enunciado do **Trabalho Final** da disciplina: um programa com aplicação no mundo real, incluindo armazenamento de dados em arquivo, uso de estruturas de dados compostas (listas, dicionários, sets etc.), um ou mais módulos próprios e ao menos 5 funções, permitindo cadastro, pesquisa e interação com os dados. Esse trabalho foi implementado como um jogo de Campo Minado e documentado em um repositório próprio: **[campo-minado-python](https://github.com/SEU-USUARIO/campo-minado-python)**.

## Como executar

```bash
python3 exercicios-praticos-aula-08/exercicio_01.py
cd exercicios-praticos-aula-08/exercicio-03-manipulador-strings && python3 exercicio_03.py
cd exercicios-praticos-aula-08/exercicio-04-calculadora && python3 exercicio_04.py
```

## Referência

Material teórico baseado no slide "AEDS - Aula 8", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
