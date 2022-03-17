class elemento():

    def __init__(self) -> None:
        self.tipo=None
        self.valor=None
        self.fondo=None
        self.valores=None
        self.eventos=None
        pass

    def __init__(self,tipo,valor) -> None:
        self.tipo=tipo
        self.valor=valor
        self.fondo=None
        self.valores=None
        self.evento=None
        pass

    def __init__(self,tipo,valor,fondo) -> None:
        self.tipo=tipo
        self.valor=valor
        self.fondo=fondo
        self.valores=None
        self.evento=None
        pass

    def __init__(self,tipo,valor,valores) -> None:
        self.tipo=tipo
        self.valor=valor
        self.fondo=None
        self.valores=valores
        self.evento=None
        pass

    def __init__(self,tipo,valor,evento) -> None:
        self.tipo=tipo
        self.valor=valor
        self.fondo=None
        self.valores=None
        self.evento=evento
        pass

    def __init__(self,tipo,valor,fondo,valores,evento) -> None:
        self.tipo=tipo
        self.valor=valor
        self.fondo=fondo
        self.valores=valores
        self.evento=evento
        pass