
catalogo=[["emma","austen","1234"],["divina commedia","dante","0000"]] #ho creato una lista catalogo iniziale
class Libro:                                                            #ho definito la prima classe
    def __init__(self,titolo,autore,isbn):
    #definsco la prima classe con alttributi
        self.titolo=titolo
        self.autore=autore
        self.isbn=isbn
        catalogo.append([self.titolo,self.autore,self.isbn])     #faccio append nella lista

#definisco la seconda classe
class Libreria:
    def __init__(self,catalogo):      #definisco una seconda classe che mi chiede come attributo il nome del catalogo che voglio vedere
        self.catalogo=catalogo

    #definisco i tre metodi della classe
    def aggiungi_libro(self):                       #aggiungo un nome 
    
        name=input("aggiungi il nome: ")
        autor=input("inserisci l'autore : ")       #gli faccio inserire un nome, autore,code
        code=input("inserisci isbn: ")

        libro=Libro(name,autor,code)                               #creo l'oggetto libro con i miei input
        catalogo.append([libro.titolo,libro.autore,libro.isbn])

    def rimuovi_libro(self,isbn):
        for libro in self.catalogo:
            if libro[2]==isbn:
                self.catalogo.remove(libro)

    def cerca_per_titolo(self,titolo):
        for libro in self.catalogo:
            if libro[0]==titolo:
                print(libro)
            

    def mostra_catalogo(self):
        print(self.catalogo)
        
Lib=Libreria(catalogo)
Lib.aggiungi_libro()
Lib.rimuovi_libro("1234")
print(catalogo)

Lib.cerca_per_titolo("divina commedia")
Lib.mostra_catalogo()

#testa tutto

    
