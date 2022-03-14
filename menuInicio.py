from tkinter import *

from interfazAreaTexto import interfazAreaTexto

class menu():

    def __init__(self) -> None:

        def abrirAreaTexto():
        #crear objeto de la ventana area texto
            interfazAreaTexto()

            pass

        ventana = Tk()

        ventana.title("Menu")

        ventana.geometry("230x180")
        ventana.config(bg="#00E7CE")

        l_inicio = Label(ventana,text="Seleccione que opcion desea",bg="#00E7CE")
        botonCargar = Button(ventana, text="Cargar Archivo lfp")

        b_text = Button(ventana,text="Ir a Area de Texto", command= abrirAreaTexto)

        l_inicio.place(x=40,y=20)

        botonCargar.place(x=60, y=70)

        b_text.place(x=63, y=120)



        ventana.mainloop()
        pass


    

    def cargarArchivo():
        #poner lo de cargar archivos de la prac 1
        pass





