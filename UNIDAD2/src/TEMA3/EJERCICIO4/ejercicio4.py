"""
Descripción: Escribe un programa que pida al usuario un número n y
muestre la tabla de multiplicar de ese número del 1 al 10. Si el usuario
introduce un número fuera del rango 1 a 10, se le debe pedir que vuelva a
introducir un número válido
"""

salir = 0

while salir < 1 or salir > 10:
    try:
        salir = int(input("Introduce numero:\n>"))
    except ValueError:
        print("No es un entero")
    else:
        print(f"La tabla del {salir}")
        for n in range(10):
            print(f"{salir} * {n + 1} = {salir * (n+1)}")