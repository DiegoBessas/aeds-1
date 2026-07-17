# Aula 02 — Operadores Matemáticos, Relacionais, Lógicos e Estruturas de Decisão

## Contexto

Segunda aula da disciplina, dividida entre uma revisão do Desafio 1 (juros compostos), a introdução teórica a operadores e estruturas de decisão, e uma aula prática em laboratório voltada à instalação do Python/VSCode e à resolução de exercícios.

## Conceitos teóricos abordados

- **Operadores matemáticos:** `+` (soma), `-` (subtração), `*` (multiplicação), `/` (divisão), `%` (resto da divisão). Discussão sobre conversão implícita de tipos (int → float) quando uma expressão combina operandos inteiros e decimais, e sobre a ordem de prioridade das operações (parênteses → multiplicação/divisão/resto → soma/subtração).
- **Operadores relacionais:** `>`, `<`, `>=`, `<=`, `==`, `!=`, usados para comparar expressões e produzir um valor lógico (verdadeiro/falso).
- **Operadores lógicos:** `and` (conjunção), `or` (disjunção), `not` (negação), usados para combinar múltiplas condições em uma única expressão.
- **Estruturas de decisão (`if` / `elif` / `else`):** conceito de processamento condicional, no qual o programa executa (ou deixa de executar) um bloco de instruções com base no valor lógico de uma condição. A aula trabalhou o comando `IF` simples e o `IF-ELSE` com múltiplas ramificações (`elif`).
- **Ambiente de desenvolvimento:** instalação do Python (Windows/Mac/Linux) e apresentação do VSCode como IDE (Integrated Development Environment), com suporte a depuração, Git integrado, realce de sintaxe e autocompletar.

## Atividades práticas

### Desafio 2 — Dia da semana

**Enunciado:** programa que lê um número (1 a 7) e exibe o dia da semana correspondente (1-Domingo, 2-Segunda, etc.); caso o valor informado esteja fora dessa faixa, deve exibir "Valor inválido!".

Ver [`desafio-02-dia-semana/desafio_02.py`](./desafio-02-dia-semana/desafio_02.py) — implementado com uma cadeia de `if/elif/else`.

### Exercícios práticos da Aula 02

Bateria de 9 exercícios feitos em laboratório, cobrindo desde a exibição de texto simples até estruturas de decisão mais elaboradas: saudação com nome, média de três números, cálculo de juros compostos (3 meses), verificação de maioridade, conversão Fahrenheit → Celsius, maior entre três números, par/ímpar e número de dias do mês.

Ver [`exercicios-praticos-aula-02/exercicios_praticos_aula_02.py`](./exercicios-praticos-aula-02/exercicios_praticos_aula_02.py).

### Exercício avulso — Média de cinco notas

Exercício adicional (fora da lista numerada oficial) que lê 5 notas, calcula a média e classifica o aluno como "Reprovado" (média < 7), "Aprovado" (7 ≤ média < 10) ou "Aprovado com Distinção" (média = 10).

Ver [`exercicio-avulso-media-notas/exercicio_media_cinco_notas.py`](./exercicio-avulso-media-notas/exercicio_media_cinco_notas.py).

### Lista de Exercícios 02

A pasta [`lista-exercicios-02`](./lista-exercicios-02/) contém a resolução de 4 exercícios:

1. Verificar se uma letra digitada é vogal ou consoante (com bônus para maiúsculas/minúsculas).
2. Ler duas notas parciais, calcular a média e classificar como "Aprovado", "Reprovado" ou "Aprovado com Distinção".
3. Calcular o reajuste salarial de um colaborador conforme faixas de salário (20%, 15%, 10% ou 5% de aumento), exibindo salário antes do reajuste, percentual aplicado, valor do aumento e novo salário.
   > **Observação:** na implementação atual, o valor do aumento (`aumento`) é informado diretamente pelo usuário como entrada, e o percentual exibido conforme a faixa salarial é apenas informativo — ele não é usado para calcular `salario_novo` automaticamente a partir do percentual.
4. Ler dois números e uma operação (soma, subtração, multiplicação ou divisão) e informar se o resultado é par/ímpar, positivo/negativo e inteiro/decimal.
   > **Observação:** a variável `num` recebe, em sequência, os quatro resultados (`soma`, `sub`, `multi`, `div`), então as classificações finais (par/ímpar, sinal, inteiro/decimal) são sempre calculadas sobre o resultado da divisão (`div`), independentemente da operação escolhida pelo usuário.

## Como executar

```bash
python3 desafio-02-dia-semana/desafio_02.py
python3 exercicios-praticos-aula-02/exercicios_praticos_aula_02.py
python3 exercicio-avulso-media-notas/exercicio_media_cinco_notas.py
python3 lista-exercicios-02/lista_exercicios_02.py
```

## Referência

Material teórico baseado no slide "AEDS - Aula 2", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
