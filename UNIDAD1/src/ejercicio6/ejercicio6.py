"""
Descripción: Crear un programa que solicite un número al usuario y determine si es par o impar.
"""

prueba = True
while prueba == True:
    try:
        numero = int(input("Dame un numero"))
        prueba = False
    except ValueError:
        print("No es entero")
        prueba = True

if numero % 2 == 0:
    print("Par")
else:
    print("Impar")