Proceso sin_titulo
	Escribir "Dame lado 1"
	Leer lado1
	Escribir "Dame lado 2"
	Leer lado2
	Escribir "Dame lado 3"
	Leer lado3
	Si lado1 <> lado2  Y lado2 <> lado3 Y lado3 <> lado1 Entonces
		Escribir "El triangulo no tiene lados iguales, luego es ESCALENO"
	SiNo
		Si lado1 = lado2  Y lado2 = lado3 Entonces
			Escribir "El triangulo tiene todos los lados iguales, luego es EQUILATERO"
		SiNo
			Escribir "El triangulo tiene un lado diferente, luego es ISOSCELES"
		Fin Si
	Fin Si
FinProceso
