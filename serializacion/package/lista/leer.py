import pickle


class LeerLista:
	
	def __init__(self):
		
		archivo = open('archivo_lista','rb')
		archivo = pickle.load(archivo)
		print(archivo)