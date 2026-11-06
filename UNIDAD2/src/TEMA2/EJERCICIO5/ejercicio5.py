"""
Enunciado: Escribe un programa que solicite al usuario un número entero y
determine si es par o impar. Recuerda que un número es par si es divisible
por 2 sin dejar resto
"""

nota = int(input("Introduce numero entero:\n>"))
print(f"{'par' if nota % 2 == 0 else 'impar'}")