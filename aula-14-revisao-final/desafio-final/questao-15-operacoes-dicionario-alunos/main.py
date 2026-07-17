import questao_15_modulo

alunos = [
    [1, "marcus", 10, 20, 29, 59],
    [2, "joao", 15, 22, 25, 62],
    [3, "camila", 18, 23, 29, 70],
]

dicionario_alunos = questao_15_modulo.lista_para_dicionario(alunos)

print(dicionario_alunos)

print("A - Mostrar nome e nota total de cada aluno:")
for matricula, dados in dicionario_alunos.items():
    print(f"Nome: {dados['nome']}, Nota total: {dados['total']}")

print("B - Mostrar alunos com total maior que 60:")
for matricula, dados in dicionario_alunos.items():
    if dados['total'] > 60:
        print(f"Aluno com total > 60: {dados['nome']} (Total: {dados['total']})")

print("C - Mostrar nome e matrícula de cada aluno:")
for matricula, dados in dicionario_alunos.items():
    print(f"Nome: {dados['nome']}, Matrícula: {matricula}")