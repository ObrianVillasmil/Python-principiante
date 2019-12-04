from tkinter import *

class AgregaContenido(object):
	
	def agregar(self,frame):
		texto = input('ingrese el texto a mostrar: ')
		color = input('ingrese el color del texto a mostrar: ')
		imagen= PhotoImage(file="goku.png")
		Label(frame,image=imagen).place(x=180,y=20)
		Label(frame, text=texto,fg=color).place(x=180,y=20)
		
		
