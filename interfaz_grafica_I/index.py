from tkinter import *

#Inicialimos la clase Tk de tkinter
raiz = Tk()

#Le damos un titulo a la ventana actual
raiz.title("Primera ventana")

#Le agregamos un icono a la ventana
raiz.iconbitmap("icono.ico")

#Podemos ajustable el tamano de la ventana con el mause en X y Y
raiz.resizable(True,False)

#Podemos darle un tamano especifco (en pixeles) a la raiz (Marco) de la ventana
raiz.geometry("500x300")

#podemos darle un color de fondo a la raiz (Marco)
raiz.config(bg="red")

#el metodo mainLoop() siempre tiene que quedar de ultimo para que la ventana quede siempre a la escucha de los eventos
raiz.mainloop()
