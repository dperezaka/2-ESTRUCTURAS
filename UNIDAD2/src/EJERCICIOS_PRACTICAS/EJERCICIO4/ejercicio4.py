"""
Ejercicio 4: Suma de Números Pares
Objetivo: Practicar for, if y operador módulo %.
Enunciado:
Pide al usuario un número entero positivo N. El programa debe sumar todos los números pares que hay entre el 0 y ese número N (inclusive). Al final, muestra la suma total.
"""

numero = int(input("Introduce numero entero positivo:\n>"))

salida = sum(n for n in range(numero+1) if n % 2 == 0)

print(salida)