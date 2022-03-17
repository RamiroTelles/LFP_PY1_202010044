import imp
from unittest import result
from menuInicio import menu
from interfazAreaTexto import interfazAreaTexto
from analizador import analizador
from os import startfile
from os import system

#funciones = analizador()

#texto = funciones.cargarArchivo()
#resul1= funciones.analizadorLexico(texto)
#print("-----------------------------------------")
#print(resul1[1])
#print("-----------------------------------------")


interfazAreaTexto()

#texto='''formulario ~>>[
#    <
#        tipo:"etiqueta",
#        valor:"Nombre:"
#    >,
#    
#    <
#        tipo:"texto",
#        valor: "nombre",
#        fondo:"Ingrese Nombre"
#    >,
#    
#    <
#        tipo: "grupo-radio",
#        nombre: "sexo",
#        valores: ['Masculino','Femenino']
#    >,
#    <
#        tipo: "grupo-option",
#        nombre: "pais",
#        valores: ['Guatemala','El salvador','Honduras']
#    >,
#    <
#        tipo:"boton",
#        valor: "Valor",
#        evento: <entrada>
#    >
#]
#'''
#cadena=""
#for caracter in texto:
#    if caracter=="\"":
#        cadena+="\\"
#        cadena+= caracter
#    elif caracter=="\'":
#        cadena+="\\"
#        cadena+= caracter
#    elif caracter=="\n":
#        cadena+="\\n"
#    else:
#        cadena+=caracter

#print(cadena)

    

#menu()
#print("-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_--")
#for obj in resul1[0]:
#    print(obj.type)
#    print(obj.lexema)
#    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_--")

#resul2= funciones.analSintactico(resul1[0])

#resul3 = funciones.analSemantico(resul2[0],texto)

#startfile("dynamicForm.html")

#funciones.reporteTokens(resul1[0])
#funciones.reporteErrores(resul1[1],resul2[1],resul3[2])

#startfile("ReporteTokens.html")
#startfile("ReporteErrores.html")

#print("-----------------------------------------")
#print(resul2[1])
#print("-----------------------------------------")

#print("-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_--")
#for obj in resul2[0]:
#    print(obj.tipo)
#    print(obj.valor)
#    print(obj.fondo)
#    print(obj.valores)
#    print(obj.evento)
#    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_--")



