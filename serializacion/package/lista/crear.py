import pickle
from package.lista.leer import leerLista

class CrearLista:
	
	def __init__(self):
		
		x=1
		valores=[]
		while True:
			val = input("Ingresa el valor " + str(x) + ": ")
			valores.append(val)
			desicion = input("Desea agregar otro valor? (y/n)")
			if(desicion == "y"):
				break
			x+=1

		print("Creando archivo con los valores ingresado")
		archivo = open("archivo_lista","wb")
		pickle.dump(valores,archivo)
		archivo.close()
		del (archivo)
		desicion =input("Archivo binario archivo_variables creado, desea leer el contenido del archivo (y/n)")
		if(desicion == "y"):
			leerLista()
		else:
			print("Adios!!!")