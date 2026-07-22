import matplotlib.pyplot as plt

# Contagem de alunos
status = ['Aprovados', 'Reprovados']
quantidade = [24, 6]

# Criando um gráfico de barras
plt.bar(status, quantidade, color=['#4CAF50', '#F44336'])
plt.title('Balanço Final de Notas')
plt.xlabel('Situação do Aluno')
plt.ylabel('Quantidade')

# Salvando a figura para garantir que o output gráfico seja preservado
nome_arquivo = 'grafico_aprovacoes.png'
plt.savefig(nome_arquivo)

print(f"Gráfico de barras gerado e salvo com sucesso como '{nome_arquivo}'.")
# plt.show() # Descomente se quiser abrir a janela interativa