"""
Ejercicio 3: La Tabla de Multiplicar
Objetivo: Practicar bucle for, range() y formateo de texto (f-strings).
Enunciado:
Pide un número entero al usuario. El programa debe imprimir la tabla de multiplicar de ese número del 1 al 10.
Ejemplo: Si el usuario escribe 5, la salida debe ser: 5 x 1 = 5, 5 x 2 = 10, etc.
"""

numero = int(input("Introduce numero:\n>"))

for n in range(1,11,1):
    print(f"{numero} x {n} = {numero*n}")