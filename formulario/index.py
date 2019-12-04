from tkinter import *

class index(object):
	
	def __init__(self):
		self.root=Tk()
		self.root.iconbitmap("formulario.ico")
		self.root.title("Formulario de datos")
		self.root.resizable(0,0)
		self.nombre=StringVar()
		self.apellido=StringVar()
		self.identificacion=IntVar()
		self.genero=IntVar()
		self.camioneta=StringVar()
		self.miniVans=StringVar()
		self.deportivo=StringVar()

	def diseno(self):
		frame = Frame(self.root,padx=50)
		Label(frame,text='Escriba sus datos personales',font=('arial',15)).grid(column=0,row=0,pady=20,columnspan=3)

		Label(frame,text='Nombre').grid(column=0,row=1,sticky='w')
		Entry(frame,textvariable=self.nombre).grid(column=0,row=2,padx=2,pady=5)

		Label(frame,text='Apellido').grid(column=1,row=1,sticky='w')
		Entry(frame,textvariable=self.apellido).grid(column=1,row=2,padx=2,pady=5)

		Label(frame,text='Identificación').grid(column=2,row=1,sticky='w')
		Entry(frame,textvariable=self.identificacion).grid(column=2,row=2,padx=2,pady=5)

		Label(frame,text='Seleccione su género',font=('arial',15)).grid(column=0,row=3,pady=20,columnspan=3)

		Radiobutton(frame,text='Masculino',variable=self.genero, value=1).grid(column=0,row=4)
		Radiobutton(frame,text='Femenino',variable=self.genero, value=2).grid(column=1,row=4)
		Radiobutton(frame,text='Otros',variable=self.genero, value=3).grid(column=2,row=4)

		Label(frame,text='Escoga sus vehículos preferidos',font=('arial',15)).grid(column=0,row=5,pady=20,columnspan=3)
		
		Checkbutton(frame,text='Camioneta 4x4',variable=self.camioneta,onvalue='Camioneta 4x4',offvalue='').grid(column=0,row=6)
		Checkbutton(frame,text='Mini Vans',variable=self.miniVans,onvalue='Mini Vans',offvalue='').grid(column=1,row=6)
		Checkbutton(frame,text='Deportivo',variable=self.deportivo,onvalue='Deportivo',offvalue='').grid(column=2,row=6)

		Label(frame,text='Escribe un comentario',font=('arial',15)).grid(column=0,row=7,pady=20,columnspan=3)

		text = Text(frame,width=45,height=5).grid(column=0,row=8,pady=('5','10'),columnspan=3)
		scrollBar= Scrollbar(frame,command=text.yview).grid(column=3,row=8,sticky='nsew')
		#text.config(yscrollcommand=text.set)


		frame.pack()
		frame.mainloop()



index =index()
index.diseno()