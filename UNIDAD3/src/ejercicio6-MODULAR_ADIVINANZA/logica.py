import random

def generar_numero(minimo, maximo):
    """Genera un entero entre minimo y maximo, ambos incluidos."""
    if minimo >= maximo:
        raise ValueError("El mínimo debe ser menor que el máximo")
    return random.randint(minimo, maximo)

def comparar(intento, secreto):
    """Devuelve 'correcto', 'mayor' o 'menor'."""
    if intento == secreto:
        return "correcto"
    return "mayor" if intento < secreto else "menor"