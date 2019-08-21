success= False;

while True:
	try:
		dia = int(input("Introduce el nùmnero del dìa de la semana que desees: "))
		break
	except:
		print("El valor ingresado debe ser un nùmero entero")
	finally:
		print("programa terminado")

def semana(dia):
	dias = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
	try:
		return dias[dia]
		success = True;
	except IndexError:
		print("El dìa ingresado no existe")

diaSemana = semana(dia)

if(success):
	print("El dìa escogido es: "+ str(diaSemana))



