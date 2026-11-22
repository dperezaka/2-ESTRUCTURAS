"""
Dada numeros_str = ["3", "7", "-2", "10", "0"] , usar map para convertirlos a enteros y calcular su
suma.
Resultado esperado: 18
"""

numeros_str = ["3", "7", "-2", "10", "0"]

suma_numeros = sum(map(lambda x: abs(int(x)), numeros_str))

print(suma_numeros)