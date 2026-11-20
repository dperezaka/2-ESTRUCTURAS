"""
Ejercicio 2: Calculadora de Notas
Objetivo: Practicar if-elif-else y operadores lógicos.
Enunciado:
Pide una nota numérica (del 0 al 10) al usuario.

Si la nota es menor que 5: Imprime "Suspenso".
Si es 5 o más pero menor que 7: Imprime "Aprobado".
Si es 7 o más pero menor que 9: Imprime "Notable".
Si es 9 o 10: Imprime "Sobresaliente".
Si la nota no está entre 0 y 10: Imprime "Error: Nota no válida".
"""
while True:
    try:
        nota = float(input("Introduce nota de 0 a 10:\n>"))
        if nota < 0 or nota > 10:
            raise TypeError
    except ValueError:
        print("No es float")
    except TypeError:
        print("Error: Nota no válida")
    else:
        break
       
if nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")