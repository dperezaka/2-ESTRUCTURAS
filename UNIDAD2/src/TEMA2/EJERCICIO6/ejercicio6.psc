Proceso sin_titulo
	Escribir "Introduce bruto"
	Leer bruto
	Si bruto <= 10000 Entonces
		Escribir "Para un bruto de ", bruto, " se paga el 10%, es decir ", bruto*0.1, " quedando ", bruto * 0.9 
	SiNo
		Si bruto <= 30000  Entonces
			Escribir "Para un bruto de ", bruto, " se paga el 20%, es decir ", bruto*0.2, " quedando ", bruto * 0.8 
		SiNo
			Escribir "Para un bruto de ", bruto, " se paga el 30%, es decir ", bruto*0.3, " quedando ", bruto * 0.7 
		Fin Si
	Fin Si
FinProceso