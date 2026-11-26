"""
A1. Tabla de multiplicar del 9
tabla = []
for i in range(1, 11):
tabla.append(f"9 x {i} = {9 * i}")
print(tabla)
# Resultado esperado: ['9 x 1 = 9', '9 x 2 = 18', ..., '9 x 10 = 90']
"""

lista = [f"{n} * 9 = {n * 9}" for n in range(1,11,1)]
print("\n".join(lista))
