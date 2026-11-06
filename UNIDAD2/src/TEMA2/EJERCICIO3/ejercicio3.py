"""
Enunciado: Escribe un programa que solicite al usuario tres números y
determine cuál es el mayor, cuál es el menor o si los tres son iguales. Usa
estructuras condicionales para comparar los tres valores.
Este ejercicio también se puede resolver utilizando las funciones max() y
min(), que son funciones integradas (built-in) en Python, lo que significa que
están disponibles de forma predeterminada en el lenguaje y no requieren
importar ninguna librería o módulo adicional para utilizarlas. Estas
funciones son parte del conjunto de funciones estándar de Python,
diseñadas para operar con diferentes tipos de datos como enteros,
flotantes, listas y tuplas. max() devuelve el valor más alto entre los
argumentos proporcionados. min() devuelve el valor más bajo entre los
argumentos proporcionados. En las soluciones tendrás la forma de hacerlo
con ellas, aunque veremos este tipo de funciones en la tercera unidad.
"""

numero1 = int(input("Introduce numero1:\n>"))

numero2 = int(input("Introduce numero2:\n>"))

numero3 = int(input("Introduce numero3:\n>"))

if numero1 == numero2 and numero2 == numero3:
    print("Son iguales")
else:
    print(f"El maximo es el {max(numero1, numero2, numero3)}")
    print(f"El minimo es el {min(numero1, numero2, numero3)}")