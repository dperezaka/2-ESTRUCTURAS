"""
Dada palabras = ["Python", "es", "un", "lenguaje", "de", "programación"] , ordenarla por longitud
y, en caso de empate, alfabéticamente.
Resultado esperado: ['de', 'es', 'un', 'Python', 'lenguaje', 'programación']
"""

frase = ["Python", "es", "un", "lenguaje", "de", "programación"]

orden1 = sorted(frase, key = lambda x: (len(x), x[0]))
print(orden1)