# Creare un sistema che faccia inserire un numero e continui a ripetere il sistema finchè il numero è pari, 
# dopo aver  inserito invece 3 numeri dispari che vengono salvati li stampa e chiude tutto

numeri_dispari=[]
while len(numeri_dispari)<=2:
    numero=int(input("inserisci un numero: "))
    if numero%2!=0:
        numeri_dispari.append(numero)
print("la lista di numeri dispari è: ",numeri_dispari)
    


