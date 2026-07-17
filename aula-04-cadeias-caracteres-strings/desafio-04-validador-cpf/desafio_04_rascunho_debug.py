# Desenvolva um programa que solicite a digitação de um número de CPF no
# formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da
# validação dos dígitos verificadores e dos caracteres de formatação.

cpf = input("Informe o CPF no formato correto: ")
resultado = "CPF Valido!"

cpf_partes = cpf.split(".")
if len(cpf_partes) != 3:
    resultado = "CPF Invalido!"
else:
    parte_um = cpf_partes[0]
    parte_dois = cpf_partes[1]
    parte_final = cpf_partes[2].split("-")
    if len(parte_final) != 2:
        resultado = "CPF Invalido!"
    else:
        parte_tres = parte_final[0]
        parte_quatro = parte_final[1]

if resultado == "CPF Valido!":
    if len(parte_um) != 3 or parte_um.isnumeric() == False:
        resultado = "CPF Invalido! {parte_um}"

    if len(parte_dois) != 3 or parte_dois.isnumeric() == False:
        resultado = "CPF Invalido! {parte_dois}"

    if len(parte_tres) != 3 or parte_tres.isnumeric() == False:
        resultado = "CPF Invalido! {parte_tres}"

    if len(parte_quatro) != 2 or parte_quatro.isnumeric() == False:
        resultado = "CPF Invalido! {parte_quatro}"

print(resultado)