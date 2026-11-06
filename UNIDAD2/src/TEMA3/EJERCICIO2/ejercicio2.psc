Proceso sin_titulo
	Escribir "Dame un numero a"
	Leer numa
	Escribir "Dame un numero b, mayor que a"
	Leer numb
	Para n <- numa Hasta numb Con Paso 1 Hacer
		Si n MOD 2 = 0 Entonces
			Escribir n
		Fin Si
	Fin Para
FinProceso