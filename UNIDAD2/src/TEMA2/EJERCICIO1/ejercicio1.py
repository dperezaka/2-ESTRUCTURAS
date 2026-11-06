"""
Enunciado: Escribe un programa que solicite al usuario tres números
correspondientes a los lados de un triángulo. El programa debe determinar
si el triángulo es equilátero (todos los lados iguales), isósceles (dos lados
iguales) o escaleno (todos los lados diferentes). Usa condicionales para
evaluar estas características.
"""
prueba = False
while prueba == False:
    try:
        prueba = True
        lado1 = int(input("Escibe lado1:\n>"))

        lado2 = int(input("Escibe lado2:\n>"))

        lado3 = int(input("Escibe lado3:\n>"))
    except ValueError:
        print("No son enteros")
        prueba = False
        
if lado1 == lado2  and lado2 == lado3:
    print("El triangulo tiene 3 lados iguales ==> Equilatero")
elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print("El triangulo no tiene lados iguales ==> Escaleno")
else:
    print("El triangulo tiene 2 lados iguales ==> Isosceles")
    