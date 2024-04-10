vendite=[500,200,600]                                        #creo una lista vuota
while True:                                        
    
    vendita=input("inserisci le vendite:(separate da spazi): ")   #faccio inserire le vendite nuove

    vendita=vendita.split(" ")                                       #le splitto
    
    for vend in vendita:                                                #per ogni elemento nella lista vendite
        try:                                                            #provo a mdoficarlo in int
            vend=int(vend)
        except ValueError:
            print("non hai inserito un intero")                          #altrimenti mi printa non hai isnerito un intero
        else:
            vendite.append(vend)                                            #se lo fa  me lo appende alla lista vendite creata inizalmente
    altro=input("vuoi inserire altre vendite? ")                         #chiedo se vuole inserire altor
    altro=altro.lower()
    if altro=="no":
            break

def tot(vendite):                                                          #definisco la funzione tot vendite
    try:
        totale= sum(vendite)                                               
        print("il tuo totale è:",totale)
    except ValueError:
        print("la lista è vuota")


def media(vendite):
    try:                                                         #definisco la funzione media vendite
        media=sum(vendite)/len(vendite)
        print("la media è: ",media)
        return media


    except ValueError:
        print("la lista vendite è vuota")

def valore_sopra_media(vendite):
    numeri = []                                                               #definisco la funzione valori sopra la media
    med = media(vendite) 
    
    for i in vendite:
        if i > med:
            numeri.append(i)
    try:

        print("I numeri sopra alla media:", numeri)
    except ValueError:
        print("non ci sono valori sopra la media")
        

tot(vendite)
media(vendite)
valore_sopra_media(vendite)
