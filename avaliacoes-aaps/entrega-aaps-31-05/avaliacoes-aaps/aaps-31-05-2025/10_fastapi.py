from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Rota assíncrona que recebe um parâmetro
@app.get("/piloto/{nome}")
async def dados_piloto(nome: str):
    # O FastAPI converte automaticamente dicionários Python em respostas JSON
    return {
        "piloto": nome,
        "status_telemetria": "Ativo",
        "mensagem": f"Coletando dados de voltas e tempo de setor para {nome.capitalize()}."
    }

# Instruções de execução:
# 1. No terminal, digite: uvicorn 10_fastapi:app --reload
# 2. Acesse no navegador: http://127.0.0.1:8000/piloto/bortoleto
# 3. Veja a documentação automática do Swagger em: http://127.0.0.1:8000/docs