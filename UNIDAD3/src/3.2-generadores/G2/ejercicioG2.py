"""
Escribir una función generadora fibonacci(n) que produzca los primeros n números de Fibonacci.
fibonacci(8) → 0, 1, 1, 2, 3, 5, 8, 13
"""

def fibonacci(numero):
    a, b = 0, 1
    for _ in range(numero):
        yield a
        a, b = b, a + b
    return a

lista = list(fibonacci(8))
print(lista)
    