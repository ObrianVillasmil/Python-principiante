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
		print("El contenido de su archivo es: ")
		print(lectura)


	def modificar(self):

		while True:
			
			modificar = input("Desea modificar una línea del archivo.? (y/n): ")

			if modificar == "y":
				self.archivo = open(self.nombre_archivo+".txt","r+") #r+ lectura y escritura de un archivo
			
				#leer linea por linea y devolver una lista de las lineas
				lineas =self.archivo.readlines()
				print("El contenido de su archivo es: \n")
				x =0
				for linea in lineas:				
					print(str(x)+") "+linea)
					x+=1

				modificaLinea  = int(input("Cual linea desea modifiar: "))
				nuevoContenido = input("Escriba el texto para modificar: ")
				
				#el metodo seek() coloca el puntero en el carcater que se le indique como parametro y empieza a escribir desde esa posicion
				self.archivo.seek(0)

				lineas[modificaLinea] = nuevoContenido
				self.archivo.writelines(lineas[modificaLinea]);

				self.archivo.close()
				self.leer()
				break

			elif modificar == "n":
				print("Adios!!!")
				break
		

		
	


			

		
		