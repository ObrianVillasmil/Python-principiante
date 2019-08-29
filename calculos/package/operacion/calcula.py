from package.basicos.basico import CalculosBasicos
from package.area.area import CalculosAreas
from package.raiz.raiz import CalculosRaiz

class Calcula(CalculosBasicos,CalculosAreas,CalculosRaiz):
	success =False;

	def __init__(self):
		opciones = {1:"Básicos",2:"Área",3:"Raíz"}
		for op in opciones:
			print(str(op) + ") " +opciones[op])
		while True:
			try:
				operacion = int(input("Seleccione con el número de la operación cual desea ejecutar: "))
				if operacion in opciones:
					self.ejectOperacion(operacion)
					break
				else: 
					print("Debe escribir sólo entre el rango de números descrito arriba para la opración")
			except Exception as e:
				print("Debe escribir sólo entre el rango de números descrito arriba para la opración")

	def __comprobarIngreso(self,val,conversion):
		try:
			if conversion == "int":
				operacion = int(val)
				self.success = True
			elif conversion == "str":
				operacion = int(val)
				self.success = True

			return self.success
		except Exception as e:
			return self.success;

	def ejectOperacion(self,opercacion):
		basicas = {1:"Suma",2:"Resta",3:"Multiplicación", 4:"División", 5:"Potencia"}
		for b in basicas:
			print(str(b) + ") " +basicas[b])
		val = input("Selecciona un operación básica: ")
		while True:
			if self.__comprobarIngreso(val,"int"):
				break
			else:
				print("Seleccione un opción válida de las mostrada arriba")
		try:
			if int(val) == 1:
				self.suma()
			elif int(val) == 2:		
				self.resta()
			elif int(val) == 3:		
				self.multiplicacion()
			elif int(val) == 4:		
				self.division()
			elif int(val) == 5:		
				self.potencia()
		except Exception as e:
			print(e)


				


