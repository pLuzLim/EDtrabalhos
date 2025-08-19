class fracao:

    num = 1
    den = 1 #padrão em caso que tentarem digitar 0 ou algo inválido
    
    def __init__(self, nume, deno): #inicializar, tem checks para a fração ser apropriamente positiva se ambos os elementos forem negativos
        self.num = nume
        if (deno == 0):
            print("Denominador inválido!")
        else:
            self.den = deno
        if (nume < 0 and deno < 0):
            self.num = abs(nume)
            self.den = abs(deno)

    def getnum(self): #getters
        return fracao.num
    
    def getden(self):
        return fracao.den

    def setnum(self, novnum: int): #setters, ambas tem o mesmo check do inicializador
        if(novnum < 0 and self.den < 0):
           self.num = abs(novnum)
           self.den = abs(self.den)
        else:
            self.num = novnum

    def setden(self, novden: int):
        if (novden == 0):
            print("Inválido, valor base atribuído")
        else:
            if(novden < 0 and self.num < 0):
                self.den = abs(novden)
                self.num = abs(self.num)
            else:
                self.den = novden


    def __str__(self): #para printar, mostra o - antes da fração se for negativo
        if ((self.num < 0 and self.den > 0) or (self.num > 0 and self.den < 0)):
            return "-" + str(abs(self.num)) + "/" + str(abs(self.den))
        elif(self.num == 0):
            return "0"
        else:
            return str(self.num) + "/" + str(self.den)
    
    def mdc(numer, deno): #mdc para simplificar
        if (numer % deno == 0):
            return deno
        else:
            return fracao.mdc(deno, (numer % deno)) 

    def simpl(self): #simplifica a fração
        fracmdc = fracao.mdc(self.num, self.den)
        self.num //= fracmdc
        self.den //= fracmdc

    #operadores
    def __add__(self, frac):
        if(self.den != frac.den):
            resnum = (self.num * frac.den) + (frac.num * self.den)
            resden = self.den * frac.den
        else:
            resnum = self.num + frac.num
            resden = self.den
        if(resnum == 0):
            return 0
        else: 
            somfrac = fracao(resnum, resden)
            return somfrac

    def __sub__(self, frac):
        if(self.den != frac.den):
            resnum = (self.num * frac.den) - (frac.num * self.den)
            resden = self.den * frac.den
        else:
            resnum = self.num - frac.num
            resden = self.den
        if(resnum == 0):
            return 0
        else: 
            subfrac = fracao(resnum, resden)
            return subfrac
    
    def __mul__(self, frac):
        resnum = self.num * frac.num
        resden = self.den * frac.den
        if (resnum == 0):
            return 0
        else: 
            mulfrac = fracao(resnum, resden)
            return mulfrac

    def __truediv__(self, frac):
        resnum = self.num * frac.den
        resden = self.den * frac.num
        if (resnum == 0 or resden == 0):
            return 0
        else:
            divfrac = fracao(resnum, resden)
            return divfrac
    
    def __gt__(self, frac) -> bool:
        if(self.num == 0 or frac.num == 0):
            return(self.num > frac.num)
        else:
            return ((self - frac).den > 0 and (self - frac).num > 0)
        
    def __lt__(self, frac) -> bool:
        if(self.num == 0 or frac.num == 0):
            return (self.num < frac.num)
        else:
            return (not(self - frac).den > 0  and (self - frac).num > 0)
         
    def __eq__(self, frac) -> bool:
        if(self.num == 0 or frac.num == 0):
            return(self.num == frac.num)
        else:
            return(self.den == frac.den and self.num == frac.num)
    
    def __ne__(self, frac) -> bool:
        if(self.num == 0 or frac.num == 0):
            return(self.num != frac.num)
        else:
            return(self.den != frac.den or self.num != frac.num)

    def __ge__(self, frac) -> bool:
        if(self.num == 0 or frac.num == 0):
            return((self.num == frac.num) or (self.num > frac.num))
        else:
            return (((self - frac).den > 0 and (self - frac).num > 0) or (self.num == frac.num and self.den == frac.den))

    def __le__(self, frac) -> bool:
        if(self.num == 0 or frac.num == 0):
            return((self.num == frac.num) or (self.num < frac.num))
        else:
            return (not((self - frac).den > 0  and (self - frac).num > 0) or (self.num == frac.num and self.den == frac.den))
  
#eu amo o 0 :DDDDDDDDDDDDDDD