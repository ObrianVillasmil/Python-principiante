class generador(object):

	def __init__(self,maximo):
		self.maximo = maximo


	def numeroImpar(self):
		x=1;

		while x < self.maximo:
			yield x+2
			x+=2


genera = generador(20)		
numero = genera.numeroImpar()

while True:
	n = next(numero)
	if(n > 10):
		print(n)
		break
	else:
		print("Menor:",n)

