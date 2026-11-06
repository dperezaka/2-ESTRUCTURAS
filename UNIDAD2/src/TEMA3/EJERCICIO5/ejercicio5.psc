Proceso sin_titulo
	objetivo <- Aleatorio(1,100)
	intento <- 0
	prueba<- Verdadero
	Mientras prueba = Verdadero Hacer
		Escribir "Dame un numero"
		Leer digito
		Si objetivo = digito Entonces
			Escribir "Has acertado en ", intento +1
			prueba = Falso
		SiNo
			intento = intento +1
			Escribir "Has fallado el intento ", intento
		Fin Si
		Si intento = 5 Entonces
			Escribir "Has fallado el intento ", intento, " el numero era el ", objetivo
			prueba = Falso
		SiNo
			Si digito > objetivo Entonces
				Escribir "Te pasaste"
			Fin Si
			Si digito < objetivo Entonces
				Escribir "Te falta"
			Fin Si
		Fin Si
	Fin Mientras
FinProceso