"""
Ejercicio 7: Cajero Automático (Menú Interactivo)
Objetivo: Aglutinar while True, if-elif-else, variables, operadores y lógica de negocio básica.
Enunciado:
Simula un cajero automático.

Inicia con un saldo de 1000€.
El programa debe mostrar un menú repetidamente con las opciones:
Consultar saldo
Retirar dinero
Ingresar dinero
Salir
Lógica:
Si elige 1: Muestra el saldo actual.
Si elige 2: Pide cantidad. Si tiene saldo suficiente, réstalo. Si no, imprime "Saldo insuficiente".
Si elige 3: Pide cantidad y súmala al saldo.
Si elige 4: Despídete y termina el programa (rompe el bucle infinito).
Si elige otra cosa: Di "Opción no válida".
"""

def pedir_cantidad(texto):
    while True:
        try:
            cantidad = int(input(texto+":\n>"))
            if cantidad <=0:
                raise TypeError
        except ValueError:
            print("No es entero")
        except TypeError:
            print("No puede ser menor igual a 0")
        else:
            break
    return cantidad

saldo = 1000.00
while True:
    try:
        eleccion = int(input(
"""1.Consulta saldo
2.Retira dinero
3.Ingresa Dinero
4.Salir
>"""))
        if eleccion <1 or eleccion > 4:
            raise TypeError
    except ValueError:
        print("Introduce numero Entero")
    except TypeError:
        print("Opcion no valida")
    
    if eleccion == 1:
        print(f"Saldo actual {saldo}")
        
    elif eleccion == 2:
        retirada = pedir_cantidad("Monto de retirada")
        if (saldo - retirada) > 0:
            print(f"Nuevo saldo {saldo - retirada}, saldo anterior {saldo}, retirada {retirada}")
            saldo = saldo - retirada
        else:
            print("Saldo insuficiente")
            
    elif eleccion == 3:
        ingreso = pedir_cantidad("Monto de ingreso")
        print(f"Nuevo saldo {saldo + ingreso}, saldo anterior {saldo}, ingreso {ingreso}")
        saldo = saldo + ingreso
        
    elif eleccion == 4:
        print("Hasta luego")
        break
    else:
        print("Opcion no valida")
    