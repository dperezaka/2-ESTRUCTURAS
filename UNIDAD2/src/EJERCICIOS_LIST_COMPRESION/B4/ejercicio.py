"""
B4. Palabras sin espacios
Dada frase = " hola
 mundo
 cruel
 " , crea una lista con cada palabra de la frase (sin espacios
vacíos).
Pista: split() separa por espacios, pero puede dejar strings vacíos. ¿O no?
Resultado esperado: ['hola', 'mundo', 'cruel']
"""

frase = """ hola
 mundo
 cruel
 """ 

lista = frase.split()
print(lista) 

listafinal = [n for n in lista if n != " "]
print(listafinal)
