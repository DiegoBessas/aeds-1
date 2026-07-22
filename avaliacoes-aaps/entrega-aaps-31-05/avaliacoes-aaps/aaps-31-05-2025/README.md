# AAPS — 31/05/2025 — Bibliotecas Python Mais Utilizadas Atualmente

## Contexto

Avaliação prática aplicada próximo ao fim do semestre, com um formato diferente das demais: o material de referência ([`bibliotecas-python-mais-utilizadas.pdf`](./bibliotecas-python-mais-utilizadas.pdf)) apresenta 10 bibliotecas populares do ecossistema Python — cada uma com uma breve explicação e um trecho de código de exemplo — cobrindo computação numérica, ciência de dados, machine learning/deep learning e desenvolvimento web.

**Enunciado da atividade:** "Com base em cada item anterior, faça uma pesquisa e crie um código simples, mas funcional para cada item."

Bibliotecas apresentadas: **NumPy**, **Pandas**, **Matplotlib**, **Scikit-Learn**, **TensorFlow**, **Keras**, **Flask**, **Django**, **Requests** e **FastAPI**.

## Exemplos desenvolvidos

Cada exemplo foi construído de forma independente do trecho de código do PDF de referência (mesma biblioteca, casos de uso diferentes):

1. **[`01_numpy.py`](./01_numpy.py)** — estatísticas de notas de uma turma (média, desvio padrão, maior/menor nota) e filtragem de array por condição booleana (alunos aprovados).
2. **[`02_pandas.py`](./02_pandas.py)** — `DataFrame` de produtos de uma loja, com filtragem por categoria e cálculo de preço médio agrupado (`groupby`).
3. **[`03_matplotlib.py`](./03_matplotlib.py)** — gráfico de barras comparando quantidade de alunos aprovados x reprovados, salvo em arquivo `.png` com `plt.savefig(...)`.
4. **[`04_scikit_learn.py`](./04_scikit_learn.py)** — classificador KNN (`KNeighborsClassifier`) treinado no dataset embutido de vinhos (`load_wine`), com cálculo de acurácia via `accuracy_score`.
5. **[`05_tensorflow.py`](./05_tensorflow.py)** — operações com tensores: soma elemento a elemento (`tf.add`) e transposta de matriz (`tf.transpose`).
6. **[`06_keras.py`](./06_keras.py)** — rede neural sequencial com uma camada oculta a mais que o exemplo de referência, compilada com otimizador `sgd` para um problema de classificação binária.
7. **[`07_flask.py`](./07_flask.py)** — rota dinâmica (`/saudacao/<nome>`) que recebe um parâmetro pela própria URL.
8. **[`08_django/`](./08_django/)** — projeto Django completo (não apenas uma view isolada), criado via `django-admin startproject` + `python manage.py startapp`, com uma rota (`/ola/`) registrada em `projeto_django/urls.py` apontando para uma view em `meu_app/views.py`.
9. **[`09_requests.py`](./09_requests.py)** — consulta à API pública gratuita [ViaCEP](https://viacep.com.br/) a partir de um CEP, com tratamento de erro via `try/except`.
10. **[`10_fastapi.py`](./10_fastapi.py)** — rota assíncrona (`/piloto/{nome}`) que recebe um parâmetro e retorna um JSON automático.
    > **Observação:** o comentário do arquivo indica rodar com `uvicorn 10_fastapi:app --reload`; como o arquivo se chama `10_fastapi.py`, o nome do módulo para o Uvicorn precisa ser informado sem o `.py` — nomes de módulo Python não podem começar com dígito, então, rigorosamente, o comando correto seria referenciar o arquivo entre aspas ou renomeá-lo (ex.: `fastapi_app.py`). Mantive o arquivo com o nome original.

Também está incluída uma captura de tela ([`captura-tela-execucao.png`](./captura-tela-execucao.png)) registrando a execução de um dos exemplos.

## Como executar

```bash
# Exemplos simples (rodam diretamente)
python3 01_numpy.py
python3 02_pandas.py
python3 03_matplotlib.py
python3 04_scikit_learn.py
python3 05_tensorflow.py
python3 06_keras.py

# Flask (servidor web local)
python3 07_flask.py
# Acesse: http://127.0.0.1:5000/saudacao/SeuNome

# Django (projeto completo)
cd 08_django
python manage.py runserver
# Acesse: http://127.0.0.1:8000/ola/

# Requests
python3 09_requests.py

# FastAPI (servidor web local, com documentação automática)
uvicorn "10_fastapi:app" --reload
# Acesse: http://127.0.0.1:8000/docs
```

## Dependências

```bash
pip install numpy pandas matplotlib scikit-learn tensorflow flask django requests fastapi uvicorn
```

> Nota: o arquivo `db.sqlite3` (banco de dados gerado automaticamente pelo Django) e a pasta `__pycache__` não foram incluídos no repositório — são gerados automaticamente na primeira execução (`python manage.py migrate`) e não fazem parte do código-fonte.

## Referência

Enunciado: "AAPS 31/05/2025 — Bibliotecas Python Mais Utilizadas Atualmente", FANS, 31/05/2025.
