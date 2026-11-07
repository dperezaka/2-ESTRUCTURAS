"""
Descripción: Escribe un programa en el que el usuario deba adivinar un
número secreto entre 1 y 100 (generado por el programa). Solo tiene 5
intentos para adivinarlo. Después de cada intento, el programa debe decir si
el número secreto es mayor o menor que el intento. Si el usuario adivina el
número antes de que se terminen los intentos, se le felicita. Si no, se
muestra el número secreto.
"""

import random

numero_adivinar = random.randint(1,100)
acierto = False
for n in range(5):
    numero_elegido = None
    while not isinstance(numero_elegido ,int):
        try:
            numero_elegido = int(input("Introduce numero:\n>"))
        except ValueError:
            print("No es un entero")
    if numero_adivinar == numero_elegido:
        acierto = True
        break
    elif numero_adivinar >numero_elegido:
        print("Te quedaste corto")
    else:
        print("Te pasaste")

print(f"Fallaste el numero era {numero_adivinar}" if acierto != True else  f"Acertaste el numero era {numero_adivinar}")