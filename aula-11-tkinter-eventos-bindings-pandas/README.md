# Aula 11 — Tkinter, Eventos e Bindings, Pandas

## Contexto

Décima primeira aula da disciplina, unindo dois temas: **Tkinter** (biblioteca padrão do Python para interfaces gráficas) e **Pandas** (biblioteca para manipulação e análise de dados). É a aula com o material prático mais extenso até aqui, culminando em uma pequena aplicação desktop completa de gestão de inventário.

## Conceitos teóricos abordados

- **Tkinter — biblioteca para interfaces gráficas:** criação de janelas (`tk.Tk()`, `.title()`, `.geometry()`) e do loop principal da aplicação (`root.mainloop()`).
- **Widgets comuns:** `Label` (texto fixo), `Button` (botão, associado a uma função via `command`), `Entry` (campo de texto de uma linha), `Text` (caixa de texto multilinha), `Combobox` (menu suspenso, do submódulo `ttk`), `Checkbutton`, `Radiobutton` e `Treeview` (tabela — usada para exibir os dados do inventário).
- **Gerenciadores de layout:** `pack()` (empacotamento sequencial, com `side`, `padx`/`pady`, `fill`, `expand`), `grid()` (posicionamento em linhas/colunas) e `place()` (posicionamento absoluto/relativo por coordenadas).
- **Diálogos e mensagens:** `messagebox` (`showinfo`, `showwarning`, `showerror`, `askyesno`), `filedialog` (`askopenfilename`, para abrir arquivos) e `simpledialog` (`askinteger`, para entrada de dados simples).
- **Eventos e bindings:** o método `.bind()` associa eventos de teclado ou mouse a uma função (ex.: `entry.bind("<KeyRelease>", funcao_que_filtra)`, `button.bind("<Button-1>", funcao_clique)`), permitindo reagir a ações do usuário além dos comandos de botão padrão.
- **Pandas:** biblioteca para manipulação de dados estruturados, leitura/escrita em múltiplos formatos (Excel, CSV, SQL, JSON) e análise exploratória. Estruturas fundamentais: `Series` (coluna única) e `DataFrame` (tabela). Leitura de dados com `pd.read_csv(...)`, `pd.read_excel(..., sheet_name=...)` e, via `sqlite3`, `pd.read_sql(...)`.

## Material de apoio

A pasta [`dados`](./dados/) contém as planilhas Excel usadas ou disponibilizadas ao longo da aula:

- **`teste.xlsx`** — planilha de exemplo simples (3 colunas genéricas), usada para testar os leitores das versões 1 e 2.
- **`inventario.xlsx`** — planilha real de controle de estoque (código, descrição, cor, quantidade, quantidade mínima, preço e valor em estoque), usada como base de dados da aplicação de gestão de inventário (versão 3).
- **`Lotofacil.xlsx`** — base histórica com os resultados de mais de 3.200 concursos da Lotofácil (números sorteados, ganhadores e rateios por faixa de acertos), disponibilizada como material de apoio para exercícios de análise de dados com Pandas.

## Exemplos teóricos

- [`exemplo-dataframe-pandas/dataframe.py`](./exemplo-dataframe-pandas/dataframe.py) — reproduz o exemplo de sala de criação de uma `Series` e de um `DataFrame` a partir de um dicionário.
- [`exemplo-mensagens-tkinter/mensagens.py`](./exemplo-mensagens-tkinter/mensagens.py) — pequena aplicação com um botão para cada tipo de diálogo do Tkinter (informação, aviso, erro, confirmação, seleção de arquivo e entrada de dados).

## Atividade prática — Leitor de Planilhas Excel (evolução em 3 versões)

A pasta [`leitor-planilhas-excel`](./leitor-planilhas-excel/) reúne três versões evolutivas de uma aplicação Tkinter + Pandas para ler e exibir planilhas Excel, com complexidade crescente:

1. **`v1_leitor_basico.py`** — versão inicial: um botão abre um seletor de arquivo (`filedialog`), lê a planilha escolhida com `pd.read_excel(...)` e exibe os dados em uma `Treeview` com 3 colunas fixas ("Coluna1", "Coluna2", "Coluna3").
2. **`v2_leitor_dinamico.py`** — evolui para colunas **dinâmicas**: em vez de nomes fixos, as colunas da `Treeview` são configuradas de acordo com as colunas reais do DataFrame carregado (`tree["columns"] = list(df.columns)`), adiciona tratamento de erro ao ler o arquivo (`try/except` com `messagebox.showerror`) e uma barra de rolagem vertical.
3. **`v3_gestao_inventario.py`** — evolui de um simples leitor para uma **aplicação completa de gestão de inventário**, estruturada como uma classe (`GestaoInventario`). Funcionalidades: carregar a planilha de inventário, adicionar/atualizar/remover itens (com uma janela de edição própria, `Toplevel`), busca/filtro em tempo real usando `.bind("<KeyRelease>", ...)`, seleção de linha com `<<TreeviewSelect>>`, e um rodapé que soma automaticamente o valor total em estoque, tratando a formatação de moeda brasileira (`R$ 1.234,56`).

## Como executar

> Os programas abrem uma interface gráfica (Tkinter) — não podem ser executados em um ambiente sem suporte a interface gráfica (ex.: terminal remoto sem X11/display).

```bash
python3 exemplo-dataframe-pandas/dataframe.py
python3 exemplo-mensagens-tkinter/mensagens.py
python3 leitor-planilhas-excel/v3_gestao_inventario.py
```

Ao rodar `v1`, `v2` ou `v3`, use o botão "Carregar Planilha" e selecione um dos arquivos da pasta [`dados`](./dados/) (`teste.xlsx` para as versões 1 e 2; `inventario.xlsx` para a versão 3).

## Dependências

```bash
pip install pandas openpyxl
```

> `openpyxl` é necessário para o Pandas conseguir ler arquivos `.xlsx`. O `tkinter` já vem incluído na instalação padrão do Python na maioria dos sistemas.

## Referência

Material teórico baseado no slide "AEDS - Aula 11 - Manipulando arquivos", do Prof. Bruno Fernando Lacerda de Oliveira (FANS, 2025).
