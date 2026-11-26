"""
B2. Solo strings
Dada mezcla = [1, "hola", 3.14, "mundo", True, "python"] , crea una lista que contenga solo los
elementos de tipo str .
Pista: usa isinstance(x, str) o type(x) == str
Resultado esperado: ['hola', 'mundo', 'python']
"""

mezcla = [1, "hola", 3.14, "mundo", True, "python"]

lista = [n for n in mezcla if type(n) == str ]
print(lista)