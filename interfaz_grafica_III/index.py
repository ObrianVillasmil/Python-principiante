from tkinter import Tk
from tkinter import Frame
from tkinter import PhotoImage
from tkinter import Label
from tkinter import Entry

class index():
	
	def __init__(self):
		self.root=Tk()
		self.root.title('Ventana con labels de entrada de informacion')
		self.root.iconbitmap('ico_escritorio.ico')


	def plantilla(self):
		frame = Frame(self.root)
		imagen = PhotoImage(file='Python.png')
		Label(frame, text='Bienvenidos').grid(row=1,column=1,pady=10,columnspan=4)
		Label(frame,image=imagen).grid(row=2,column=1,pady=30,padx=60,columnspan=4)
		Label(frame,text='Nombre:').grid(row=3,column=1,pady=20,sticky='e')
		Entry(frame).grid(row=3,column=2)
		Label(frame,text='Apellido:').grid(row=3,column=3,pady=20,sticky='e')
		Entry(frame).grid(row=3,column=4)

		frame.pack()
		frame.mainloop()

index =index()
index.plantilla()