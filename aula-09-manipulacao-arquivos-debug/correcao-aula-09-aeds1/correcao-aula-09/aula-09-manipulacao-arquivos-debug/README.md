# Aula 09 — Manipulação de Arquivos e Debug Mode

## Contexto

Nona aula da disciplina, dividida em dois blocos: manipulação de arquivos (leitura, escrita e exclusão de arquivos e diretórios) e uma introdução ao processo de depuração (*debugging*) usando os recursos do VSCode.

## Conceitos teóricos abordados

- **Memória RAM:** revisão do conceito de memória volátil, de acesso rápido e temporário, em contraste com o armazenamento em disco (não volátil).
- **Manipulação de arquivos com `open()`:**
  - Modos de acesso: `"r"` (leitura, padrão), `"a"` (escrita ao final do arquivo, sem apagar o conteúdo existente), `"w"` (escrita, sobrescrevendo o conteúdo desde o início) e `"x"` (criação de um novo arquivo — gera erro se o arquivo já existir).
  - Leitura: `.read()` (lê todo o conteúdo, ou uma quantidade específica de caracteres, ex.: `.read(5)`), `.readline()` (lê uma linha) e uso do `for` para iterar linha a linha sobre um arquivo aberto, combinado com `.rstrip("\n")` para remover a quebra de linha final de cada uma.
  - `arquivo.close()` — fecha o arquivo após o uso.
  - **Exclusão de arquivos e diretórios:** `os.remove("arquivo.txt")` (usando o módulo `os`), com verificação prévia via `os.path.exists(...)` para evitar erro caso o arquivo não exista; `os.rmdir("pasta")` para excluir um diretório.
- **Debugging:** o processo de encontrar e corrigir *bugs* (erros de programação), estruturado em três passos — definir pontos de parada (*breakpoints*) na execução do código, executar o código e interagir com ele enquanto estiver em execução (inspecionar variáveis, avançar passo a passo). A aula demonstrou o uso do depurador integrado ao VSCode.

## Atividades práticas

Os dois exercícios usam o mesmo arquivo de dados, [`arquivo1.csv`](./arquivo1.csv), contendo o nome e a nota de 8 alunos (fornecido pelo professor como se fosse a exportação de uma planilha).

> **Observação sobre os caminhos de arquivo:** o material original lia o CSV a partir de um caminho absoluto do computador de origem. Para que o código funcione em qualquer máquina que clonar o repositório, o caminho foi ajustado para relativo (`open("../arquivo1.csv", "r")`), já que o CSV está um nível acima, na raiz da pasta desta aula. Os scripts devem ser executados a partir de dentro da própria pasta do exercício (ver "Como executar" abaixo).

### Exercício 1 — Estatísticas das notas

**Enunciado:** ler o arquivo com as notas dos alunos e calcular a média da turma, o aluno com a maior nota (e sua nota) e o aluno com a menor nota (e sua nota).

Ver [`exercicio-01-notas-alunos/exercicio_01.py`](./exercicio-01-notas-alunos/exercicio_01.py).

### Exercício 2 — Busca de nota por nome de aluno

**Enunciado:** alterar o programa do Exercício 1 para permitir também a busca da nota de um aluno específico pelo nome, informando se ele foi encontrado ou não.

A pasta [`exercicio-02-busca-aluno`](./exercicio-02-busca-aluno/) contém duas versões da solução:

- **`exercicio_02_lista.py`** — mantém a mesma estrutura de dados do Exercício 1 (lista de listas `[aluno, nota]`) e adiciona uma busca linear em loop (`while True`), pedindo o nome do aluno até que o usuário digite `"sair"`.
- **`exercicio_02_dicionario_menu.py`** — versão alternativa (mais alinhada ao gabarito oficial da aula), que troca a lista por um dicionário (`{aluno: nota}`) para busca direta por chave, e organiza a interação como um menu numerado (`1 - Pesquisar Nota de Aluno`, `2 - Sair`) em vez de um comando de texto livre.

## Como executar

```bash
cd aula-09-manipulacao-arquivos-debug/exercicio-01-notas-alunos
python3 exercicio_01.py

cd ../exercicio-02-busca-aluno
python3 exercicio_02_dicionario_menu.py
```

> Importante: os scripts precisam ser executados a partir de dentro da própria pasta do exercício (`exercicio-01-notas-alunos` ou `exercicio-02-busca-aluno`), já que o caminho até o CSV é relativo a cada uma dessas pastas.

## Referência

Material teórico baseado no slide "AEDS - Aula 9" e no gabarito "Exercícios resolvidos da Aula 9", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
