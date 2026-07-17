# Aula 06 — Sets e Dicionários

## Contexto

Sexta aula da disciplina, encerrando o bloco de tipos de dados compostos (collections) do Python com sets e dicionários (o bloco havia começado na [Aula 05](../aula-05-listas-tuplas-matrizes/) com listas, tuplas e matrizes).

## Conceitos teóricos abordados

- **Sets:** armazenam múltiplos itens em uma única variável, **sem permitir valores duplicados** e **sem manter uma ordem definida**; não permitem alteração de seus elementos individuais após a criação (embora seja possível adicionar/remover itens do conjunto como um todo). Observação apresentada em aula: `True` e `1` são tratados como o mesmo valor dentro de um set.
  - Criação: literal `{...}` ou `set((...))`.
  - Funções e métodos: `len()`, `type()`, uso em `for` e `in`, `add()`, `update()` (para unir com outro conjunto), `remove()` (gera erro se o item não existir), `discard()` (não gera erro), `pop()` (remove um elemento aleatório), `clear()`, `copy()`.
- **Dicionários (dictionaries):** estruturas do tipo `chave: valor`, que mantêm ordem definida e não permitem chaves duplicadas (se uma chave for redefinida, o valor mais recente prevalece).
  - Acesso por chave (`dict["chave"]` ou `dict.get("chave")`).
  - Funções e métodos: `len()`, `type()`, `.keys()`, `.values()`, `.items()`, atualização de valores por atribuição direta ou `.update()`, remoção com `.pop()`, `.clear()` ou `.popitem()` (remove o último item inserido), cópia com `.copy()` ou `dict(...)`.
  - Iteração com `for` sobre as chaves, valores ou pares chave-valor (`.items()`), e verificação de existência de chave com `in`.
  - **Dicionários de dicionários:** uma estrutura em que cada chave do dicionário externo aponta para outro dicionário (ex.: `turma["Deivid"]["nota"]`), usada como base para o Desafio 6.
- **Comparação entre collections:** listas (ordenadas, mutáveis, com duplicados), tuplas (ordenadas, imutáveis, com duplicados), sets (não ordenados, não indexados, sem duplicados) e dicionários (ordenados, mutáveis, sem chaves duplicadas).

## Atividades práticas

### Exercícios práticos da Aula 06

A pasta [`exercicios-praticos-aula-06`](./exercicios-praticos-aula-06/) contém a resolução dos 5 exercícios propostos:

1. **Enunciado:** dada uma lista de números, identificar **quantos números únicos** existem nela (ex.: `[10, 2, 2, 10, 11, 5, 5, 5, 6, 8, 4, 10]` → resultado `7`).
2. **Enunciado:** dada uma lista de números, informar **se pelo menos um número se repete** (resultado booleano).
   > **Observação:** os arquivos `exercicio_01.py` e `exercicio_02.py` contêm exatamente o mesmo código — uma implementação que resolve o Exercício 2 (retorna `True`/`False` comparando o tamanho da lista com o tamanho do set gerado a partir dela). O Exercício 1, que pede a **contagem** de números únicos (não um booleano), não possui uma implementação própria no material enviado.
3. **`exercicio_03.py`** — gera um dicionário com os números inteiros de 1 a N como chaves e seus respectivos quadrados como valores, usando dict comprehension (`{i: i**2 for i in range(1, N + 1)}`).
4. **`exercicio_04.py`** — a partir do mesmo tipo de dicionário (quadrados de 1 a 50), consulta e exibe o quadrado de valores específicos (5, 15, 28, 36 e 47).
5. **`exercicio_05.py`** — cadastro de estoque de uma agência de carros seminovos: para cada carro, armazena marca, modelo, ano, quilometragem e preço de venda em um dicionário, adicionando cada um a uma lista; ao final, exibe todos os carros cadastrados.

### Desafio 6 — Cadastro de turma com dicionário de dicionários

**Enunciado:** refazer o exercício de cadastro de alunos da aula anterior (que usava uma lista de tuplas — ver [Aula 05](../aula-05-listas-tuplas-matrizes/)), agora utilizando uma estrutura de **dicionário de dicionários**, em que a chave de cada aluno é sua matrícula.

Ver [`desafio-06-turma-dicionario/desafio_06.py`](./desafio-06-turma-dicionario/desafio_06.py) — para cada aluno cadastrado, a matrícula (informada pelo usuário) é usada como chave de um dicionário externo `turma`, cujo valor é outro dicionário contendo nome e as três notas de etapa, além da nota total calculada.

## Como executar

```bash
python3 exercicios-praticos-aula-06/exercicio_03.py
python3 desafio-06-turma-dicionario/desafio_06.py
```

## Referência

Material teórico baseado no slide "AEDS - Aula 6", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
