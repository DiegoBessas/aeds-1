# Aula 13 — Exemplos Práticos de Pandas e Tkinter (e Streamlit)

## Contexto

Décima terceira aula da disciplina, estruturada como uma explicação linha a linha (método a método) de dois programas que resolvem exatamente o **mesmo problema** — um leitor de planilhas Excel com Pandas — usando duas abordagens de interface diferentes: **Tkinter** (aplicação desktop) e **Streamlit** (aplicação web). O objetivo da aula é comparar diretamente os dois paradigmas para o mesmo caso de uso.

> Nota: o material desta aula veio em dois PDFs próprios (`Pandas_TK.pdf` e `Pandas_Streamlit.pdf`), com uma decomposição bastante detalhada de cada trecho de código, célula por célula — refletida na explicação de cada função/método abaixo.

## Leitor de Planilhas — versão Tkinter

Ver [`leitor-planilhas-tkinter/pandas_tk.py`](./leitor-planilhas-tkinter/pandas_tk.py).

> Esta versão é funcionalmente idêntica à versão 1 do leitor de planilhas já documentada na [Aula 11](../aula-11-tkinter-eventos-bindings-pandas/leitor-planilhas-excel/v1_leitor_basico.py) (mesma lógica, apenas com pequenas diferenças de quebra de linha) — a aula a retoma para servir de contraponto direto à versão em Streamlit, explicada abaixo.

Fluxo: `filedialog.askopenfilename(...)` abre um seletor de arquivo restrito a `.xlsx`/`.xls` → `pd.read_excel(arquivo)` carrega os dados → a `Treeview` é limpa (`tree.get_children()` + `tree.delete(i)`) e repopulada linha a linha (`df.iterrows()` + `tree.insert(...)`).

## Leitor de Planilhas — versão Streamlit

Ver [`leitor-planilhas-streamlit/pandas_streamlit.py`](./leitor-planilhas-streamlit/pandas_streamlit.py).

Streamlit é um framework Python para construir aplicações web de dados sem precisar escrever HTML/CSS/JavaScript — cada elemento da interface é uma chamada de função (`st.title`, `st.file_uploader`, etc.), e o script inteiro é reexecutado a cada interação do usuário.

Fluxo desta versão, mais completo que o da versão Tkinter:

1. `st.file_uploader(...)` recebe o arquivo Excel diretamente no navegador.
2. O arquivo é lido em memória com `BytesIO(arquivo_carregado.read())` e aberto como `pd.ExcelFile(...)`, o que permite listar as abas da planilha (`dados_excel.sheet_names`).
3. `st.selectbox(...)` deixa o usuário escolher qual aba visualizar, e `pd.read_excel(dados_excel, sheet_name=...)` carrega o `DataFrame` correspondente.
4. Exibe mensagem de sucesso e as dimensões da tabela (`dataframe.shape`), e mostra os dados com `st.dataframe(...)`.
5. Oferece exportação dos dados em dois formatos, gerados em memória (sem salvar em disco): CSV (`dataframe.to_csv(...).encode('utf-8')`) e Excel (via `BytesIO` + `pd.ExcelWriter(..., engine='xlsxwriter')`), cada um disponibilizado com `st.download_button(...)`.
6. Tratamento de erro com `try/except`, exibindo a mensagem via `st.error(...)`.

## Comparativo Tkinter x Streamlit

| Aspecto | Tkinter | Streamlit |
|---|---|---|
| Tipo de aplicação | Desktop (janela nativa) | Web (roda no navegador) |
| Interface | Widgets montados manualmente (`pack`/`grid`) | Elementos declarativos (`st.*`), reexecuta o script a cada interação |
| Seleção de arquivo | Diálogo do sistema operacional (`filedialog`) | Upload via navegador (`st.file_uploader`) |
| Suporte a múltiplas abas | Não implementado nesta versão | Sim, com seletor de aba |
| Exportação de dados | Não implementado nesta versão | CSV e Excel, via download direto no navegador |

## Como executar

```bash
# Versão Tkinter
python3 leitor-planilhas-tkinter/pandas_tk.py

# Versão Streamlit
pip install streamlit pandas openpyxl xlsxwriter
streamlit run leitor-planilhas-streamlit/pandas_streamlit.py
```

> A versão Streamlit abre automaticamente uma aba no navegador padrão ao ser executada com `streamlit run`.

## Referência

Material baseado nos PDFs "Pandas_TK" e "Pandas_Streamlit", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
