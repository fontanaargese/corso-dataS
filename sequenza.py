
def sequenza():
    #inserisci il numero
    numero=int(input("inserisci un numero: "))
    counter=True
    #inizalizza sequenza
    seq=[0,1]
    inizio=0
    #creo ciclo while
    while counter:
        #creo nuovi elementi per ogni sequenza
        elemento=seq[-1]+seq[-2]
        seq.append(elemento)
        if seq[-1]>numero:
            break
        print(seq[-1])
sequenza()
