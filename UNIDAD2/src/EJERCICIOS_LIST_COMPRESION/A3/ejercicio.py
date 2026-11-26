"""
A3. Divisibles por 5 entre 1 y 100
divisibles = []
for i in range(1, 101):
if i % 5 == 0:
divisibles.append(i)
print(divisibles)
# Resultado esperado: [5, 10, 15, ..., 100]
"""

lista = [n for n in range(1,101,1) if n % 5 == 0]
print(lista)