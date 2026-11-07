"""
Descripción: Escribe un programa que pida al usuario números enteros
hasta que introduzca 0. Al final, el programa debe mostrar la suma de todos
los números positivos introducidos.
"""

salir = 1
suma = 0
while salir != 0:
    try:
        salir = int(input("Introduce numero:\n>"))
    except ValueError:
        print("No es un entero")
    else:
        print(f"{suma} + {salir} da un total de {suma + salir}")
        suma += salir
print(f"La suma total en de {suma}")