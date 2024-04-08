#Definisco la classe

lista_oggetti=[]
lista_ristoranti=[]
class Ristorante:
    
    def __init__(self,nome,tipo):       #definisco l'oggetto di tipo ristorante
        self.nome=nome                  #nome e tipo sono attrbuti da specificare nella creazione 
                                        #aperto è sempre di ciascun oggetto ma non lo specifico nella creazione
        self.tipo=tipo
        self.aperto=False
        self.menu={}
        lista_ristoranti.append(self.nome)
        
                        #anche il menu è di ciascun oggetto ed è un dizionario 

    def descrivi_ristorante(self):             #creo la funzione descrivi ristorante
        print("il nome del ristorante è: ",self.nome, ".","Lo stile della mia cucina è", self.tipo)
        #inserendo come attributo il self che fa riferimento al ristorante 



    def stato_apertura(self):                               #controllo se il risotrante è aperto o chiuso
        if self.aperto==False:                             #e printo in base all'if
            print("il ristorante è attualmente aperto ")
        else:
            print("il ristorante è chiuso")


    def apri_ristorante(self):                                 #apro il ristorante
        if self.aperto==False:
            print("il ristorantè è stato appena aperto")
            self.aperto==True
      

    def chiudi_ristorante(self):                              #chiudo il risturante
        if self.aperto==True:
            print("il ristorante è stato appena chiuso")
            self.aperto==False

    def stampa_menu(self):
        print("il nostro menu è: ", self.menu)    
    

    def aggiungi_al_menu(self):
        while True:
            nome=input("inserisci un nuovo nome per il piatto: ")      #faccio un ciclo while
            prezzo=int(input("inserisci il prezzo del piatto: "))      #faccio inserire nome e prezzo. 
            self.menu[nome]=prezzo                                     #aggiungo nuovo elemento al menu
            altro=input("vuoi aggiungere altro?: ")
            if altro=="no":
                break
    
    def rimuovi_dal_menu(self):
        print(self.menu)
        cosa=input("quale elemento vuoi rimuovere?: ")       #da verificare se funziona
        del self.menu[cosa]


ristorante1=Ristorante("viva L'Italia","italiano")
ristorante2=Ristorante("viva il Messico","messicano")
lista_oggetti.append(ristorante1)
lista_oggetti.append(ristorante2)
print(lista_ristoranti)

while True:
        ristorante=input("ciao. Inserisci il nome del ristorante che vuoi cercare: ")
        for i, ristorante in zip(lista_oggetti,lista_ristoranti):
            action=int(input("cosa vuoi fare?(1:descrizione, 2:status, 3:apri, 4:chiudi, 5:menu) "))
            if action==1:
                i.descrivi_ristorante()
            elif action==2:
                i.stato_apertura()
            elif action==3:
                i.apri_ristorante()
            elif action==4:
                i.chiudi_ristorante()
            else:
                cosa=int(input("cosa vuoi fare? (1:aggiungere, 2:modificare)"))
                if cosa==1:
                    i.aggiungi_al_menu()
                else:
                    i.rimuovi_dal_menu()

            again=int(input("vuoi cercare un altro ristorante?:(1:si, 2:no) "))
            if again==2:
                break
            
  