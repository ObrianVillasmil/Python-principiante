from package.variables.crear import CrearVariables
from package.variables.leer import LeerVariables
from package.lista.crear import CrearLista
from package.lista.leer import leerLista


class Index():

	desicion = ""
	opcionesAccion = {1:"Variables",2:"Listas",3:"Objetos",4:"Tuplas",5:"Diccionario"}
	
	def __init__(self):

		opciones = {1:"Crear un archivo binario",2:"Leer un archivo binario"}
		for x in opciones:
			print(str(x)+") " + opciones[x])

		while True:
			try:
				self.desicion = int(input("Que desea hacer?:"))
				if(self.desicion > 0 and self.desicion < 3):
					break				
				else:
					print("Debe escribir el numero de alguna de las dos opciones")
			except Exception as e:
				print("Debe escribir el numero de alguna de las dos opciones")


	def accion(self,param):

		if(param == 1):
			print("Desea Crear un archivo con: ")
			for x in self.opcionesAccion:
				print(str(x)+") " + self.opcionesAccion[x])
			
			while True:
				try:
					decisionAccion = int(input("Que desea hacer?:"))
					if(decisionAccion > 0 and decisionAccion < 6):
						break				
					else:
						print("Debe escribir el numero de alguna de las dos opciones")
				except Exception as e:
					print("Debe escribir el numero de alguna de las dos opciones")
			
			if decisionAccion == 1: 
				CrearVariables()
			if decisionAccion == 2: 
				CrearLista()


		if(param == 2):
			pass
		


inicio = Index()	
inicio.accion(inicio.desicion)