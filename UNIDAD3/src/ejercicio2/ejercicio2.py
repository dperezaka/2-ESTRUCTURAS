"""
Ejercicio 2: Función para verificar números primos
Escribe una función llamada es_primo que reciba un número entero y devuelva True si el número es primo o False si no lo es. 
Luego, usa esta función en un programa que permita al usuario introducir un número y verificar si es primo.

"""

def introducir_entero():
    numero = None
    while not isinstance(numero, int):
        try:
            numero = int(input("Dame el numero entero elegido:\n>"))
        except ValueError:
            print("Introduce un entero")
    return numero

def es_primo(numero):
    primo = True
    for n in range(2,numero):
        print(f"para {n} el valor del divisor es {numero % n}")
        if numero % n == 0:
            primo = False
            break
    return primo
        
numero = introducir_entero()
primo = es_primo(numero)
if primo == True:
    print("Es primo")
else:
    print("No es primo")