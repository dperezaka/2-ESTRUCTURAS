"""
Ejercicio 3: Función para contar vocales
Escribe una función llamada contar_vocales que reciba una cadena de texto y devuelva el número de vocales en la cadena. 
Usa esta función en un programa que permita al usuario introducir una frase y muestre cuántas vocales contiene.
"""

def contar_vocales(palabra):
    vocales = ["a", "e" ,"i" ,"o" ,"u"]
    diccionario= {}
    for letra in vocales:
        diccionario[letra] = len([n for n in palabra if n == letra])
    return diccionario


frase = input("Introduce la frase:\n>")
diccionario = contar_vocales(frase)
print("\n".join([f"La letra {letra}, esta repetida {numero}" for letra, numero in diccionario.items()]))