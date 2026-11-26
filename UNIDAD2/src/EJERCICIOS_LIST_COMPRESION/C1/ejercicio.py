"""
C1. Producto cartesiano
Dadas dos listas colores = ["rojo", "azul"] y tallas = ["S", "M", "L"] , crea una lista con todas
las combinaciones posibles como tuplas.
Resultado esperado: [('rojo', 'S'), ('rojo', 'M'), ('rojo', 'L'), ('azul', 'S'), ('azul', 'M'),
Pista: se pueden anidar dos for dentro de una comprehension
"""

colores = ["rojo", "azul"] 
tallas = ["S", "M", "L"]

lista = [(x,y) for x in colores for y in tallas]
print(lista)