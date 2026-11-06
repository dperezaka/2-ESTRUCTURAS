Proceso sin_titulo
	Escribir "Introduce numero 1"
	Leer numero1
	Escribir "Introduce numero 2"
	Leer numero2
	Escribir "Introduce numero 3"
	Leer numero3
	Si numero1 = numero2 Y numero2 = numero3 Entonces
		Escribir "Los numeros son iguales"
	SiNo
		Si numero1 >= numero2 Entonces
			Si numero2 > numero3 Entonces
				Escribir "El mayor es ", numero1
			SiNo
				Si numero1 > numero3 Entonces
					Escribir "El mayor es ", numero1
				SiNo
					Escribir "El mayor es ", numero3
				Fin Si
			Fin Si
		SiNo
			Si numero2 > numero3 Entonces
				Escribir "El mayor es ", numero2
			SiNo
				Escribir "El mayor es ", numero3
			Fin Si
		Fin Si
		Si numero1 <= numero2 Entonces
			Si numero2 < numero3 Entonces
				Escribir "El menor es ", numero1
			SiNo
				Si numero1 < numero3 Entonces
					Escribir "El menor es ", numero1
				SiNo
					Escribir "El menor es ", numero3
				Fin Si
			Fin Si
		SiNo
			Si numero2 < numero3 Entonces
				Escribir "El menor es ", numero2
			SiNo
				Escribir "El menor es ", numero3
			Fin Si
		Fin Si
	Fin Si
FinProceso
