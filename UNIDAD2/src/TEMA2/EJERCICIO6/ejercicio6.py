"""
Enunciado: Escribe un programa que calcule el impuesto sobre los ingresos
anuales de una persona. Pide al usuario que introduzca su ingreso anual. Si
el ingreso es menor o igual a 10,000, el impuesto es del 10%. Si es menor o
igual a 30,000, el impuesto es del 20%. Si es mayor a 30,000, el impuesto es
del 30%. Usa condicionales para calcular el impuesto
"""

bruto = int(input("Dame bruto:\n>"))

if bruto <=10000:
    print(f"Para {bruto} es el impuesto de un 10% dejando un neto de {bruto * 0.9}")
elif bruto > 30000:
    print(f"Para {bruto} es el impuesto de un 30% dejando un neto de {bruto * 0.7}")
else:
    print(f"Para {bruto} es el impuesto de un 20% dejando un neto de {bruto * 0.8}")