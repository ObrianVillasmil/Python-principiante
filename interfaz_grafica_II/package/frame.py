from tkinter import Frame

class frame():
	frame =""
	def crearFrame(self):
		self.frame = Frame()
		self.frame.pack()
		self.frame.config(bg="red")
		self.frame.config(width="500", height="400")