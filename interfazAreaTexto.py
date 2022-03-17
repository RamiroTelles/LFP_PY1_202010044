from itertools import tee
from sqlite3 import adapt
from tkinter import *

from tkinter.scrolledtext import ScrolledText
from turtle import width
from typing import TextIO
from tkinter import ttk
from click import style
from analizador import analizador
from os import startfile

#from matplotlib.pyplot import text

class interfazAreaTexto():

    
    def __init__(self) -> None:
        self.funciones = analizador()
      
        
        def cargarArchivo():
            texto=self.funciones.cargarArchivo()
            t_editor.delete("1.0","end")
            t_editor.insert("1.0",texto)
            pass
        
        def analizar():
            texto =t_editor.get("1.0","end")
            #print(texto)
            result1= self.funciones.analizadorLexico(texto)
          
            
            result2 = self.funciones.analSintactico(result1[0])

            result3 = self.funciones.analSemantico(result2[0],texto)
     

            self.funciones.reporteTokens(result1[0])
            self.funciones.reporteErrores(result1[1],result2[1],result3[2])
            startfile("dynamicForm.html")
            pass

        def generarReporte():

            opcion = cajaCombo.get()

            
            if opcion=="Generar Reporte Tokens":
                startfile("ReporteTokens.html")
            elif opcion== "Generar Reporte Errores":
                startfile("ReporteErrores.html")
            elif opcion=="Manual de Usuario":
                startfile("ManualDeUsuario.pdf")
            elif opcion=="Manual Técnico":
                startfile("ManualTecnico.pdf")
            pass
        ventana = Tk()

        ventana.geometry("800x600")
        ventana.config(bg="#00E7CE")
        ventana.resizable(False,False)

        #b_volver = Button(ventana,text="volver")

        b_analizar = Button(ventana,text="Analizar", command=analizar)

        b_reporte = Button(ventana,text="Generar Reportes", command=generarReporte)
        b_Cargar = Button(ventana, text="Cargar Archivo form", command=cargarArchivo)
         

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