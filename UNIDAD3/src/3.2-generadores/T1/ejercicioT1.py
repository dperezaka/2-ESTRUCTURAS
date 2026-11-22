"""
Dada una lista de notas, obtener las notas aprobadas (>= 5) redondeadas al entero más cercano.
notas = [3.7, 7.2, 4.8, 9.1, 5.0, 2.3, 6.6, 8.4]
"""
notas = [3.7, 7.2, 4.8, 9.1, 5.0, 2.3, 6.6, 8.4]

import math
# Con comprehension:
aprobados = [round(x)for x in notas if x >=5]  

print(aprobados)  
    
# Con map + filter:
aprobados2 = map(lambda y: round(y), filter(lambda x : x >=5, notas))
print(list(aprobados2))     
    
# Con generador (si solo se necesita iterar una vez)

print(list(round(x)for x in notas if x >=5))