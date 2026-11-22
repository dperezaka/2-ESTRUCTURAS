"""
Dada palabras = ["hola", "", "mundo", "", "python", ""] , usar filter para eliminar las cadenas
vacías.
Resultado esperado: ['hola', 'mundo', 'python']
"""

def potencia(numero, exponente, acumulado=1):
  if exponente == 0:
    return acumulado
  return potencia(numero, exponente - 1, acumulado * numero)

print(potencia(2,3))