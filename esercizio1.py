def calcola_area_triangolo(base, altezza):
    return base * altezza / 2

def calcola_area_quadrato(lato):
    return lato ** 2

def calcola_area_rettangolo(base, altezza):
    return base * altezza

def calcolo_area():
    aree = []
    while True:
        scelta = input("Quale forma geometrica? (triangolo, quadrato, rettangolo): ").lower()
        if scelta == "triangolo":
            base = int(input("Inserisci la base del triangolo: "))
            altezza = int(input("Inserisci l'altezza del triangolo: "))
            area = calcola_area_triangolo(base, altezza)
            aree.append(("Triangolo", area))
        elif scelta == "quadrato":
            lato = int(input("Inserisci il lato del quadrato: "))
            area = calcola_area_quadrato(lato)
            aree.append(("Quadrato", area))
        elif scelta == "rettangolo":
            base = int(input("Inserisci la base del rettangolo: "))
            altezza = int(input("Inserisci l'altezza del rettangolo: "))
            area = calcola_area_rettangolo(base, altezza)
            aree.append(("Rettangolo", area))
        else:
            print("Scelta non valida. Riprova.")
            continue
        print(aree)
        flag = input("Vuoi continuare? (sì/no): ")
        flag=flag.lower()
        if flag != "sì":
            break


calcolo_area()
