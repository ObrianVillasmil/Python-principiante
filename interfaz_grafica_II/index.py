class index():

	def __init__(self):
		self.celulares={1:{'marca': 'Nokia E3','precio':100},2:{'marca': 'Samsung s4','precio':100},3:{'marca': 'Samsung s5','precio':100},4:{'marca':'Samsung s8','precio':100}}

		print("Tenemos a la venta los siguientes celulares: ")
		for i in self.celulares:
			print(i,") ",self.celulares[i]['marca'])

	def compra(self):
		while True:
			try:
				opcion = int(input("Para seleccionar alguno escriba su respectivo numero en la lista: "))
				try:
					self.celulares[opcion]
					break
				except Exception as e:
					print("La seleccion ", e," no se encuentra en los celulares listados")
			except Exception as e:
				print("Tienes que ingresar solo numeros")

		print("Su seleccion es ",self.celulares[opcion]['marca'], " y su precio es: ", self.celulares[opcion]['precio'])

clase = index()
clase.compra()
