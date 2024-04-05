#prenotazione del tavolo
counter=0
tavoli=[]
while counter < 10:
    nome=input("inserisci il nome: ")
    if nome:
        counter= counter + 1
        tavoli.append(counter)
        print("il tuo tavolo è: ",counter)
    
    #definzione dei tipi di torte
    base=[[" base cioccolato",2],[" base vaniglia",3],["base pistacchio",4]]
    farcitura=[["farcitura cioccolato",1],["farcitura vaniglia",2],["farcitura pistacchio",3]]
    topping=[["topping cioccolato",1],["topping vaniglia",1],["topping pistacchio",3]]

    mix=[]
    prezzo=0
    quant=0
    while quant<3:
        #scelta della base dall'utente
        base_scelta=int(input("Che tipo di base vuoi (cioccolato=1, vaniglia=2, pistacchio=3): "))
        if base_scelta==1:
            prezzo= prezzo + base[0][1]
            mix.append(base[0][0])
        elif base_scelta==2:
            prezzo = prezzo +base[1][1]
            mix.append(base[1][0])
        else:
            prezzo= prezzo +base[2][1]
            mix.append(base[2][0])
        #scelta della farcitura
        farcitura_scelta=int(input("Che tipo di farcitura vuoi (cioccolato=1, vaniglia=2, pistacchio=3): "))
        if farcitura_scelta==1:
            prezzo= prezzo +farcitura[0][1]
            mix.append(farcitura[0][0])
        elif farcitura_scelta==2:
            prezzo = prezzo +farcitura[1][1]
            mix.append(farcitura[1][0])
        else:
            prezzo= prezzo + farcitura[2][1]
            mix.append(farcitura[2][0])
        #scelta del topping
        topping_scelto=int(input("Che tipo di topping vuoi (cioccolato=1, vaniglia=2, pistacchio=3): "))
        if topping_scelto==1:
            prezzo= prezzo + topping[0][1]
            mix.append(topping[0][0])
        elif topping_scelto==2:
            prezzo = prezzo +topping[1][1]
            mix.append(topping[1][0])
        else:
            prezzo= prezzo +topping[2][1]
            mix.append(topping[2][0])
        #print resume
        print("Il prezzo complessivo è: ",prezzo)
        print("la torta scelta è: ",mix)
        quant=quant+1
        print("la quantità è: ", quant)
        #ordinare piu torte
        cont=input("vuoi ordinare un altra torta?: ")
        cont=cont.lower()
        if cont=="no":
            break