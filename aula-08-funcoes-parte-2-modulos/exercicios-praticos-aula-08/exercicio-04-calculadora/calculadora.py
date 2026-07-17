def soma(*nums):
    if len(nums) < 2:
        return "É necessário pelo menos 2 números para realizar a soma."
    return sum(nums)

def subtracao(num_1, num_2):
    return num_1 - num_2

def multiplicacao(*nums):
    if len(nums) < 2:
        return "É necessário pelo menos 2 números para realizar a multiplicação."
    resultado = 1
    for num in nums:
        resultado *= num
    return resultado

def divisao(num_1, num_2):
    if num_2 == 0:
        return "O divisor não pode ser 0."
    return num_1 / num_2