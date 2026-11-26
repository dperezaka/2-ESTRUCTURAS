"""
C3. Fizzbuzz con comprehension
Crea una lista del 1 al 20 donde:
Si el número es divisible por 3 y por 5, aparece "FizzBuzz"
Si es divisible solo por 3, aparece "Fizz"
Si es divisible solo por 5, aparece "Buzz"
En otro caso, aparece el número como string
Resultado esperado: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fiz
Pista: necesitarás expresiones condicionales (ternarios) anidadas. Si te resulta ilegible, eso 
"""

lista= [("FizzBuzz" if ((n % 3 == 0) and (n % 5 == 0)) else ("Fizz" if (n % 3 == 0) else ("Buzz" if (n % 5== 0) else n ))) for n in range(1,21,1) ]

print(lista)