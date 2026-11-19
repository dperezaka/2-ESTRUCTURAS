def pedir_entero(mensaje):
    """Solicita un entero; repite hasta recibir una entrada válida."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Introduce un número entero válido.")