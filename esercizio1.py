
counter=0
tavoli=[]
while counter < 10:
    nome=input("inserisci il nome: ")
    if nome:
        counter= counter + 1
        tavoli.append(counter)
        print("il tuo tavolo è: ",counter)

    base=[["cioccolato",2],["vaniglia",3],["pistacchio",4]]
    farcitura=[["cioccolato",1],["vaniglia",2],["pistacchio",3]]
    topping=[["cioccolato",1],["vaniglia",1],["pistacchio",3]]

    mix=[]
    prezzo=0
    quant=0
    while quant<3:

        base_scelta=int(input("Che tipo di base vuoi (cioccolato=1, vaniglia=2, pistacchio=3): "))
        if base_scelta==1:
            prezzo= prezzo + base[0][1]
            mix.append("base cioccolato")
        if base_scelta==2:
            prezzo = prezzo +base[1][1]
            mix.append("base vaniglia")
        else:
            prezzo= prezzo +base[2][1]
            
        farcitura_scelta=int(input("Che tipo di farcitura vuoi (cioccolato=1, vaniglia=2, pistacchio=3): "))
        if farcitura_scelta==1:
            prezzo= prezzo +1
            mix.append("farcitura cioccolato")
        if farcitura_scelta==2:
            prezzo = prezzo +2
            mix.append("farcitura vaniglia")
        else:
            prezzo= prezzo +3
        topping_scelto=int(input("Che tipo di topping vuoi (cioccolato=1, vaniglia=2, pistacchio=3): "))
        if topping_scelto==1:
            prezzo= prezzo +1
            mix.append("topping cioccolato")
        if topping_scelto==2:
            prezzo = prezzo +1
            mix.append("topping vaniglia")
        else:
            prezzo= prezzo +3
            
        print("Il prezzo complessivo è: ",prezzo)
        print("la torta scelta è: ",mix)
        quant=quant+1
        print("la quantità è: ", quant)
        cont=input("vuoi ordinare un altra torta?: ")
        cont=cont.lower()
        if cont=="no":
            break