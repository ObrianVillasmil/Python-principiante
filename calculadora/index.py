from tkinter import *
from package.operaciones.index import operaciones

class index(operaciones):

	def __init__(self):
		self.root=Tk()
		self.root.iconbitmap('ico_escritorio.ico')
		self.root.resizable(0,0)
		self.root.title('Calculadora')
		self.numero = StringVar()
		self.accionado=False
		self.cadena=StringVar()
		self.num1=0
		self.num2=0
		self.acc= '';

	def num(self,val):
		
		accion = self.accion(val)
		if(accion['ope']):

			self.accionado=True

			if(val=="√"):
				self.acc = accion['op']
				self.num1=self.numero.get()
				self.num2=0
			
			if(self.num1!=0):
				res = self.operacion(self.acc,self.num1,self.num2)
				self.num1=res
				self.numero.set(res)
				
			else:
				self.num1=self.numero.get()
					
			self.acc = accion['op']
			if(val=="√"):
				self.acc = ''
				self.num1=0
		else:
			if(self.accionado):
				self.numero.set("")
				self.numero.set(self.numero.get()+val)
				self.accionado=False
			else:
				self.numero.set(self.numero.get()+val)

			self.num2=self.numero.get()
		
		self.cadena.set(self.cadena.get()+val)


	def resultado(self):
		res = self.operacion(self.acc,self.num1,self.numero.get())
		self.numero.set(res)
		

	def diseno(self):
		
		self.frame= Frame(self.root,pady=35,padx=55)	
		Entry(self.frame,bg='black',fg='white',width=20,justify='right',textvariable=self.cadena).grid(row='0',column='1',padx=5,columnspan=4)
		Entry(self.frame,bg='black',fg='white',width=20,justify='right',textvariable=self.numero).grid(row='1',column='1',padx=5,columnspan=4)

		#-------- FILA 1--------------
		Button(self.frame,text='C',width=3,command=lambda:self.borrar(self.numero,self.cadena)).grid(row='2',column='1')
		Button(self.frame,text='%',width=3).grid(row='2',column='2')
		Button(self.frame,text='x2',width=3,command=lambda:self.num("x2")).grid(row='2',column='3')
		Button(self.frame,text='√',width=3,command=lambda:self.num("√")).grid(row='2',column='4')

		#-------- FILA 2--------------
		Button(self.frame,text='7',width=3,command=lambda:self.num("7")).grid(row='3',column='1')
		Button(self.frame,text='8',width=3,command=lambda:self.num("8")).grid(row='3',column='2')
		Button(self.frame,text='9',width=3,command=lambda:self.num("9")).grid(row='3',column='3')
		Button(self.frame,text='/',width=3,command=lambda:self.num("/")).grid(row='3',column='4')

		#-------- FILA 3--------------
		Button(self.frame,text='4',width=3,command=lambda:self.num("4")).grid(row='4',column='1')
		Button(self.frame,text='5',width=3,command=lambda:self.num("5")).grid(row='4',column='2')
		Button(self.frame,text='6',width=3,command=lambda:self.num("6")).grid(row='4',column='3')
		Button(self.frame,text='X',width=3,command=lambda:self.num('X')).grid(row='4',column='4')

		#-------- FILA 4--------------
		Button(self.frame,text='1',width=3,command=lambda:self.num("1")).grid(row='5',column='1')
		Button(self.frame,text='2',width=3,command=lambda:self.num("2")).grid(row='5',column='2')
		Button(self.frame,text='3',width=3,command=lambda:self.num("3")).grid(row='5',column='3')
		Button(self.frame,text='+',width=3,command=lambda:self.num("+")).grid(row='5',column='4')


		#-------- FILA 5--------------
		Button(self.frame,text='0',width=3,command=lambda:self.num("0")).grid(row='6',column='1')
		Button(self.frame,text='=',width=3,command=lambda:self.resultado()).grid(row='6',column='4')
		Button(self.frame,text='-',width=3,command=lambda:self.num("-")).grid(row='6',column='3')
		Button(self.frame,text=',',width=3,command=lambda:self.num(",")).grid(row='6',column='2')
		self.frame.pack()
		self.frame.mainloop()

	

index =index()
index.diseno()
