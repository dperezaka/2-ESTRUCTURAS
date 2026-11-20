# Proyecto integrado: del juego monolítico a tres módulos

El documento original incluye el juego **«Adivina el número secreto»** construido mediante funciones. El siguiente paso es organizar esas funciones en varios archivos, con responsabilidades claras y fácilmente comprobables.

La propuesta mantiene el juego de un jugador y permite elegir el intervalo de números. Se divide en:

| Archivo             | Responsabilidad                                                          |
| :------------------ | :----------------------------------------------------------------------- |
| `logica.py`         | Generar el secreto y comprobar si un intento es mayor, menor o correcto. |
| `entrada.py`        | Pedir números enteros y validar las entradas.                            |
| `principal.py`      | Mostrar el menú, coordinar la partida y dar feedback al usuario.         |
| `pruebas_logica.py` | Comprobar la lógica automáticamente con `unittest`.                      |
|                     |                                                                          |

---

## 1. Lógica del juego

### `logica.py`

```
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
``` 

2. Gestión de entradas
entrada.py
```
def pedir_entero(mensaje):
    """Solicita un entero; repite hasta recibir una entrada válida."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Introduce un número entero válido.")
```
3. Programa principal
principal.py
```
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
```
4. Ejecutar y comprobar el proyecto
Guardar los archivos en una carpeta, abrir una terminal en esa carpeta y ejecutar:

Bash
```
python principal.py
```
(Si el equipo usa el comando python3, utilizarlo en su lugar).

Nota: Los archivos de ejemplo ya preparados están disponibles para descargar en el proyecto completo (ZIP con 4 archivos .py: principal.py, logica.py, entrada.py y pruebas_logica.py).

5. Pruebas automáticas sencillas
pruebas_logica.py
```
import unittest
from logica import comparar, generar_numero

class PruebasLogica(unittest.TestCase):
    def test_comparar(self):
        self.assertEqual(comparar(5, 5), "correcto")
        self.assertEqual(comparar(3, 5), "mayor")
        self.assertEqual(comparar(8, 5), "menor")

    def test_generar_en_rango(self):
        for _ in range(100):
            self.assertTrue(1 <= generar_numero(1, 10) <= 10)

if __name__ == "__main__":
    unittest.main()
```

Ejecución en Terminal
Bash
```
python -m unittest pruebas_logica -v
```

Ampliación: Dos jugadores
Enunciado:
Incorporar una opción para que el primer jugador establezca el número secreto y el segundo intente adivinarlo. ¿En qué módulo debería situarse la lógica para comparar intentos?

Solución y retroalimentación:

- La función comparar() se reutiliza sin cambios desde logica.py.
- En principal.py se podría añadir otra función jugar_dos_jugadores(),
- encargada de solicitar el secreto y los intentos a cada jugador.
- La validación de entradas continúa en entrada.py.
- No es necesario duplicar la función de comparación: la modularidad permite utilizar la misma lógica desde varios modos de juego.