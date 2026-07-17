arquivo = open(r"C:\Users\diego\OneDrive\Área de Trabalho\Engenharia de Software\1º PERÍODO\ANÁLISE E ESTRUTURA DE DADOS\2ª ETAPA\AULA 9\arquivo1.csv", "r")
alunos = {}
for linha in arquivo:
	aluno = linha.rstrip('\n').split(",")[0]
	nota = int(linha.rstrip('\n').split(",")[1])
	alunos[aluno] = (nota)

opcao = 0
while opcao != 2:
	print("### Pesquisando notas de alunos ###")
	print(" 1 - Pesquisar Nota de Aluno")
	print(" 2 - Sair")
	opcao = int(input("Informe a opcao que deseja: "))
	if opcao == 1:
		aluno = input("Informe o nome do aluno que deseja pesquisar: ")
		if aluno in alunos:
			print("Aluno encontrado!")
			print(f"A nota do aluno {aluno} e: {alunos[aluno]}")
		else:
			print("Aluno nao encontrado. Por favor, tente novamente...")