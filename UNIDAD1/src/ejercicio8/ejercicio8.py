"""
Descripción: Crear un programa que solicite un número al usuario y calcule la suma de todos los números desde 1 hasta ese número utilizando un bucle
"""

prueba = True
while prueba == True:
    try:
        numero = int(input("Introduce numero:\n>"))
        prueba = False
    except ValueError:
        print("No es entero")
        prueba = True

suma = 0
for n in range(numero+1):
    suma +=n
    print(suma)
