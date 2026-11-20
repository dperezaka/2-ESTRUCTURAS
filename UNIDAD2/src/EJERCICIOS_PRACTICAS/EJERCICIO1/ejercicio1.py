"""
Ejercicio 1: El Portero de Discoteca
Objetivo: Practicar input, conversión de tipos (int) y condicionales if-else.
Enunciado:
Crea un programa que pida al usuario su edad y su nombre.

Si el usuario tiene 18 años o más, imprime: "Bienvenido al club, [Nombre]".
Si tiene menos de 18, imprime: "Lo siento [Nombre], eres menor de edad. Vuelve en [X] años", donde [X] es la cantidad de años que le faltan para cumplir 18.
"""

nombre = str(input("Introduce tu nombre:\n>"))

while True:
    try:
        edad = int(input("Introduce tu edad:\n>"))
        if edad < 1 or edad > 119:
            raise TypeError
    except ValueError:
        print("No es un entero")
    except TypeError:
        print("edad entre 1 y 119")
    else:
        break
    
if edad >=  18:
    print(f"Bienvenido al club {nombre}")
else:
    print(f"Lo siento {nombre} vuelve en {18-edad}")