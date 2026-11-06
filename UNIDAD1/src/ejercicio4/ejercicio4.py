"""
Descripción: Crear un programa que solicite al usuario dos números y los compare, 
mostrando cuál es mayor o si son iguales.
"""

numero1 = int(input("Dame numero1:\n>"))
numero2 = int(input("Dame numero2:\n>"))

if numero1 == numero2:
    print(f"numero1 {numero1} y numero2 {numero2} son iguales")
else:
    if numero1 > numero2:
        print(f"numero1 {numero1} mayor numero2 {numero2}")
    else:
        print(f"numero1 {numero1} menor numero2 {numero2}")


    



