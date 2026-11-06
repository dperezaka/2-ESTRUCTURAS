"""
Enunciado: Escribe un programa que convierta una puntuación numérica en
una letra de calificación. Pide al usuario una puntuación (por ejemplo, entre
0 y 100) y convierte esa puntuación en una letra según la escala A, B, C, D, F.
Usa condicionales para clasificar la puntuación.
"""

nota = int(input("Introduce calificacion 0 - 100:\n>"))

if nota >90:
    print(f"La nota para {nota} es A")
if nota <89 and nota >80:
    print(f"La nota para {nota} es B")
if nota <79 and nota >70:
    print(f"La nota para {nota} es C")
if nota <69 and nota >60:
    print(f"La nota para {nota} es D")
if nota <59 and nota >50:
    print(f"La nota para {nota} es E")
if nota <50:
    print(f"La nota para {nota} es F")