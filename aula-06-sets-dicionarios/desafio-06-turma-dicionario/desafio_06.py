#
# Definindo o número de alunos
num_alunos = int(input("Número de alunos: "))

# Criando o dicionário para armazenar os dados dos alunos
turma = {}

# Cadastrando os alunos no dicionário
for i in range(num_alunos):
    matricula = input(f"Matrícula do aluno {i + 1}: ")
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota da etapa 1 (total 25): "))
    nota2 = float(input("Nota da etapa 2 (total 30): "))
    nota3 = float(input("Nota da etapa 3 (total 45): "))
    nota_total = nota1 + nota2 + nota3
    turma[matricula] = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "nota_total": nota_total
    }

# Exibindo a lista de alunos com suas notas
print("\nLista de alunos e suas notas:")
for matricula, dados in turma.items():
    print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Etapa 1: {dados['nota1']}, "
          f"Etapa 2: {dados['nota2']}, Etapa 3: {dados['nota3']}, Nota Total: {dados['nota_total']}")