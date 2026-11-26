"""
A5. Notas subidas un punto (solo las suspensas)
notas = [3, 7, 4, 9, 2, 6, 5, 1]
recuperadas = []
for nota in notas:
if nota < 5:
recuperadas.append(nota + 1)
print(recuperadas)
# Resultado esperado: [4, 5, 3, 2]
"""

notas = [3, 7, 4, 9, 2, 6, 5, 1]

lista = [n+1 for n in notas if n < 5]
print(lista)