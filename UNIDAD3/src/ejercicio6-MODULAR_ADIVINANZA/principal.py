from entrada import pedir_entero
from logica import generar_numero, comparar

def jugar():
    while True:
        minimo = pedir_entero("Valor mínimo: ")
        maximo = pedir_entero("Valor máximo: ")
        if minimo < maximo:
            break
        print("El mínimo debe ser menor que el máximo.")

    secreto = generar_numero(minimo, maximo)
    intentos = 0
    print(f"Adivina el número entre {minimo} y {maximo}.")

    while True:
        intento = pedir_entero("Tu intento: ")
        intentos += 1
        pista = comparar(intento, secreto)
        if pista == "correcto":
            print(f"¡Acertaste en {intentos} intentos!")
            return
        print(f"El número secreto es {pista}.")

def main():
    while True:
        print("\n1. Jugar\n2. Salir")
        opcion = pedir_entero("Opción: ")
        if opcion == 1:
            jugar()
        elif opcion == 2:
            print("Hasta luego")
            return
        else:
            print("Elige 1 o 2.")

if __name__ == "__main__":
    main()