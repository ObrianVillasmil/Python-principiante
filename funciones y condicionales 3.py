intento = 1
contrasena = 1234
acceso = False
diaSemanaSeleccionada = False
mSeleccionada = False
hSeleccionado = False
contrasennaAcceso = input("Ingrese la contraseña :")

def diaSemana():
	return ['Lunes','Martes','Miercoles','Jueves','Viernes']

def materias():
	return ['quimica','fisica','matematica','sociales']

def horario():
	return ['vespertino','diurno','nocturno']

while contrasena != int(contrasennaAcceso):
	contrasennaAcceso = input("Contrasena Incorrecota, ingrese nuevamente la contraseña :")
	intento+=1
	if intento == 3:
		print("Lo sentimos ha intentado ingresar tres veces sin exito, espere 3 minutos para intentar volver a accesar")
		break

if contrasena == int(contrasennaAcceso):
	acceso = True


if acceso:

	print("Bienvenido, a continuación se muestran las opciones disponibles para escoger sus materias y horarios")

	print("Dias: ")
	for i in diaSemana():
		print(i,end=" ")
		
	print('\n'+"Materias: ")
	for j in materias():
		print(j,end=" ")
		
	print('\n'+"Horarios: ")
	for k in horario():
		print(k,end=" ")

	diaSeleccionado =input('\n'+"Escriba uno de los dias de la semana expuesto: ")

	while diaSemanaSeleccionada == False:
		print("El dia seleccionado no se encuentra en la lista expuesta")
		diaSeleccionado =input('\n'+"Escriba uno de los dias de la semana expuesto: ")
		if diaSeleccionado in diaSemana():
			diaSemanaSeleccionada = diaSeleccionado

	print('\n'+"Día seleccionado " + diaSemanaSeleccionada)

	materiaSeleccionada = input('\n'+"Escriba la materia que desea cursa del listado expuesto: ")

	if materiaSeleccionada in materias():
		mSeleccionada = materiaSeleccionada

	while mSeleccionada == False:
		print("La materia seleccionada no se encuentra en la lista expuesta")
		materiaSeleccionada = input('\n'+"Escriba la materia que desea cursa del listado expuesto: ")
		if materiaSeleccionada in materias():
			mSeleccionada = materiaSeleccionada
	
	print('\n'+"Materia seleccionada : " + mSeleccionada)

	horarioSelecionado = input("Seleccione su horario del listado expuesto: ")

	if horarioSelecionado in horario():
			hSeleccionado = horarioSelecionado

	while hSeleccionado == False:
		print("El horario seleccionado no se encuentra en la lista expuesta")
		horarioSelecionado = input("Seleccione su horario del listado expuesto: ")
		if horarioSelecionado in horario():
				hSeleccionado = horarioSelecionado
			
	print('\n'+"Felicitaciones a seleccionado la materia : " + mSeleccionada + " los dias: " + diaSemanaSeleccionada + " en el horaio: " +hSeleccionado)


	