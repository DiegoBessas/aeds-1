def maiusculo(texto):
    """Recebe um texto e retorna o mesmo em maiúsculo."""
    return texto.upper()

def minusculo(texto):
    """Recebe um texto e retorna o mesmo em minúsculo."""
    return texto.lower()

def frase_para_lista(texto):
    """Recebe uma frase e retorna uma lista de palavras."""
    return texto.split()

def tamanho(texto):
    """Recebe um texto e retorna a quantidade de palavras no texto."""
    return len(texto.split())

def contador_palavras(*palavras):
    """Recebe as palavras como parâmetros e retorna o número de palavras informadas."""
    return len(palavras)