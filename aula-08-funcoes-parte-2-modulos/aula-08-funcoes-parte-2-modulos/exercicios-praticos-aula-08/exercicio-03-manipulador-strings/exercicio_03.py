import manipulador_strings # Importando o módulo manipulador_strings
# Testando as funções do módulo manipulador_strings
resultado = manipulador_strings.maiusculo("Cruzeiro Campeao!")
print(resultado) # Convertendo para maiúsculo
resultado = manipulador_strings.minusculo("Galo Eliminado!")
print(resultado) # Convertendo para minúsculo
resultado = manipulador_strings.frase_para_lista("A China Azul canta, e o Mineirao se levanta...")
print(resultado) # Convertendo frase para lista
resultado = manipulador_strings.tamanho("Existe um grande clube na cidade.")
print(resultado) # Contando o número de palavras
resultado = manipulador_strings.contador_palavras("Galo", "Cruzeiro", "Flamengo", "Sao Paulo")
print(resultado) # Contando o número de palavras passadas como parâmetros