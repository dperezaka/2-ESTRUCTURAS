"""
Descripción: Pide al usuario dos números enteros a y b (donde a < b). El
programa debe contar cuántos números pares hay en el rango de a a b
(incluidos).
"""

superior = int(input("Introduce numero superior:\n>"))
inferior= int(input("Introduce numero inferior:\n>"))

for n in range(inferior,superior,1):
    print(f"{n}\n" if n % 2 == 0 else "", end="")