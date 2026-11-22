"""
Crear una tabla con los factoriales del 1 al 10 usando la función recursiva factorial() y una
comprehension
"""

def factorial(numero=10):
    print(f"El factorial de {numero} es {sum([x for x in range(numero+1)])}")
    numero = numero -1
    if numero < 0:
        return False
    else:
        return factorial(numero)
    
factorial()