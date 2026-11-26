"""
A4. Palabras que empiezan por vocal
palabras = ["arbol", "casa", "elefante", "mesa", "isla", "perro", "uva"]
con_vocal = []
for p in palabras:
if p[0] in "aeiou":
con_vocal.append(p)
print(con_vocal)
# Resultado esperado: ['arbol', 'elefante', 'isla', 'uva']
"""

palabras = ["arbol", "casa", "elefante", "mesa", "isla", "perro", "uva"]
lista = [n for n in palabras if n[0] in ["a", "e" ,"i" ,"o" ,"u"] ]
print(lista)