"""
Escribir una función recursiva fib(n) que devuelva el n-ésimo número de Fibonacci.
fib(0) → 0
fib(1) → 1
fib(6) → 8 (0, 1, 1, 2, 3, 5, 8)
"""


def fib(numero, anterior = 0, primero = 1):
    if numero == 0:
        return anterior
    else:
        numero_nuevo = numero -1
        anterior, primero = primero, primero+anterior
        print(primero)
        return fib(numero_nuevo, anterior, primero)
        
fib(10)