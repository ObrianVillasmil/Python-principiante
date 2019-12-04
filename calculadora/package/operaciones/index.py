from tkinter import *
import math

class operaciones():

	def suma(self,val1,val2):
		return float(val1)+float(val2)

	def resta(self,val1,val2):
		return float(val1)-float(val2)

	def multiplicacion(self,val1,val2):
		return float(val1)*float(val2)

	def division(self,val1,val2):
		return float(val1)/float(val2)

	def potencia(self,val1,val2):
		return float(val1)**float(val2)

	def raizCuadrada(self,val1,val2):
		return math.sqrt(float(val1))

	def porcentaje(self,val1,val2):
		return math.sqrt(float(val1))

	def borrar(self,var,cad):
		var.set('')
		cad.set('')
		self.num1=0
		print(self.num1)

	def operacion(self,op,val1,val2):
		print(op)
		res =0
		if(op=="+"):
			res= self.suma(val1,val2)

		elif(op=="-"):
			res= self.resta(val1,val2)

		elif(op=="X"):
			res= self.multiplicacion(val1,val2)

		elif(op=="/"):
			res= self.division(val1,val2)

		elif(op=="%"):
			res= self.porcentaje(val1,val2)

		elif(op=="x2"):
			res= self.potencia(val1,val2)

		elif(op=="√"):
			res= self.raizCuadrada(val1,val2)

		return res
	
		
	def accion(self,op):
		ope=False
		if(op=="+"):
			ope=True

		elif(op=="-"):
			ope=True

		elif(op=="X"):
			ope=True

		elif(op=="/"):
			ope=True

		elif(op=="%"):
			ope=True

		elif(op=="x2"):
			ope=True

		elif(op=="√"):
			ope=True

		return {'ope':ope,'op':op}
	