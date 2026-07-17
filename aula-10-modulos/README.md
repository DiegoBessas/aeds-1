# Aula 10 — Módulos

## Contexto

Décima aula da disciplina, dedicada a apresentar módulos prontos da biblioteca padrão do Python (e do ecossistema PyPI) que resolvem problemas comuns sem a necessidade de implementar tudo do zero. É a última aula teórica antes do início do desenvolvimento do Trabalho Final da disciplina.

## Conceitos teóricos abordados

- **Módulos da biblioteca padrão:** Python já vem com um conjunto de módulos pré-definidos para tarefas comuns (a aula cita `system` e `random` como exemplos adicionais), com a documentação completa disponível no [Python Module Index](https://docs.python.org/3/py-modindex.html).
- **`datetime`:** obtenção da data/hora atual (`datetime.datetime.now()`), definição de uma data específica (`datetime.datetime(2024, 6, 26)`, com acesso a `.year`, `.month`, `.day`) e formatação de datas com `.strftime(...)` (ex.: `"%d de %B de %Y"`).
- **Funções matemáticas embutidas:** `min()`, `max()`, `abs()`, `pow()`.
- **Módulo `math`:** `math.sqrt()` (raiz quadrada), `math.ceil()` (arredondamento para cima), `math.floor()` (arredondamento para baixo), `math.pi`.
- **Módulo `json`:** conversão entre string JSON e dicionário Python nos dois sentidos — `json.loads(...)` (string → dicionário) e `json.dumps(...)` (dicionário → string).
- **Módulo `re` (expressões regulares — RegEx):** uso de `re.match(...)` para verificar se uma string corresponde a um padrão (ex.: validar se um CPF contém apenas números, ou se uma string começa com uma letra específica).
- **PIP:** o gerenciador de módulos do Python, usado para instalar bibliotecas externas da comunidade (`pip install nome_do_modulo`), com exemplos usando os pacotes `camelcase` e `keyboard`, disponíveis no [PyPI](https://pypi.org/).

## Atividades práticas — Desafios Python + RegEx

Diferente das aulas anteriores, esta aula trouxe uma lista de **4 desafios focados especificamente no módulo `re`** (expressões regulares), reunidos no PDF "Desafios Python + Regex". Todas as soluções estão na pasta [`desafios-python-regex`](./desafios-python-regex/), cada uma implementada como uma função testável isoladamente:

1. **`desafio_01_validacao_email.py`** — `validar_email(email)`: verifica se uma string é um e-mail válido no formato `nome@dominio.extensao`, em que o nome pode conter letras, números, `.`, `-` e `_`, e o domínio apenas letras, números e hífens.
2. **`desafio_02_extracao_datas.py`** — `extrair_datas(texto)`: extrai todas as datas no formato `DD/MM/AAAA` de um texto, validando os intervalos de dia (01–31), mês (01–12) e ano (1900–2099) diretamente na expressão regular.
3. **`desafio_03_palavras_cao.py`** — `buscar_palavras(texto)`: encontra todas as palavras terminadas em "ção" em um texto, ignorando diferenças entre maiúsculas e minúsculas (`re.IGNORECASE`).
4. **`desafio_04_validacao_senha.py`** — `validar_senha(senha)`: verifica se uma senha é forte, exigindo ao menos 8 caracteres, uma letra maiúscula, uma minúscula, um número e um caractere especial (`@#$%^&*`).

Todas as soluções foram testadas com os exemplos fornecidos no próprio enunciado e retornaram os resultados esperados.

## Como executar

```bash
cd aula-10-modulos/desafios-python-regex
python3 desafio_01_validacao_email.py
python3 desafio_02_extracao_datas.py
python3 desafio_03_palavras_cao.py
python3 desafio_04_validacao_senha.py
```

## Referência

Material teórico baseado no slide "AEDS - Aula 10" e no PDF "Desafios Python + Regex", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
