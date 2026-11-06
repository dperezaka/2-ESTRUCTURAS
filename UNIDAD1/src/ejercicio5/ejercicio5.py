"""
Descripción: Crear un programa que solicite tres números al usuario, calcule su promedio y lo muestre.
"""
prueba = True
while prueba == True:
    try:
        numero1 = int(input("Introduce numero1:\n>"))
        numero2 = int(input("Introduce numero2:\n>"))
        numero3 = int(input("Introduce numero3:\n>"))
        prueba = False
    except ValueError:
        print("No son enteros")
        prueba = True
    
print(f"El promedio de {numero1}, {numero2}, {numero3}, es {(numero1+numero2+numero3)/3}")