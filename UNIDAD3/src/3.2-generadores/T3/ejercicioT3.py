"""
Obtener los cuadrados de los números impares del 1 al 20.
Con bucle for:
resultado = []
for i in range(1, 21):
if i % 2 != 0:
resultado.append(i ** 2)
# [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
"""
# Con comprehension:
print([x**2 for x in range(1,21,1) if x % 2 != 0])

# Con map + filter:
lista = list(map(lambda z : z**2, filter(lambda x : x % 2 != 0, range(1,21,1))))
print(lista)    

# Con generador (si solo se necesita la suma):
generador = (x**2 for x in range(1,21,1) if x % 2 != 0)
print(generador)

for _ in range(11):
    print(next(generador))  # EL ULTIMO DA ERROR PUES SOLO HAY 10 NUMEROS Y HE PUESTO 11 ITERACIONES