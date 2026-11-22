"""
Dada una lista de productos con nombre y precio, obtener los nombres de los productos que cuestan
más de 20€, en mayúsculas, ordenados por precio de mayor a menor.
productos = [
("Camiseta", 25.0),
("Calcetines", 5.0),
("Pantalón", 40.0),
("Gorra", 12.0),
("Chaqueta", 80.0),
]
"""

productos = [
("Camiseta", 25.0),
("Calcetines", 5.0),
("Pantalón", 40.0),
("Gorra", 12.0),
("Chaqueta", 80.0),
]

# Con comprehension + sorted
ordenado = sorted([x.upper() for x, y in productos if y > 20], key= lambda z: z[1], reverse=True)
print(ordenado)

# Con map + filter + sorted
ordenado2= map(lambda y: y[0].upper(), sorted(filter(lambda x : x[1] > 20, productos), key= lambda z: z[1], reverse = True))
print(list(ordenado2))