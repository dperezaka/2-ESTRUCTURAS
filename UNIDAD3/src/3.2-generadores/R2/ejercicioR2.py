"""
Escribir una función recursiva invertir(texto) que devuelva el texto al revés.
invertir("hola") → "aloh"
invertir("") → ""
"""

def invertir(palabra, invertido=" "):
    if len(palabra) == len(invertido)-1:
        return invertido
    else:
        invertido_nuevo = invertido + palabra[-len(invertido)]
        return invertir(palabra, invertido_nuevo)
    
    
invertida=invertir("Prueba")

print(invertida)