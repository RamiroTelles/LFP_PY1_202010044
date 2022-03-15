
from Eltoken import token
from tkinter import Tk
from tkinter.filedialog import askopenfilename


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
                    print("Simbolo " + actual + " no reconocido")
                    errores+= "Simbolo "+ actual + " no reconocido en columna: "+ str(columna) + " fila: "+ str(fila)+ "\n"
                    break
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
                    print("Error, Se esperaba una >")
                    errores+="Se esperaba una > en la columna: "+ str(columna) + ". fila "+ str(fila)+ "\n"
                    break
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
                    print("Error, Se esperaba una >")
                    errores+="Se esperaba una > en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
                    break
            elif estado == 6 :
                if actual=="\"":
                    estado=0
                    lexema+=actual
                    tokens.append(token(tokentype.Cadena,lexema))
                    lexema=""
                    i+=1
                    columna+=1
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
                else:
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
        if estado==6 or estado == 12:
            print("Se esperaba un \" o un \' para finalizar la cadena")
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

        
            