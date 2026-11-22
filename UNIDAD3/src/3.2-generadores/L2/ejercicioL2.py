"""
Crear una lambda que reciba un número y devuelva "aprobado" si es >= 5, o "suspenso" en caso
contrario. Probarla con [3, 7, 4, 9, 5] .
Resultado esperado: ['suspenso', 'aprobado', 'suspenso', 'aprobado', 'aprobado']
"""

notas = [3, 7, 4, 9, 5]

resultado = ["aprobado" if x >= 5 else "suspenso" for x in notas]

print(resultado)

resultado2 = list(map(lambda x: "aprobado" if x >= 5 else "suspenso", notas))

print(resultado2)