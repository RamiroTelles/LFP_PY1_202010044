from fileinput import filename


class token:

    def __init__(self,type,lexema,fila,columna):
        self.lexema = lexema
        self.type = type
        self.fila = fila
        self.columna = columna
