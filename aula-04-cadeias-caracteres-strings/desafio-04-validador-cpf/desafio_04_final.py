import re

def validar_cpf(cpf):
    # Verificar se o formato está correto
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
        return False

    # Remover caracteres de formatação
    cpf = cpf.replace('.', '').replace('-', '')

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * len(cpf):
        return False

    # Calcular os dígitos verificadores
    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        digito = 11 - (soma % 11)
        return 0 if digito >= 10 else digito

    primeiro_digito = calcular_digito(cpf, 10)
    segundo_digito = calcular_digito(cpf, 11)

    # Verificar se os dígitos verificadores estão corretos
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"

cpf = input("Digite um número de CPF (xxx.xxx.xxx-xx): ")

if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")