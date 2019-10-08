class Equacio:
    def __init__(self,eq):
        self.eq = eq

    def calcula(self):
        self.a,self.operator,self.c,self.equal,self.e = self.eq.split(" ")
        self.NumX,self.x = self.a.split("x")

        if self.operator == "+":
            self.NoX = float(self.e) - float(self.c)
            self.x = float(self.NoX) / float(self.NumX)
        else:
            self.NoX = float(self.e) + float(self.c)
            self.x = float(self.NoX) / float(self.NumX)

        return float(self.x)
