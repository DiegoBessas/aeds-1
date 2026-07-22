import requests

cep_alvo = "35519000" # Exemplo de CEP
url = f"https://viacep.com.br/ws/{cep_alvo}/json/"

try:
    resposta = requests.get(url)
    
    # Checando o status da requisição HTTP
    if resposta.status_code == 200:
        dados = resposta.json()
        
        if "erro" not in dados:
            print("--- Dados Encontrados ---")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
            print(f"Bairro: {dados.get('bairro', 'Não especificado')}")
        else:
            print("O CEP digitado não foi encontrado.")
    else:
        print(f"Erro na comunicação com a API. Código: {resposta.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Falha na requisição HTTP: {e}")