# Aula 14 — Revisão Final

## Contexto

Décima quarta e última aula da disciplina, dedicada a uma revisão geral de todo o conteúdo do semestre (variáveis e tipos de dados, estruturas de decisão, estruturas de repetição, listas/tuplas/sets/dicionários, funções, módulos e manipulação de arquivos), encerrando com um **Desafio Final** avaliativo.

## Resumo da revisão

A aula percorreu, em alto nível, os grandes temas trabalhados ao longo do curso — para o detalhamento completo de cada um, ver as aulas correspondentes já documentadas neste repositório: variáveis e tipos ([Aula 01](../aula-01-introducao-programacao-python/)), estruturas de decisão ([Aula 02](../aula-02-operadores-estruturas-decisao/)), estruturas de repetição ([Aula 03](../aula-03-funcoes-uteis-estruturas-repeticao/)), listas/tuplas/matrizes ([Aula 05](../aula-05-listas-tuplas-matrizes/)), sets/dicionários ([Aula 06](../aula-06-sets-dicionarios/)), funções ([Aula 07](../aula-07-funcoes-parte-1/) e [Aula 08](../aula-08-funcoes-parte-2-modulos/)), módulos ([Aula 08](../aula-08-funcoes-parte-2-modulos/) e [Aula 10](../aula-10-modulos/)) e manipulação de arquivos ([Aula 09](../aula-09-manipulacao-arquivos-debug/)).

## Desafio Final

**Enunciado:** implementar, em um módulo chamado `conversor_tipos`, uma função `lista_para_dicionario` que recebe uma lista de listas de alunos (matrícula, nome, notas das 3 etapas e nota total) e retorna um dicionário de dicionários, indexado pela matrícula. A partir dessa conversão, o desafio pede três operações, cada uma percorrendo o dicionário resultante com um `for`:

- **a)** exibir o nome e a nota total de cada aluno;
- **b)** exibir apenas os alunos com nota total maior que 60;
- **c)** exibir o nome e a matrícula de cada aluno.

O professor dividiu esse desafio em duas questões avaliadas separadamente (14 e 15), reunidas na pasta [`desafio-final`](./desafio-final/):

- **[`questao-14-conversao-lista-dicionario`](./desafio-final/questao-14-conversao-lista-dicionario/)** — implementa apenas a conversão da lista de listas para o dicionário de dicionários (`main.py` + módulo com a função `lista_para_dicionario`).
- **[`questao-15-operacoes-dicionario-alunos`](./desafio-final/questao-15-operacoes-dicionario-alunos/)** — reaproveita a mesma função de conversão e adiciona as três operações (a, b, c) pedidas no restante do enunciado.

> **Observação:** o enunciado pede que o módulo se chame `conversor_tipos`; nos arquivos enviados, os módulos foram nomeados `questao_14_modulo.py` e `questao_15_modulo.py` (mantive esses nomes no repositório, já que os arquivos `main.py` de cada questão importam exatamente por esse nome). Testei os dois programas e ambos produzem a saída esperada para os três alunos de exemplo do enunciado (marcus, joao e camila).

## Como executar

```bash
cd desafio-final/questao-14-conversao-lista-dicionario
python3 main.py

cd ../questao-15-operacoes-dicionario-alunos
python3 main.py
```

## Referência

Material teórico baseado no slide "AEDS - Aula 14" (revisão geral e Desafio Final), do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
