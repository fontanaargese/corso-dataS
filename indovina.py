import random
def indovina():
    counter=True
    while counter:
        numero=random.randint(0,100)
        num=int(input("inserisci un numero: "))
        if numero<num:
            print("numero troppo basso")
        elif numero>num:
            print("numero troppo alto")
        elif numero==num:
            print("hai indovinato")
            break
        else:
            esci=input("vuoi uscire?: ")
            esci=esci.lower()
            if esci=="si":
                break

indovina()