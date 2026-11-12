"""
Ejercicio 4: Función que recibe dos listas y devuelve las combinaciones
Escribe una función llamada combinar_listas que reciba dos listas como parámetros y 
devuelva una nueva lista con todas las combinaciones posibles entre los elementos de ambas listas. 
Cada combinación debe ser una lista con dos elementos, uno de cada lista.
"""

def recoger_lista():
    print("Inicio lista")
    lista = []
    salida = None
    while salida != "ª":
        try:
            salida = input("Introduce un valor (str), ª para salir:\n>")
        except Exception as e:
            print(f"Ha sucedido un error {e}")
        if salida != "ª":
            lista.append(salida)
    return lista

def combinar_lista(lista1, lista2):
    try:
        lista_combinada = list(zip(lista1, lista2, strict=True))
    except Exception:
        return False
    else:
        return lista_combinada
    
def mostrar_resultado(lista_combinada):
    if lista_combinada == False:
        print("No son igual longuitud")
    else:
        print(lista_combinada)


lista1 = recoger_lista()
lista2 = recoger_lista()
print(f"lista1 {lista1}")
print(f"lista2 {lista2}")
lista_combinada1 = combinar_lista(lista1, lista2)
print(f"lista_combinada {lista_combinada1}")
mostrar_resultado(lista_combinada1) 


