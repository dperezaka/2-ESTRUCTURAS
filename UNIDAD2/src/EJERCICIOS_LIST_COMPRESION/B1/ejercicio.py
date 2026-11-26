"""
B1. Mitades
Dada numeros = [2, 7, 10, 15, 20, 3] , crea una lista con la mitad de cada número.
Resultado esperado: [1.0, 3.5, 5.0, 7.5, 10.0, 1.5]
"""

numeros = [2, 7, 10, 15, 20, 3]
 
lista = [n / 2 for n in numeros]

print(lista)