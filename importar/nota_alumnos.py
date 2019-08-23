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
			"jesus":{
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
			if(arrNotas.get(alumno)):
				if(materia != ""):
					try:
						return arrNotas[alumno][materia]
					except Exception as e:
						print("La materia no existe")
				
				if(arrNotas.get(alumno)):
					return arrNotas[alumno]
				else:
					print("El alumno no existe")
					exit()

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
				
			nota = self.notas(self.alumno,materia);


			nota = {self.materia:nota}
			self.__calculaPromedio(nota,self.alumno)

		else:
			print("Debe ingresar al menos el nombre del alumno")

	def getPromedioAlumno(self,alumno):
		nota = self.notas(alumno);
		self.__calculaPromedio(nota,alumno)