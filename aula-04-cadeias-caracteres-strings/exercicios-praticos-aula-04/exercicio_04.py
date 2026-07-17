unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas_maiores = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

numero = int(input("Digite um número até 99: "))

if 0 <= numero <= 9:
    extenso = unidades[numero]
elif 10 <= numero <= 19:
    extenso = dezenas[numero - 10]
else:
    dezena = numero // 10
    unidade = numero % 10
    if unidade == 0:
        extenso = dezenas_maiores[dezena - 2]
    else:
        extenso = f"{dezenas_maiores[dezena - 2]} e {unidades[unidade]}"

print(f"O número {numero} por extenso é: {extenso}")