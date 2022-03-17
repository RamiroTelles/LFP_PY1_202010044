
from tkinter.messagebox import NO
from wsgiref.validate import validator
from pyparsing import col
from Eltoken import token
from tkinter import N, Tk
from tkinter.filedialog import askopenfilename
from elemento import elemento
from generadorForm import generadorForm
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
                    tokens.append(token(tokentype.corcheteAbre,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual== '<':
                    lexema+=actual
                    tokens.append(token(tokentype.objetoAbre,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual == ':':
                    lexema+=actual
                    tokens.append(token(tokentype.dosPuntos,lexema,fila,columna))
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
                    tokens.append(token(tokentype.coma,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=='>':
                    lexema+=actual
                    tokens.append(token(tokentype.objetoCierre,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual==']':
                    lexema+=actual
                    tokens.append(token(tokentype.corcheteCierre,lexema,fila,columna))
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
                    tokens.append(token(tokentype.Letras,lexema,fila,columna))
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
                    tokens.append(token(tokentype.Entrada,lexema,fila,columna))
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
                    tokens.append(token(tokentype.Cadena,lexema,fila,columna))
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
                    tokens.append(token(tokentype.Cadena,lexema,fila,columna))
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
                    errores+="Error, Se esperaba la palabra reservada Formulario en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
                    break
            if estado==1:
                if actual.type == tokentype.Entrada:
                    estado=2
                    continue
                else:
                    errores+="Error, Se esperava la palabra reservada ~>> en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
                    break
            if estado==2:
                if actual.type == tokentype.corcheteAbre:
                    estado=3
                    continue
                else:
                    errores+="Error, Se esperaba un [ en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
                    break
            if estado==3:
                if actual.type == tokentype.objetoAbre:
                    estado=4
                    continue
                else:
                    errores+="Error, Se esperaba un < en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
                    break
            if estado ==4:
                if actual.type == tokentype.Letras:
                    identificador = actual.lexema
                    estado=41
                    continue
                else:
                    errores+="Error, Esperaba un identificador en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
                    break
            if estado == 41:
                if actual.type == tokentype.dosPuntos:
                    estado=5
                    continue
                else:
                    errores+="Error, Esperaba un : en la fila "+ str(actual.fila) + " y columna " + str(actual.columna)
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
                    elif identificador.upper() == "NOMBRE":

                        valor = actual.lexema[1:-1]
                        estado=6
                        continue
                    elif identificador.upper() == "FONDO":
                        fondo = actual.lexema[1:-1]
                        estado=6
                        continue
                    else:
                        errores+="Error, la palabra " + identificador + " no coincide con niguna palabra reservada en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
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
                    errores+= "Se esperaba un , o un > en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
                    break
            if estado == 7:
                if actual.type == tokentype.coma:
                    estado=3
                    continue
                elif actual.type == tokentype.corcheteCierre:
                    print("Fin analisis lexico")
                    break
                else:
                    errores+="Se esperaba un ] o un , en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
                    break
            if estado == 9:
                if actual.type == tokentype.Cadena:
                    valores.append(actual.lexema[1:-1])
                    estado=10
                    continue
                else:
                    errores+="Se esperaba una cadena en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
                    break
            if estado==10:
                if actual.type == tokentype.coma:
                    estado=9
                    continue
                elif actual.type == tokentype.corcheteCierre:
                    estado=6
                    continue
                else:
                    errores+="Se esperaba un , o un ] en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
                    break
            if estado ==11:
                if actual.type == tokentype.Letras:
                    evento=actual.lexema
                    estado=12
                    continue
                else:
                    errores+="Error, Se esperaba una palabra en la fila: "+ str(actual.fila) + "y columna: " + str(actual.columna)
                    break
            if estado==12:
                if actual.type== tokentype.objetoCierre:
                    estado=6
                    continue

        resultados=[]
        resultados.append(elementos)
        resultados.append(errores)
        return resultados
        pass

    def analSemantico(self,elementos,entrada):
        form = generadorForm()
        errores=""
        for obj in elementos:
            if obj.tipo.upper() == "ETIQUETA":
                #Crear el label en el html
                form.agregarLabel(obj)
                #agarrar solo valor
                continue
            elif obj.tipo.upper() == "TEXTO":
                #Crear textbox en el html
                form.agregarText(obj)
                #agarrar valor y fondo
                continue
            elif obj.tipo.upper() == "GRUPO-RADIO":
                #Crear grupo radio en html
                form.agregarRadio(obj)
                #agarrar valor y valores
                continue
            elif obj.tipo.upper() == "GRUPO-OPTION":
                #Crear grupo radio en html
                form.agregarCombo(obj)
                #agarrar valor y valores
                continue
            elif obj.tipo.upper() == "BOTON":
                #Crear boton en html
                form.agregarBoton(obj)
                #agarrar valor y evento
                continue
            else:
                errores+="el elemento "+ obj.tipo + "no se reconoce"
                continue
        form.cerrarForm(entrada)

        try:


            with open("dynamicForm.html",'w') as file:
                file.write(form.form)

                file.close()
        
        except:
            print("No se pudo generar el form")

        try:


            with open("fun.js",'w') as file:
                file.write(form.js)

                file.close()
        
        except:
            print("No se pudo generar el js del form")
        
        resultados=[]
        resultados.append(form.form)
        resultados.append(form.js)
        resultados.append(errores)
        return resultados
        

    def reporteTokens(self,tokens):
        txt = '''
<html>
    <head>

    </head>
    <link rel="stylesheet" href="estilo.css">

<body>
    <div class="container">
        <table>
            <thead>
                <tr>
                    <th>Tipo token</th>
                    <th>Lexema</th>
                    <th>Fila</th>
                    <th>Columna</th>
                </tr>
            </thead>
<tbody>'''
        for obj in tokens:

            if obj.type == tokentype.Letras:

                txt+= "<tr> <th> Letras:1001</th>\n"
            elif obj.type == tokentype.Entrada:

                txt+= "<tr> <th> Entrada:1002</th>\n"
            elif obj.type == tokentype.corcheteAbre:

                txt+= "<tr> <th> corcheteAbre:1003</th>\n"
            elif obj.type == tokentype.objetoAbre:

                txt+= "<tr> <th> objetoAbre:1004</th>\n"
            elif obj.type == tokentype.dosPuntos:

                txt+= "<tr> <th> dosPuntos:1005</th>\n"
            elif obj.type == tokentype.Cadena:

                txt+= "<tr> <th> Cadena:1006</th>\n"
            elif obj.type == tokentype.coma:

                txt+= "<tr> <th> coma:1007</th>\n"
            elif obj.type == tokentype.objetoCierre:

                txt+= "<tr> <th> objetoCierre:1008</th>\n"
            elif obj.type == tokentype.corcheteCierre:

                txt+= "<tr> <th> corcheteCierre:1009</th>\n"
            
            
            txt+="<th> "+ str(obj.lexema)+ "</th>\n"
            txt+="<th> "+ str(obj.fila)+ "</th>\n"
            txt+="<th> "+ str(obj.columna)+ "</th>\n"
            
            txt+="</tr>"
        txt+='''
            </tbody>
        </table>
</div>
    

</body>
</html>
        '''
        try:


            with open("ReporteTokens.html",'w') as file:
                file.write(txt)

                file.close()
        
        except:
            print("No se pudo generar el reporte")
        pass

    def reporteErrores(self,erroreslexicos,erroresSintacticos,erroresSemanticos):
        filas = erroreslexicos.split('\n')
        

        txt = '''
    <html>
        <head>

        </head>
        <link rel="stylesheet" href="estilo.css">

    <body>
        <div class="container">
            <table>
                <thead>
                    <tr>
                        <th>Errores lexicos</th>
                        
                    </tr>
                </thead>
    <tbody>'''
        for obj in filas:
                    
            txt+= "<tr> <th> "+ obj + "</th>\n"
        
            txt+="</tr>"
        
        txt+= '''
            </tbody>
        </table>
        <hr>
        <hr>
        <table>
            <thead>
                <tr>
                    <th>
                        Errores Sintacticos
                    </th>
                </tr>
            </thead>
            <tbody>

            '''
        filas = erroresSintacticos.split('\n')
        for obj in filas:
                    
            txt+= "<tr> <th> "+ obj + "</th>\n"
        
            txt+="</tr>"
        txt+= '''
            </tbody>
        </table>
        <hr>
        <hr>
        <table>
            <thead>
                <tr>
                    <th>
                        Errores Semanticos
                    </th>
                </tr>
            </thead>
            <tbody>

            '''
        filas = erroresSemanticos.split('\n')
        for obj in filas:
                    
            txt+= "<tr> <th> "+ obj + "</th>\n"
        
            txt+="</tr>"

        txt+='''
                </tbody>
            </table>
    </div>
        

    </body>
    </html>
            '''
        try:


            with open("ReporteErrores.html",'w') as file:
                file.write(txt)

                file.close()
            
        except:
            print("No se pudo generar el reporte")