"""
C2. Aplanar una lista de listas
Dada matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] , crea una lista plana con todos los elementos.
Resultado esperado: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Pista: dos for anidados, el primero recorre filas, el segundo recorre elementos
"""

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lista = [ elemento for sublista in matriz for elemento in sublista]
print(lista)