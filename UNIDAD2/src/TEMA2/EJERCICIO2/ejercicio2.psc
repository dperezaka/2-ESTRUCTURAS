Proceso sin_titulo
	Escribir "Dame un año"
	Leer anyo
	bisiesto <- Falso
	Si anyo MOD 4 = 0 Entonces
		bisiesto <- Verdadero
	Fin Si
	Si anyo MOD 100 = 0 Entonces
		bisiesto  <- Falso
	Fin Si
	Si anyo MOD 400 = 0 Entonces
		bisiesto <- Verdadero
	Fin Si
	Si bisiesto = Verdadero Entonces
		Escribir "Es bisiesto"
	SiNo
		Escribir "No es bisiesto"
	Fin Si
FinProceso