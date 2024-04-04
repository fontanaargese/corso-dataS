numero = int(input("Inserisci un numero: "))
counter = 0
while counter == 0:
    for i in range(numero, 0, -1): 
        print(i)
    domanda = int(input("Vuoi inserire un altro numero? (0 per no, 1 per sì): "))
    if domanda == 0:
        numero = int(input("Inserisci un altro numero: "))
    else:
        counter = 1
        print("Fine")