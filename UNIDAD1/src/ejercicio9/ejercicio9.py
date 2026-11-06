"""
Descripción: Crear un programa que solicite un número positivo al usuario y calcule su factorial utilizando un bucle Mientras.
"""

prueba = True
while prueba == True:
    try:
        numero = int(input("Introduce numero positivo"))
        if numero < 0:
            raise AttributeError
        prueba = False
    except ValueError:
        print("No es un numero positivo")
        prueba = True
    except AttributeError:
        print("No debe de ser un  numero negativo")
        prueba = True

contador = 0
suma = 0
while contador <= numero:
    suma += contador
    contador +=1
    print(suma)