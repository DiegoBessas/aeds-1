# Definindo o número de alunos
num_alunos = int(input("Número de alunos: "))

# Definindo uma lista para armazenar os dados dos alunos
alunos = []

# Criando uma lista para armazenar os dados dos alunos
for i in range(num_alunos):
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota da etapa 1 (total 25): "))
    nota2 = float(input("Nota da etapa 2 (total 30): "))
    nota3 = float(input("Nota da etapa 3 (total 45): "))
    nota_total = nota1 + nota2 + nota3
    alunos.append((nome, nota1, nota2, nota3, nota_total))

# Exibindo a lista de alunos com suas notas
print("\nLista de alunos e suas notas:")
for aluno in alunos:
    print(f"Nome: {aluno[0]}, Etapa 1: {aluno[1]}, Etapa 2: {aluno[2]}, Etapa 3: {aluno[3]}, Nota Total: {aluno[4]}")

# Calculando a média da turma
media_turma = sum(aluno[4] for aluno in alunos) / num_alunos
print(f"\nMédia da turma: {media_turma:.2f}")

# Exibindo os alunos abaixo da média
print("\nAlunos abaixo da média:")
for aluno in alunos:
    if aluno[4] < media_turma:
        print(f"Nome: {aluno[0]}, Nota Total: {aluno[4]}")