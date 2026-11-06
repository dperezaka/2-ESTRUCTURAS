Proceso sin_titulo
	entero0_10 <- Falso
	Mientras entero0_10 = Falso Hacer
		Escribir "Introduce un entero entre 1 y 10"
		Leer digito
		entero0_10 <- Verdadero
		Si digito MOD 1 <> 0 Entonces
			entero0_10 <- Falso
		Fin Si
		Si digito > 10 O digito < 1 Entonces
			entero0_10 <- Falso
		Fin Si
	Fin Mientras
	Para n <- 1  Hasta 10 Con Paso 1 Hacer
		Escribir "Multiplicar ", n, " * ",digito, " es un total de ", digito*n
	Fin Para
FinProceso