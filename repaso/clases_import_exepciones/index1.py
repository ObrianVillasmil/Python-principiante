from validaciones.validar import validar

class index(validar):
	
	def __init__(self):
		
		self.dic={1:"Valida un string",2:"Valida un entero",3:"Valida un float",4:"Valida un mail"}
		
		for x in self.dic:
			print(x,")", self.dic[x])

		while True:
			v = self.autoriza(3);
			validado = v.comprueba()
			if(validado['success']):
				print(validado['valor'])
				existe = self.existeValor()
				if(existe):
					print("El valor existe") # desde aquí se pueden hacer otras cosas
					break
			

	def existeValor(self):
		while True:
			try:
				self.dic[int(self.op)]
				return True
				break
			except Exception as e:
				print("El valor ingresado no existe, intente de nuevo")
				return False;

			
	def autoriza(self,num):
		self.op=input("Seleccione una de las opciones para ejecutar: ")
		return validar(num,self.op)



clase = index()
