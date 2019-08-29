class CalculosBasicos():
	
	def suma(self):
		while True:
			try:
				val1 = float(input('ingresar el primer valor: '))
				val2 = float(input('ingresar el segundo valor: '))
				break
			except Exception as e:
				print("Sólo se deben ingresar números")
		print(val1+val2)

	def resta(self):
		while True:
			try:
				val1 = float(input('ingresar el primer valor: '))
				val2 = float(input('ingresar el segundo valor: '))
				break
			except Exception as e:
				print("Sólo se deben ingresar números")
		print(val1-val2)

	def miltipilcacion(self):
		while True:
			try:
				val1 = float(input('ingresar el primer valor: '))
				val2 = float(input('ingresar el segundo valor: '))
				break
			except Exception as e:
				print("Sólo se deben ingresar números")
		print(val1*val2)

	def division(self):

		while True:
			try:
				val1 = float(input('ingresar el primer valor: '))
				val2 = float(input('ingresar el segundo valor: '))
				break
			except Exception as e:
				print("Sólo se deben ingresar números")
			try:
				print(val1/val2)
			except Exception as e:
				print("No se puede dividir por 0")

	def potencia(self):
		while True:
			try:
				val1 = float(input('ingresar el primer valor: '))
				val2 = float(input('ingresar el segundo valor: '))
				break
			except Exception as e:
				print("Sólo se deben ingresar números")
		print(val1**val2)