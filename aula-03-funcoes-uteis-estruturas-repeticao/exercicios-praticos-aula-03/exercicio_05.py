quantidade_turmas = int(input("Digite a quantidade de turmas: "))

total_alunos = 0

for i in range(quantidade_turmas):
    while True:
        quantidade_alunos = int(input(f"Digite a quantidade de alunos na turma {i + 1}: "))
        if quantidade_alunos <= 40:
            total_alunos += quantidade_alunos
            break
        else:
            print("A turma não pode ter mais de 40 alunos. Tente novamente.")
media_alunos = total_alunos / quantidade_turmas
print(f"O número médio de alunos por turma é: {media_alunos:.2f}")