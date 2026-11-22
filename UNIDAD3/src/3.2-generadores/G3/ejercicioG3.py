"""
Escribir una función generadora aprobados(notas) que reciba una lista de tuplas (nombre, nota) y
produzca solo los nombres de los que tienen nota >= 5.
datos = [("Ana", 7), ("Luis", 3), ("Marta", 9), ("Pedro", 4)]
# aprobados(datos) → "Ana", "Marta"
"""
datos = [("Ana", 7), ("Luis", 3), ("Marta", 9), ("Pedro", 4)]
aprobados = list(x for x, y in datos if y >= 5)
print(aprobados)