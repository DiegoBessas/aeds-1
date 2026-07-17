arquivo = open("../arquivo1.csv", "r")
alunos = []
soma = 0
maior = 0
aluno_maior_nota = ""
menor = -1
aluno_menor_nota = ""
for linha in arquivo:
	aluno = linha.rstrip('\n').split(",")[0]
	nota = int(linha.rstrip('\n').split(",")[1])
	alunos.append([aluno, nota])
	soma = soma + nota
	if nota > maior:
		maior = nota
		aluno_maior_nota = aluno
	if nota < menor or menor == -1:
		menor = nota
		aluno_menor_nota = aluno
print("Media: " + str(soma/len(alunos)))
print("Maior Nota: " + str(maior))
print("Aluno com maior nota: " + aluno_maior_nota)
print("Menor Nota: " + str(menor))
print("Aluno com menor nota: " + aluno_menor_nota)