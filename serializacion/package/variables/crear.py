import pickle
from package.variables.leer import LeerVariables

class CrearVariables():
	
	def __init__(self):
		
		val1 = input("Introduce el valor de la variable 1: ")

		archivo = open("archivo_variables","wb")
		pickle.dump(val1,archivo)
		archivo.close()
		del (archivo)
		desicion =input("Archivo binario archivo_variables creado, desea leer el contenido del archivo (y/n)")
		if(desicion == "y"):
			LeerVariables()
		else:
			print("Adios!!!")





