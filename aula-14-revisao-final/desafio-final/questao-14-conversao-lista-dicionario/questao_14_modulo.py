def lista_para_dicionario(lista_alunos):
    dicionario = {}
    for aluno in lista_alunos:
        matricula = aluno[0]
        dicionario[matricula] = {
            "nome": aluno[1],
            "etapa1": aluno[2],
            "etapa2": aluno[3],
            "etapa3": aluno[4],
            "total": aluno[5]
        }
    return dicionario