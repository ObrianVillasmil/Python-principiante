from io import open

class crear():
	
	def __init__(self):
		self.nombreArchivo = input("Escribe el nombre del archivo:")
		archivo = open(self.nombreArchivo+".txt",'w')

		while True:
			self.texto = input("Ingrese el contenido del archivo: ")
			archivo.write(self.texto+"\n")
			
			pregunta = input("Desea continuar escribiendo en el archivo.? y/n: ")

			if(pregunta != "y"):
				archivo.close()
				del (archivo)
				break
	