# Aula 04 — Cadeias de Caracteres, Formatação e Operações com Strings

## Contexto

Quarta aula da disciplina. Abre com a revisão do Desafio 3 (validação de dados cadastrais), apresentada pelo professor com uma solução baseada em `while` + `os.system('clear')` para cada campo — uma abordagem diferente da que foi usada na resolução própria do Desafio 3 (ver [Aula 03](../aula-03-funcoes-uteis-estruturas-repeticao/)). Em seguida, a aula avança para cadeias de caracteres (strings): literais, caracteres de escape, operações e formatação, fechando com uma aula prática em laboratório.

## Conceitos teóricos abordados

- **Cadeias de caracteres (strings):** operações aritméticas com strings (concatenação), uso de aspas simples ou duplas, caracteres de escape, strings multilinha e outros caracteres de escape especiais.
- **Operações com strings:** conversão para minúsculo/maiúsculo, obtenção do tamanho (`len`), conversão para inteiro/decimal, verificação de prefixo/sufixo (`startswith`/`endswith`), substituição de trechos (`replace`), divisão em substrings (`split`) e acesso a trechos por *slicing*.
- **Encadeamento de operações:** a aula demonstrou como mesclar várias operações de string em uma única expressão encadeada — ver [`exemplos-teoricos-strings/encadeamento_metodos_string.py`](./exemplos-teoricos-strings/encadeamento_metodos_string.py), que reproduz o exemplo de sala (substituir ocorrências de "o" por "a", converter para minúsculo, remover "!" e extrair a segunda palavra do texto, tudo em uma única linha encadeada).
- **`for` com strings:** o comando `for` permite percorrer, um a um, todos os caracteres de uma string.
- **Formatação de strings:** uso de f-strings para compor mensagens combinando texto fixo e variáveis.

## Atividades práticas

### Desafio 4 — Validador de CPF

**Enunciado:** solicitar a digitação de um CPF no formato `xxx.xxx.xxx-xx` e indicar se é válido ou inválido, validando tanto os caracteres de formatação quanto os dígitos verificadores.

A pasta [`desafio-04-validador-cpf`](./desafio-04-validador-cpf/) reúne duas versões:

- **`desafio_04_rascunho_debug.py`** — versão de rascunho, associada a uma "aula de debug": valida apenas o formato (uso de `.split()` para separar as partes do CPF pelos pontos e o traço, checando o tamanho e se cada parte é numérica), sem checar os dígitos verificadores. Contém uma mensagem de erro com um `{}` de interpolação que não é efetivamente formatada, por faltar o prefixo `f` na string (ex.: `"CPF Invalido! {parte_um}"` ao invés de `f"CPF Invalido! {parte_um}"`) — mantive esse detalhe como está no material original, já que parece fazer parte do próprio exercício de identificar e corrigir erros ("aula de debug").
- **`desafio_04_final.py`** — versão final e mais completa: usa expressão regular (`re.match`) para validar o formato, remove a formatação, descarta CPFs com todos os dígitos iguais e calcula de fato os dois dígitos verificadores segundo o algoritmo oficial do CPF, comparando com os dígitos informados.

### Exercícios práticos da Aula 04

A pasta [`exercicios-praticos-aula-04`](./exercicios-praticos-aula-04/) contém a resolução dos 6 exercícios propostos:

1. **`exercicio_01.py`** — lê o nome do usuário e o imprime na vertical (um caractere por linha) e em maiúsculo.
2. **`exercicio_02.py`** — variação do anterior, imprimindo o nome em "formato de escada" (cada linha mostra um prefixo maior da string).
3. **`exercicio_03.py`** — lê uma data de nascimento (`dd/mm/aaaa`) e exibe o nome do mês por extenso.
4. **`exercicio_04.py`** — converte um número de 0 a 99 para sua forma por extenso.
5. **`exercicio_05.py`** — verifica se uma sequência de caracteres informada é um palíndromo (ignorando espaços e diferenças de maiúsculas/minúsculas).
6. **`exercicio_06.py`** — conta a quantidade de espaços em branco e de vogais em uma frase informada.

### Lista de Exercícios 04

A pasta [`lista-exercicios-04`](./lista-exercicios-04/) contém a resolução de 4 exercícios:

1. **`exercicio_01.py`** — lê o nome do usuário e o exibe invertido e em maiúsculo.
2. **`exercicio_02.py`** — lê um número de telefone (com ou sem traço) e adiciona o dígito "9" na frente quando o número tiver apenas 8 dígitos.
3. **`exercicio_03.py`** — lê uma frase e uma letra, e conta quantas vezes a letra aparece na frase.
4. **`exercicio_04.py`** — conta caracteres alfabéticos em um texto.
   > **Observação:** o enunciado original pede a contagem do número de **palavras** do texto; a implementação atual conta o número de **letras** (caracteres para os quais `isalpha()` é verdadeiro), o que produz um resultado diferente do solicitado.

## Como executar

```bash
python3 desafio-04-validador-cpf/desafio_04_final.py
python3 exercicios-praticos-aula-04/exercicio_05.py
python3 lista-exercicios-04/exercicio_02.py
```

## Referência

Material teórico baseado no slide "AEDS - Aula 4", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
