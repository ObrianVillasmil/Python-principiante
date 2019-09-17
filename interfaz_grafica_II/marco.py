from tkinter import *
from package.frame import frame

class crearVentana(frame):
	raiz=""
	titulo=""
	resizableX=""
	resizableY=""
	colorFondo=""
	icono=""

	def __init__(self):
		self.raiz = Tk()
		self.titulo = input("Ingrese el titulo de la ventana: ")
		self.resizableX = input("Se redimencionara horizontalmente? (y/n): ")
		self.resizableY = input("Se redimencionara verticalmente? (y/n): ")
		self.colorFondo = input("Ingrese el color de fondo del marco: ")
		self.icono = input("Ingrese el nombre del icono con su extencion .ico: ")
		
	def paramRaiz(self,titulo,colorFondo,icono,resizableX=False,resizableY=False):
		if self.raiz != "":
			if self.titulo != "":
				self.raiz.title(self.titulo)
			if self.colorFondo != "":
				self.raiz.config(bg=self.colorFondo)
			if self.icono != "":
				self.raiz.iconbitmap(self.icono)
			self.raiz.resizable(self.resizableX,self.resizableY)

		else:
			print("No se inicializo la ventana, contacte al administrador")



ventana = crearVentana()
ventana.paramRaiz(ventana.titulo,ventana.resizableX,ventana.resizableY, ventana.colorFondo,ventana.icono)
ventana.crearFrame()
ventana.raiz.mainloop()