"""
Descripción: Crear un programa que utilice un bucle Para para contar y mostrar los números pares entre 1 y 20. 
Al final, debe mostrar la suma total de esos números
"""

suma=0
for n in range(2,20,2):
    print(n)
    suma += n
	
print(f"La suma total es de {suma}")