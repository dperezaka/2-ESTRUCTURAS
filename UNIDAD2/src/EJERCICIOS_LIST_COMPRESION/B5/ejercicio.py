"""
B5. Números de Fibonacci menores que 100
Dada la lista de Fibonacci fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233] , crea una lista
solo con los que sean menores que 100.
Resultado esperado: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

lista = [n for n in fib if n < 100 ]
print(lista)