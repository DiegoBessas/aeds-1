# Algoritmos e Estruturas de Dados I

Repositório com os exercícios, desafios e programas desenvolvidos durante a disciplina de **Algoritmos e Estruturas de Dados I**, cursada no **1º período** do curso de **Engenharia de Software** na **Faculdade de Nova Serrana (FANS)**, no 1º semestre de 2025.

## Sobre a disciplina

- **Carga horária:** 80 horas
- **Professor:** Bruno Fernando Lacerda de Oliveira
- **Objetivo da disciplina (segundo o plano de ensino):** apresentar as fases do desenvolvimento de programas em uma linguagem de alto nível — dados, comandos e metodologias de desenvolvimento — utilizando Python como linguagem de ensino.

### Ementa

- Introdução à lógica de programação: conceitos fundamentais para o desenvolvimento lógico de programas estruturados
- Conceitos básicos para construção de algoritmos (estratégias de solução, representação e documentação)
- Compiladores e interpretadores
- Estruturação de programas: nomes, variáveis, constantes, tipos de dados
- Operadores matemáticos, relacionais e lógicos; blocos de execução
- Estruturas de decisão e de repetição
- Estruturas de dados compostas homogêneas: vetores e matrizes
- Cadeias de caracteres
- Ambientes de programação e transcrição de algoritmos
- Depuração de programas

### Bibliografia indicada pelo professor

- BACKES, André R. *Algoritmos e Estruturas de Dados em Linguagem C*. Grupo GEN, 2023.
- JR., Dilermando. *Algoritmos e Programação de Computadores*. Grupo GEN, 2019.
- SOUZA, Marco A. Furlan de; GOMES, Marcelo M.; SOARES, Marcio V.; CONCILIO, Ricardo. *Algoritmos e lógica de programação: um texto introdutório para a engenharia*. Cengage Learning Brasil, 2019.

## Tecnologias

- **Python 3**
- **Tkinter** (interfaces gráficas, a partir da Aula 11)
- **Pandas** (manipulação de dados/planilhas, a partir da Aula 11)
- **Streamlit** (aplicações web de dados, a partir da Aula 13)

## Estrutura do repositório

Cada pasta representa uma aula da disciplina, contendo os exercícios e desafios propostos, junto com um README explicando o conteúdo teórico abordado e os enunciados das atividades.

| Aula | Tema | Conteúdo |
|---|---|---|
| [Aula 01](./aula-01-introducao-programacao-python/) | Introdução à Programação e Python | Conceitos de algoritmo, variáveis, tipos de dados, Desafio 1 (juros compostos) e Lista de Exercícios 1 |
| [Aula 02](./aula-02-operadores-estruturas-decisao/) | Operadores Matemáticos, Relacionais, Lógicos e Estruturas de Decisão | Operadores e estruturas `if/elif/else`, Desafio 2 (dia da semana), exercícios práticos de laboratório e Lista de Exercícios 2 |
| [Aula 03](./aula-03-funcoes-uteis-estruturas-repeticao/) | Funções Úteis e Estruturas de Repetição | Funções nativas (`range`, `len`, `round`, etc.), estruturas `for`/`while`, Desafio 3 (validação de dados), exercícios práticos e Lista de Exercícios 3 |
| [Aula 04](./aula-04-cadeias-caracteres-strings/) | Cadeias de Caracteres, Formatação e Operações com Strings | Operações e formatação de strings, `for` com strings, Desafio 4 (validador de CPF), exercícios práticos e Lista de Exercícios 4 |
| [Aula 05](./aula-05-listas-tuplas-matrizes/) | Listas, Tuplas e Matrizes | Listas, tuplas, matrizes (listas de listas), exercícios práticos e Desafio 5 (Jogo da Velha) |
| [Aula 06](./aula-06-sets-dicionarios/) | Sets e Dicionários | Sets, dicionários, dicionários de dicionários, exercícios práticos e Desafio 6 (cadastro de turma) |
| [Aula 07](./aula-07-funcoes-parte-1/) | Funções (Parte 1) | Definição de funções, parâmetros, retorno, escopo de variáveis; evolução incremental do Jogo da Velha em 5 exercícios |
| [Aula 08](./aula-08-funcoes-parte-2-modulos/) | Funções (Parte 2) e Módulos | Parâmetros arbitrários (`*args`/`**kwargs`), parâmetros nomeados e default, criação de módulos próprios (`manipulador_strings`, `calculadora`) |
| [Aula 09](./aula-09-manipulacao-arquivos-debug/) | Manipulação de Arquivos e Debug Mode | Leitura/escrita/exclusão de arquivos (`open`, modos `r`/`a`/`w`/`x`, módulo `os`), depuração (breakpoints) no VSCode, exercícios de leitura de CSV |
| [Aula 10](./aula-10-modulos/) | Módulos | Módulos da biblioteca padrão (`datetime`, `math`, `json`, `re`), PIP; 4 desafios de expressões regulares (validação de e-mail, extração de datas, busca de palavras, validação de senha) |
| [Aula 11](./aula-11-tkinter-eventos-bindings-pandas/) | Tkinter, Eventos e Bindings, Pandas | Interfaces gráficas com Tkinter (widgets, layout, diálogos, eventos/bindings), Pandas (Series, DataFrame, leitura de Excel); evolução em 3 versões de um leitor de planilhas até uma aplicação de gestão de inventário |
| [Aula 12](./aula-12-pilhas-filas/) | Pilhas e Filas | Pilha (LIFO: push/pop/peek) e Fila (FIFO: enqueue/dequeue/front), ambas implementadas com menu interativo |
| [Aula 13](./aula-13-pandas-tkinter-streamlit/) | Exemplos Práticos de Pandas e Tkinter | Comparativo Tkinter (desktop) x Streamlit (web) implementando o mesmo leitor de planilhas Excel com Pandas |
| [Aula 14](./aula-14-revisao-final/) | Revisão Final | Revisão geral do conteúdo do semestre e Desafio Final avaliativo (conversão lista de listas → dicionário de dicionários) |

## Trabalho Final

O Trabalho Final da disciplina — um jogo de Campo Minado em Python, com placar persistente em arquivo — foi grande o suficiente para justificar um repositório próprio, em vez de ficar como mais uma pasta de aula aqui: **[campo-minado-python](https://github.com/DiegoBessas/campo-minado-python)**.

## Como executar os programas

Todos os programas foram escritos em Python 3 e podem ser executados diretamente via terminal:

```bash
python3 caminho/para/o/arquivo.py
```
