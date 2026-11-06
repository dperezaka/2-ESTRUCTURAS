"""
Descripción: Crear un programa que solicite un número al usuario y muestre todos los números primos entre 1 y ese número utilizando un bucle Para.
Incluye la verificación de si un número es primo o no.
"""

prueba = True
while prueba == True:
    try:
        numero = int(input("Introduce numero positivo:\n>"))
        if numero < 0:
            raise AttributeError
        prueba = False
    except ValueError:
        print("No es un numero positivo")
        prueba = True
    except AttributeError:
        print("No debe de ser un  numero negativo")
        prueba = True

primos = []

for n in range(2,numero+1,1):  # nos dara los numeros hasta numero+1 (el propio numero), siempre es divisible por 1, asi que nos lo ahorramos
    primo = True
    for i in range(2,n,1): # nos dara los numeros hasta n-1, siempre es divisible por 1, asi que nos lo ahorramos
        if n % i == 0: # es decir es divisible por un numero que no es 1, ni el propio, luego no es primo
            primo = False
            break
    if primo == True:
        primos.append(n)
    
print(" ,".join(str(n) for n in primos))
if int(primos[-1]) == int(numero):
    print("El numero es primo")