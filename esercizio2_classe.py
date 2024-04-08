class Libro:
    def __init__(self,titolo,autore,pagine):
        self.titolo=titolo
        self.autore=autore
        self.pagine=pagine
    
    def descrizione(self):
        print("il titolo del libro è: ", self.titolo," L'autore è: ", self.autore, "le pagine sono: ",self.pagine)

libro1=Libro("Emma","Austen",400)
libro1.descrizione()