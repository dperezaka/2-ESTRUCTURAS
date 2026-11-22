"""
Dada palabras = ["python", "es", "un", "lenguaje"] , ordenarlas por longitud (más cortas primero)
usando sorted() con key=lambda .
Resultado esperado: ['es', 'un', 'python', 'lenguaje']
"""

palabras = ["python", "es", "un", "lenguaje"]

ordenado = list(sorted(palabras, key = lambda x: x[0]))

print(ordenado)