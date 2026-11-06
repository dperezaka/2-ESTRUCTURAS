

Algoritmo NumerosPrimos
	Escribir "Dame un numero mayor de 2"
	Leer num
	Para n <- 1 Hasta num Con Paso 1 Hacer
		contador<-2
		Primo<-Verdadero
		Mientras contador < n  Hacer
			Si n MOD contador  = 0 Entonces
				Primo <- Falso
			Fin Si
			contador <- contador + 1
		Fin Mientras
		
		Si Primo = Verdadero Entonces
			Escribir n
		Fin Si
		
	Fin Para
	
	
FinAlgoritmo
