
from tkinter.messagebox import NO
from wsgiref.validate import validator
from pyparsing import col
from Eltoken import token
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from elemento import elemento

from tokentype import tokentype


class analizador():

    def __init__(self) -> None:
        pass

    def analizadorLexico(self,texto):
        estado=0
        lexema=""
        columna=1
        fila=1
        errores=""
        tokens= []
        i=0
        actual=""
        long = len(texto)
        while(i<long and texto[i]!=None):
            actual=texto[i]

            if estado==0:
                if actual.isalpha():
                    lexema+=actual
                    estado=1
                    i+=1
                    columna+=1
                    continue
                elif actual == '~':
                    lexema+=actual
                    estado=2
                    i+=1
                    columna+=1
                    continue
                elif actual == '[':
                    lexema+= actual
                    tokens.append(token(tokentype.corcheteAbre,lexema))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual== '<':
                    lexema+=actual
                    tokens.append(token(tokentype.objetoAbre,lexema))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual == ':':
                    lexema+=actual
                    tokens.append(token(tokentype.dosPuntos,lexema))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=='\"':
                    lexema+=actual
                    estado= 6
                    i+=1
                    columna+=1
                    continue
                elif actual=='\'':
                    lexema+=actual
                    estado= 12
                    i+=1
                    columna+=1
                    continue
                elif actual==',':
                    lexema+=actual
                    tokens.append(token(tokentype.coma,lexema))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=='>':
                    lexema+=actual
                    tokens.append(token(tokentype.objetoCierre,lexema))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual==']':
                    lexema+=actual
                    tokens.append(token(tokentype.corcheteCierre,lexema))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=='\n':
                    fila+=1
                    i+=1
                    columna=1
                    continue
                elif actual=='\t' or actual=='\r' or actual==' ':
                    i+=1
                    columna+=1
                    continue
                else:
                    #print("Simbolo " + actual + " no reconocido")
                    errores+= "Simbolo "+ actual + " no reconocido en columna: "+ str(columna) + " fila: "+ str(fila)+ "\n"
                    i+=1
                    columna+=1
                    continue
            elif estado==1:
                if actual.isalpha():
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    tokens.append(token(tokentype.Letras,lexema))
                    lexema=""
                    estado=0
                    continue
            elif estado==2:
                if actual=='>':
                    estado=10
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    #print("Error, Se esperaba una >")
                    errores+="Se esperaba una > en la columna: "+ str(columna) + ". fila "+ str(fila)+ "\n"
                    estado=0
                    continue
            elif estado==10:
                if actual=='>':
                    lexema+=actual
                    tokens.append(token(tokentype.Entrada,lexema))
                    lexema=""
                    estado=0
                    i+=1
                    columna+=1
                    continue
                else:
                    #print("Error, Se esperaba una >")
                    errores+="Se esperaba una > en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
                    estado=0
                    continue
            elif estado == 6 :
                if actual=="\"":
                    estado=0
                    lexema+=actual
                    tokens.append(token(tokentype.Cadena,lexema))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=="\n":
                    lexema+=actual
                    i+=1
                    columna=1
                    fila+=1
                    continue
                else:
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
            elif estado == 12 :
                if actual=="\'":
                    estado=0
                    lexema+=actual
                    tokens.append(token(tokentype.Cadena,lexema))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=="\n":
                    lexema+=actual
                    i+=1
                    columna=1
                    fila+=1
                    continue
                else:
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
        if estado==6 or estado == 12:
            #print("Se esperaba un \" o un \' para finalizar la cadena")
            errores+="Se esperaba un \" o un \' para finalizar la cadena"
        resultados = []
        resultados.append(tokens)
        resultados.append(errores)
        return resultados

    def cargarArchivo(self):
        Tk().withdraw()

        try:
            path = askopenfilename(filetypes=[('.form','*.form'),('*.*','*.*')])
            

            with open(path,encoding='utf-8') as file:
                txt = file.read().strip()
                file.close()
        except:
            print("Error")

        
        
        return str(txt)

        
    def analSintactico(self,tokens):
        estado=0
        identificador=""
        errores=""
        tipo=None
        valor=None
        fondo=None
        valores=[]
        evento=None
        elementos=[]

        for actual in tokens:
            if estado==0:
                if actual.lexema.upper() == "FORMULARIO":
                    estado=1
                    continue
                else:
                    errores+="Error, Se esperaba la palabra reservada Formulario"
                    break
            if estado==1:
                if actual.type == tokentype.Entrada:
                    estado=2
                    continue
                else:
                    errores+="Error, Se esperava la palabra reservada ~>>"
                    break
            if estado==2:
                if actual.type == tokentype.corcheteAbre:
                    estado=3
                    continue
                else:
                    errores+="Error, Se esperaba un ["
                    break
            if estado==3:
                if actual.type == tokentype.objetoAbre:
                    estado=4
                    continue
                else:
                    errores+="Error, Se esperaba un <"
                    break
            if estado ==4:
                if actual.type == tokentype.Letras:
                    identificador = actual.lexema
                    estado=41
                    continue
                else:
                    errores+="Error, Esperaba un identificador"
                    break
            if estado == 41:
                if actual.type == tokentype.dosPuntos:
                    estado=5
                    continue
                else:
                    errores+="Error, Esperaba un :"
                    break
            if estado==5:
                if actual.type == tokentype.Cadena:
                    if identificador.upper() == "TIPO":
                        tipo= actual.lexema[1:-1]
                        estado=6
                        continue
                    elif identificador.upper() == "VALOR":

                        valor = actual.lexema[1:-1]
                        estado=6
                        continue
                    elif identificador.upper() == "FONDO":
                        fondo = actual.lexema[1:-1]
                        estado=6
                        continue
                    else:
                        errores+="Error, la palabra " + identificador + " no coincide con niguna palabra reservada"
                        break
                elif actual.type == tokentype.corcheteAbre:
                    estado=9
                    continue
                elif actual.type == tokentype.objetoAbre:
                    estado=11
                    continue
            if estado==6:
                if actual.type == tokentype.coma:
                    estado =4
                    continue
                elif actual.type == tokentype.objetoCierre:
                    #creo el objeto elemento del form
                    elementos.append(elemento(tipo, valor,fondo,valores,evento))
                    tipo=None
                    valor=None
                    fondo=None
                    valores=[]
                    evento=None
                    estado=7
                    continue
                else:
                    errores+= "Se esperaba un , o un >"
                    break
            if estado == 7:
                if actual.type == tokentype.coma:
                    estado=3
                    continue
                elif actual.type == tokentype.corcheteCierre:
                    print("Fin analisis lexico")
                    break
                else:
                    errores+="Se esperaba un ] o un ,"
                    break
            if estado == 9:
                if actual.type == tokentype.Cadena:
                    valores.append(actual.lexema[1:-1])
                    estado=10
                    continue
                else:
                    errores+="Se esperaba una cadena"
                    break
            if estado==10:
                if actual.type == tokentype.coma:
                    estado=9
                    continue
                elif actual.type == tokentype.corcheteCierre:
                    estado=6
                    continue
                else:
                    errores+="Se esperaba un , o un ]"
                    break
            if estado ==11:
                if actual.type == tokentype.Letras:
                    evento=actual.lexema
                    estado=12
                    continue
                else:
                    errores+="Error, Se esperaba una palabra"
            if estado==12:
                if actual.type== tokentype.objetoCierre:
                    estado=6
                    continue

        resultados=[]
        resultados.append(elementos)
        resultados.append(errores)
        return resultados
        pass
