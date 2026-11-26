"""
B3. Índices de aprobados
Dada notas = [3, 7, 4, 9, 2, 6, 5, 1] , crea una lista con los índices (posiciones) de las notas
aprobadas (>= 5).
Pista: necesitarás range(len(notas)) para tener acceso al índice
Resultado esperado: [1, 3, 5, 6]
"""

notas = [3, 7, 4, 9, 2, 6, 5, 1]

lista = [notas.index(n) for n in notas if n >=5]
print(lista)

print([notas[n] for n in lista])