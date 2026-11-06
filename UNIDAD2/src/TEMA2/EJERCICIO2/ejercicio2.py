"""
Enunciado: Un año es bisiesto si es divisible por 4, excepto aquellos años
que son divisibles por 100, a menos que también sean divisibles por 400.
Escribe un programa que pida al usuario un año y determine si es bisiesto o
no. Asegúrate de usar las condiciones correctas para esta evaluación.
"""

anyo = int(input("Introduce año:\n>"))

bisiesto = False
if anyo % 4 == 0:
    bisiesto = True
if anyo % 100 == 0:
    bisiesto = False
if anyo % 400 == 0:
    bisiesto = True
    
if bisiesto == True:
    print(f"El año {anyo} es bisiesto")
else:
    print(f"El año {anyo} no es bisiesto")