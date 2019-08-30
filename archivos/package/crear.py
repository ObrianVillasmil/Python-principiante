from io import open

class CrearArchivo():
	nombre_archivo=""
	contenido = ""
	archivo = ""

	def __init__(self):
		self.nombre_archivo = input("Escribe el nombre del archivo a crear: ")
	
	def crear(self):
		self.archivo = open(self.nombre_archivo+".txt","w") 

		while True:
			self.contenido = input("Escribe el contendio del archivo: ")
			self.archivo.write(self.contenido+"\n")

			continuar = input("Desea seguir agregando contenido al archivo (y/n): ")
			if(continuar == "n"):
				self.archivo.close()
				break

	def leer(self):
		self.archivo = open(self.nombre_archivo+".txt","r") 
		#leer todo el contenido
		lectura = self.archivo.read()

		self.archivo.close()
		print(lectura)


	def modificar(self):
		self.archivo = open(self.nombre_archivo+".txt","r") 
		
		#leer linea por linea y devolver una lista de las lineas
		lineas =self.archivo.readlines()
		x =1
		modificaLinea = print("Cual linea desea modifiar: ")
		for linea in lineas:				
			print(str(x) + linea)
			x+=1

		
		#el metodo seek() coloca el puntero de el carcater que s ele indique como parametro
		self.archivo.seek(1)
		self.archivo.close()


			

		
		