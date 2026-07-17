frase = input('Digite uma frase: ')
letras = [char for char in frase if char.isalpha()]
print(f'A frase contém {len(letras)} letras.')