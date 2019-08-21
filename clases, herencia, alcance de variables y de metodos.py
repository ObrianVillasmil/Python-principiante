class notasAlumno():

	alumno=""
	materia = ""

	def materias(self,id=False):
		arrMaterias = {1:'Comunicacion',2:'Matematicas',3:'Química',4:'Física'}
		if(id):
			return arrMaterias[id]
		else:
			return arrMaterias

	def notas(self,alumno=False,materia=""):
		arrNotas = {
			"jose":{
				1:[7,6,9],
				2:[8,8,10],
				3:[8,7,6,10],
				4:[5,6,9]
			},
			"daniel":{
				1:[9,5,7,4],
				2:[8,9,5,10],
				3:[5,7,6],
				4:[8,5,9]
			}
		}

		if(alumno):
			if(materia != ""):
				return arrNotas[alumno][materia]
			return arrNotas[alumno]

	def __calculaPromedio(self,notas,alumno):
		x=0
		for materia in notas:
			sumatoria = 0
			y=0
			for n in notas[materia]:
				sumatoria += n
				y+=1
			x+=1
			promedio = sumatoria/y
			print( 'El promedio de la materia: ' + str(self.materias(x)) +  ' para el alumno ' +alumno+ ' es: '+ str(promedio))

	def getPromedio(self):

		self.alumno = input("Ingrese el nombre del alumno: ")
		self.materia = input("Ingrese la materia del alumno: ")

		if self.alumno !="" and self.materia == "":
			
			nota = self.notas(self.alumno);
			self.__calculaPromedio(nota,self.alumno)
		
		elif self.alumno !="" and self.materia != "":
			while True:
				try:
					materia = int(self.materia)
					break
				except:
					self.materia = input("Ingrese la materia del alumno, debe ser un numero entre 1 y 4: ")
				
			nota = self.notas(self.alumno,);
			nota = {self.materia:nota}
			self.__calculaPromedio(nota,self.alumno)

		else:
			print("Debe ingresar al menos el nombre del alumno")



#notas = notasAlumno()
#notas.getPromedio()

class Login(notasAlumno):
	
	def __init__(self):
		
		while True:
			try:
				self.usuario = str(input("Ingrese su usuario: "))
				self.contrasena = int(input("Ingrese su contraseña: "))
				break
			except:
				print("El usuario deben ser letras y la contrasena numeros")

		
	def roles(self,all=False,id=0):
		if (all):
			return {1:"Administrador",2:"Profesor",3:"Alumno"}
		elif id!=0:
			return datosDiccionario[id]
			

	def usuarios(self,all=False,user=""):
		arr = {
				"jose": {"rol":1,"contrasenna":123},
				"pedro" : {"rol":2,"contrasenna":1234},
				"daniel" : {"rol":3,"contrasenna":12345},
				"jesus" : {"rol":3,"contrasenna":123456}
			}
		if all:
			return arr 
		elif user!="":
			return arr[user]


login = Login()
login.getPromedio()
usuarios = login.usuarios(True);

if login.usuario in usuarios:
	
	if usuarios[login.usuario]['contrasenna'] == login.contrasena:
	
		print("Bienvenido al sitema ", login.usuario)
		roles = login.roles(True)

		if usuarios[login.usuario]["rol"] in roles:
			if(roles[usuarios[login.usuario]["rol"]] == "Administrador"):
				pass

			elif(roles[usuarios[login.usuario]["rol"]] == "Profesor"):
				pass

			else:
				pass

	else:
		print("La combinación de usuario y contraseña no exite")
else:
	print("El usuario no existe")