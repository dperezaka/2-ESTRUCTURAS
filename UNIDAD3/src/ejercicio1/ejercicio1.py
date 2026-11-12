"""
Ejercicio 1: Mejora del juego de adivinanza
Modifica el juego de adivinanza del número secreto para que el jugador pueda elegir el rango de números
en los que se generará el número secreto. Por ejemplo, el jugador debería poder elegir que el número esté entre 1 y 50, o entre 100 y 200. La opción debe ser configurable desde el menú
"""

from random import randint

def elegir_rango():
    minimo = None
    while not isinstance(minimo, int):
        try:
            minimo = int(input("Dame el minimo:\n>"))   
        except ValueError:
            print("No es un entero")
    maximo = None
    while not isinstance(maximo, int):
        try:
            maximo = int(input("Dame el maximo:\n>"))   
        except ValueError:
            print("No es un entero")
    return (maximo,minimo)

def elegir_objetivo(maximo, minimo):
    objetivo = randint(minimo,maximo)
    return objetivo

def seleccionar_numero():
    numero = None
    while not isinstance(numero, int):
            try:
                numero = int(input("Dame el numero:\n>"))   
            except ValueError:
                print("No es un entero")
    return numero

def comparar_numero(numero, objetivo):
    if numero == objetivo:
        return (True, 0)
    elif numero > objetivo:
        return (False, +1)
    else:
        return (False, -1)

def representar_salida(acierto, estado):
    if acierto == True:
        pass # NO DEBEMOS HACER NADA
    elif estado == +1:
        print("Te pasaste")
    else:
        print("Corto")


maximo, minimo = elegir_rango()
objetivo = elegir_objetivo(maximo, minimo)
contador = 0
while True:
    contador +=1
    numero = seleccionar_numero()
    acierto, estado = comparar_numero(numero, objetivo)
    representar_salida(acierto, estado)
    if acierto == True:
        print("Acertaste")
        break
    if contador == 5 and acierto != True:
        print(f"Se te acabo el tiempo, numero era {objetivo}")
        break