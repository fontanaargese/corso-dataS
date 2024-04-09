catal=[["emma","austen","1234"],["divina commedia","dante","0000"]] 

class Libro:                                                            #ho definito la prima classe
    def __init__(self,titolo,autore,isbn):
    #definsco la prima classe con alttributi
        self.titolo=titolo
        self.autore=autore
        self.isbn=isbn
        catal.append([self.titolo,self.autore,self.isbn])     #faccio append nella lista

#definisco la seconda classe
class Libreria:
    def __init__(self,catalogo):      #definisco una seconda classe che mi chiede come attributo il nome del catalogo che voglio vedere
        self.catalogo=catalogo

    #definisco i tre metodi della classe
    def aggiungi_libro(self):                       #aggiungo un nome 
    
        name=input("aggiungi il nome: ")
        autor=input("inserisci l'autore : ")       #gli faccio inserire un nome, autore,code
        code=input("inserisci isbn: ")

        Libro(name,autor,code)                               #creo l'oggetto libro con i miei input
        

    def rimuovi_libro(self,isbn):
        for libro in self.catalogo:                                  #itero su ogni lista nella lista catalogo
            if libro[2]==isbn:                                       #se nella lista in posizione 2 dove è presento l'isbn  
                self.catalogo.remove(libro)                             #lo rimuovo

    def cerca_per_titolo(self,titolo):
        for libro in self.catalogo:                                 
            if libro[0]==titolo:                                  #itero su ogni lista nella lista catalogo
                print(libro)                                        #se nella lista in posizione 0 dove è presente il titolo
                                                                    #lo printo
            

    def mostra_catalogo(self):
        print(self.catalogo)                                   #print del catalogo



Lib=Libreria(catal)
Lib.aggiungi_libro()
Lib.rimuovi_libro("1234")
Lib.cerca_per_titolo("divina commedia")
Lib.mostra_catalogo()

#testa tutto

    
