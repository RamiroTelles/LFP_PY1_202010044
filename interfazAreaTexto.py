from itertools import tee
from sqlite3 import adapt
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from turtle import width
from typing import TextIO
from tkinter import ttk
from click import style

#from matplotlib.pyplot import text

class interfazAreaTexto():

    def __init__(self) -> None:
        ventana = Tk()

        ventana.geometry("800x600")
        ventana.config(bg="#00E7CE")
        ventana.resizable(False,False)

        #b_volver = Button(ventana,text="volver")

        b_analizar = Button(ventana,text="Analizar")

        b_reporte = Button(ventana,text="Generar Reportes")
        b_Cargar = Button(ventana, text="Cargar Archivo lfp")
         

        b_Cargar.place(x=30,y=15)

        b_analizar.place(x=50,y=540)

        b_reporte.place(x=520,y=45)

        t_editor = ScrolledText(ventana,width=91,height=28)
        #ScrolVer = Scrollbar(ventana, command=t_editor.yview)
        cajaCombo = ttk.Combobox(ventana,values=["Generar Reporte Tokens","Generar Reporte Errores","Manual de Usuario","Manual Técnico"],state="readonly")
        
        t_editor.place(x=30,y=80)
        cajaCombo.place(x=630,y=45)
        cajaCombo.current(0)

        #ScrolVer.place(x=760,y=80)
        

        ventana.mainloop()
        pass