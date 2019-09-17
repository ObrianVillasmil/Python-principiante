import pickle

class LeerVariables():
	
	def __init__(self):
		
		archivo = open('archivo_variables','rb')
		archivo = pickle.load(archivo)
		print(archivo)