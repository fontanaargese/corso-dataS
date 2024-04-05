def sequenza():
    numero=int(input("inserisci un numero: "))
    counter=True
    seq=[0,1]
    inizio=0
    while counter:
        elemento=seq[-1]+seq[-2]
        seq.append(elemento)
        if seq[-1]>numero:
            break
        print(seq[-1])
sequenza()
