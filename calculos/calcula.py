from basicos.basico import CalculosBasicos
from area.area import CalculosAreas
from raiz.raiz import CalculosRaiz

class Calcula(CalculosBasicos,CalculosAreas,CalculosRaiz):
	
	def __init__(self):
		opciones = {1:"Básicos",2:"Área",3:"Raíz"}
		for op in opciones:
			print(str(op) + ") " +opciones[op])
		while True:
			try:
				operacion = int(input("Seleccione con el número de la operación cual desea ejecutar: "))
				if operacion <= len(opciones):
					break
				else: 
					print("Debe escribir sólo entre el rango de números descrito arriba para la opración")
			except Exception as e:
				print("Debe escribir sólo entre el rango de números descrito arriba para la opración")
			

		
calcula = Calcula()
