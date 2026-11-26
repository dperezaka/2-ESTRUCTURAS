"""
A2. Números al revés
numeros = [1, 2, 3, 4, 5]
reversos = []
for n in numeros:
reversos.append(-n)
print(reversos)
# Resultado esperado: [-1, -2, -3, -4, -5]
"""

numeros = [1, 2, 3, 4, 5]

lista = [-n for n in numeros]
print(lista)