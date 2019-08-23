#si se quiere importar toda la clase
from nota_alumnos import notasAlumno

class Login(notasAlumno):
	
	def __init__(self):
		
		while True:
			try:
				self.usuario = str(input("Ingrese su usuario: "))
				self.contrasena = int(input("Ingrese su contraseña: "))
				break
			except:
				print("El usuario deben ser letras y la contrasena numeros")

	def roles(self,all=False,id=0):
		if (all):
			return {1:"Administrador",2:"Profesor",3:"Alumno"}
		elif id!=0:
			return datosDiccionario[id]

	def usuarios(self,all=False,user=""):
		arr = {
				"jose": {"rol":1,"contrasenna":123},
				"pedro" : {"rol":2,"contrasenna":1234},
				"daniel" : {"rol":3,"contrasenna":12345},
				"jesus" : {"rol":3,"contrasenna":123456}
			}
		if all:
			return arr 
		elif user!="":
			return arr[user]

	def getDataAlumno(self):
		usu = self.usuarios(self,True)
		data = {};
		for user in usu:
			if usu[user]['rol'] == 3:
				#agrega dicionarios dentro de otros diccionarios 
				data.setdefault(user,{'rol':usu[user]['rol'],'contrasenna':usu[user]['contrasenna']})
		return data
