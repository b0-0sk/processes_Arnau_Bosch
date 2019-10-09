class Equacio:
    def __init__(self,eq):
        self.eq = eq

    def calcula(self):
        try:
            self.a,self.operator,self.c,self.equal,self.e = self.eq.split(" ")
            self.NumX,self.x = self.a.split("x")

        except:
            return ("l'equacio no segueix el format: ax + b = c")
        try:
            if self.operator == "+" :
                self.NoX = float(self.e) - float(self.c)
                self.x = float(self.NoX) / float(self.NumX)
            if self.operator == "-":
                self.NoX = float(self.e) + float(self.c)
                self.x = float(self.NoX) / float(self.NumX)
        except:
                return ("l'equacio conte caracter no calculables o conte un string buit: " + self.eq)


        try:
            return float(self.x)
        except:
            return ("Operador no valid: " + self.operator)
