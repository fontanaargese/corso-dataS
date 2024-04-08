class Punto:
    x=0
    y=0
    def __init__(self):
        pass
    def muovi(self):
        self.dx=int(input("inserisci un valore per x:"))
        self.x=self.dx
        self.dy=int(input("inserisci un valore per y: "))
        self.y=self.dy
        print("il punto ha cordinate: ",self.x,self.y)


    def distanza_da_origine(self):
        distanza= ((self.x-0)**2 + (self.y-0)**2)**0.5
        print("la distanza dall'origine è: ",distanza)


a=Punto()
Punto.muovi(a)
Punto.distanza_da_origine(a)

