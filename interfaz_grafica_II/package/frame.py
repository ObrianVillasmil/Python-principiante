from tkinter import Frame
from tkinter import PhotoImage
from tkinter import Label

class frame():
	
	frame =""

	def crearFrame(self):
		self.frame = Frame()
		self.frame.pack()
		self.frame.config(bg="red")
		self.frame.config(width="500", height="400")
		return self.frame

	def agregar(self,frame):
		texto = input('ingrese el texto a mostrar: ')
		color = input('ingrese el color del texto a mostrar: ')
		imagen= PhotoImage(file="goku.png")
		Label(frame,image=imagen).place(x=180,y=20)
		#Label(frame, text=texto,fg=color).place(x=180,y=20)