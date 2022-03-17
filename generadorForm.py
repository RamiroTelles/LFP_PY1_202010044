from matplotlib.pyplot import text


class generadorForm():
    
    def __init__(self) -> None:
        self.cantLabels=0
        self.cantText=0
        self.cantRadio=0
        self.cantCombo=0
        self.cantBoton=0
        self.info="let info = "
        self.js="function INFO(){ \n"

        self.form = '''
        <!DOCTYPE html>
<html>
    <header>

        <link href="style.css" rel="stylesheet" type="text/css">

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    </header>
<body>
    <div style="height: 100%;">

        <div id="mod1" class="login">
        '''
        
        pass

    def agregarLabel(self,elemento):
        self.cantLabels+=1
        self.form += "<h4 style=\"color: white;\"> "+ elemento.valor + "</h4>\n"
        pass

    def agregarText(self,elemento):
        
        self.form+="<input type=\"text\" class=\"buttonLogin\" placeholder="+ elemento.fondo + " id=\"t" + str(self.cantText) + "\"/>\n"
        self.agregarTextJs()
        self.agregarTextinfo()
        self.cantText+=1

    def agregarRadio(self,elemento):
        self.form+="<b style=\"color: rgb(255, 255, 255);\" >"+elemento.valor+"</b>\n"

        for obj in elemento.valores:
            self.form+="<input type=\"radio\" value=\""+obj+"\" id=\"g"+str(self.cantRadio)+"\" name=\"g"+str(self.cantRadio)+"\"/> <b style=\"color: white;\">"+obj+"</b>\n"
        self.form+="<br>\n"
        self.agregarRadioJs()
        self.agregarRadioinfo()
        self.cantRadio+=1
    
    def agregarCombo(self,elemento):
        self.form+="<b style=\"color: rgb(255, 255, 255);\" >"+ elemento.valor+"</b> \n"

        self.form+="<select name=\"c"+str(self.cantCombo)+"\" id=\"c"+str(self.cantCombo)+"\">\n"

        for obj in elemento.valores:
            self.form+="<option value=\""+str(obj)+"\">"+obj+"</option>\n"
        self.form+="</select>\n"
        self.agregarComboJs()
        self.agregarComboinfo()
        self.form+="<br>\n"
        self.cantCombo+=1

    def agregarBoton(self,elemento):
        self.form+="<button type=\"button\" class=\"btn btn-primary btn-block btn-large\" onclick=\""+elemento.evento.upper()+"()\">"+elemento.valor+"</button>\n"
        self.form+="<br>\n"

    def cerrarForm(self,entrada):
        self.form+='''
        </div>


    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <script src="fun.js"></script>
</body>
</html>
        '''
        self.unirInfo()
        self.FuncionEntrada(entrada)
        
    
    def agregarTextJs(self):
        self.js+= "let t"+ str(self.cantText)+" = document.getElementById(\"t"+ str(self.cantText) +"\").value;\n"

    def agregarRadioJs(self):
        self.js+= "let g"+ str(self.cantRadio)+" = document.querySelector('input[name=\"g"+str(self.cantRadio)+"\"]:checked').value; \n"

    def agregarComboJs(self):
        self.js+= "let c"+str(self.cantCombo)+" = document.getElementById(\"c"+str(self.cantCombo)+"\").value;\n"
    
    #def unirInfo(self):
    #    self.js+="let info = "

       # for i in range(self.cantText):
        #    self.js+="t" + str(i)+" + \"\\n\" +"
        
        #for i in range(self.cantRadio):
         #   self.js+="g"+str(i)+" + \"\\n\" +"

        #for i in range(self.cantCombo):
         #   self.js+="c"+str(i)+" + \"\\n\" +"
        
        #self.js+="\"\" \n"

        #self.js+="alert(info); \n"
        #self.js+="}\n"

    def unirInfo(self):

        self.info+="\"\" \n"
        self.js+= self.info
        self.js+="alert(info); \n"
        self.js+="}\n"


        pass

    def agregarTextinfo(self):
        self.info+= "t"+str(self.cantText)+" + \"\\n\" +"
        pass

    def agregarRadioinfo(self):
        self.info+= "g"+str(self.cantRadio)+" + \"\\n\" +"
        pass

    def agregarComboinfo(self):
        self.info+= "c"+str(self.cantCombo)+" + \"\\n\" +"
        pass

    def FuncionEntrada(self,texto):
        cadena=""
        for caracter in texto:
            if caracter=="\"":
                cadena+="\\"
                cadena+= caracter
            elif caracter=="\'":
                cadena+="\\"
                cadena+= caracter
            elif caracter=="\n":
                cadena+="\\n"
            else:
                cadena+=caracter

        self.js+="function ENTRADA(){ \n"
        self.js+="let info = \"" + cadena + "\" \n"
        self.js+="alert(info)\n"
        self.js+="}\n"
        pass

