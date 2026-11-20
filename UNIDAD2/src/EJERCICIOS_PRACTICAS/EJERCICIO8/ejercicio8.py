"""
Ejercicio 8: Pirámide de Asteriscos (Bucles Anidados)
Objetivo: Practicar bucles anidados (for dentro de for o lógica de multiplicación de strings).
Enunciado:
Pide al usuario un número entero altura. Dibuja una pirámide de asteriscos alineada a la izquierda.
Si el usuario introduce 5, el resultado debe ser:

*
**
***
****
*****
(Extra: Intenta hacerlo usando bucles anidados, aunque Python permite multiplicar strings)
"""

while True:
    try:
        cantidad = int(input("Introduce un numero entero positivo:\n>"))
        if cantidad <=0:
            raise TypeError
    except ValueError:
        print("No es entero")
    except TypeError:
        print("No puede ser menor igual a 0")
    else:
        break
    
for n in range(1, cantidad +1,1):
    print("*" * n)
   
   
print("\n\n\n")
print("-" * 50)
print("\n\n\n")

for n in range(1, cantidad +1,1):
    for j in range(1, n+1,1):
        print("*", end = "")
    print("\n")