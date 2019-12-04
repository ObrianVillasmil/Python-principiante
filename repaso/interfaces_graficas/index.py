from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import PhotoImage

class index():

	def marco(self):
		marco = Tk()
		marco.title("Ventana de escrito de repaso")
		marco.iconbitmap('ico_escritorio.ico')	
		marco.config(bg="red")	
		
	def plantilla(self):
		m = self.marco()
		cantidad = int(input('ingrese la cantidad de labels a crear: '))
		plantilla=Frame(m,width='350',height ='500')
		imagen = PhotoImage(file='Python.png')
		Label(plantilla,image=imagen).place(x=1,y=1)
		plantilla.pack(fill='y',expand='True')
		
		for z in range(0,cantidad):
			texto = input('Escribe el texto del label '+str(z)+ ': ')
			x = int(input('Escribe el eje x del texto del label '+str(z)+ ': '))
			y = int(input('Escribe el eje y del texto del label '+str(z)+ ': '))
			Label(plantilla,text=texto).place(x=x,y=y)
		plantilla.config(bg='blue')
		plantilla.mainloop()

	def imagen(self):
		marco = self.marco()
		frame = Frame(marco,width='350',height ='500')
		frame.pack()
		imagen = PhotoImage(file='Python.gif')
		label =Label(marco,image=imagen).place(x=1,y=1)
		frame.mainloop()
	

index = index()
#index.imagen()
index.plantilla()

