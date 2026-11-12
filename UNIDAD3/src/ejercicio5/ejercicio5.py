"""
Ejercicio 5: Función que muestra los números perfectos  
Escribe una función llamada mostrar_numeros_perfectos que reciba un número entero como parámetro y 
muestre todos los números perfectos entre 1 y el número dado. Un número es perfecto si es igual a la suma de sus divisores propios.
"""

def recoger_numero_entero():
    while True:
        try:
            numero = int(input("Introduce un numero entero positivo >0:\n>"))
            if numero <= 0:
                raise AttributeError("No es un positivo")
        except ValueError:
            print("No es un entero")
        except AttributeError:
            print("No es un positivo")
        else:
            return numero
            
def encontrar_numeros_perfectos(tope):
    perfectos=[]
    for numero in range(1,tope):
        divisor =  list(n for n in range(1,numero) if numero % n == 0)
        if sum(divisor) == numero:
            perfectos.append(numero)
    return perfectos


def mostrar_numeros_perfectos(num_perfectos):
    print(", ".join(str(n) for n in num_perfectos))

elegido = recoger_numero_entero()
num_perfectos = encontrar_numeros_perfectos(elegido)
mostrar_numeros_perfectos(num_perfectos)