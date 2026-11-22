"""
Escribir una función recursiva potencia(base, exponente) que calcule base^exponente sin usar ** .
potencia(2, 3) → 8 (2 × 2 × 2)
potencia(5, 0) → 1 (caso base: cualquier número elevado a 0 es 1)
"""

def potencia(numero, exponente, resultado = 0):
    if resultado == 0:
        salida = 1
    if (exponente -1) >= 0:
        salida = salida * numero
        potencia(numero, (exponente -1), salida)
    else:
        return salida

respuesta = potencia(2,3)

print(respuesta)