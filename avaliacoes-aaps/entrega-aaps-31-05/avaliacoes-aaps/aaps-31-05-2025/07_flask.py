from flask import Flask

app = Flask(__name__)

# Rota que recebe um parâmetro 'nome' direto pela URL
@app.route('/saudacao/<nome>')
def saudacao_personalizada(nome):
    return f"<h1>Olá, {nome}!</h1><p>Sua rota dinâmica no Flask está funcionando perfeitamente.</p>"

if __name__ == '__main__':
    print("Iniciando o servidor Flask. Acesse: http://127.0.0.1:5000/saudacao/SeuNome")
    app.run(debug=True)