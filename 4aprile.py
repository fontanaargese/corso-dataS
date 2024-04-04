
# #print 
# print("Hello wolrd!")
# nome="alice"
# età=25
# print("il mio nome è",nome, "la mia età è:",età)
#il concatenamento di int e stringhe non è possibile con il +

#input function
# nome=input("inserisci il tuo nome:")
# print("ciao, ",nome," Benvenuto in Python")

#metodi per le stringhe
# s="ciao mondo!"
# print(len(s))
# print(s.upper())
# print(s.split('o'))
# print(s.replace('mondo','universo'))

# #bool e operatori logici
# x=15
# y=20
# z=30
# print(x<y and x>y)
# print(not(x<y and x>y))

#esercizio1
#fai inserire all'utente 3 dati(Nome,password,età)

# nome=input("inserisci il tuo nome:")
# età=int(input("inserisci la tua età:"))
# password=input("inserisci una password: ")
# print("il tuo nome è: ",nome," la tua età è: ", età,", la tua passwoord è:",password)
# print(età>18)

# #if elif
# numero=100
# if numero>0:
#     print("il numero è positivo")
#     if numero==100:
#         print("wow")
# elif numero <0:
#     print("il numero è negativo")  
# else: 
#     print("il numero è zero")

#nuovo utente
nuovo_nome=input("inserisci il tuo nuovo nome:")
nuova_password=input("inserisci la tua nuova password:")
nuovo_animale_preferito=input("quale è il tuo animale preferito?:")
nuovo_colore_preferito=input("quale è il tuo colore preferito?:")

#login
nome=input("inserisci il tuo nome=")
password=input("inserisci password=")

#controllo password
if nome==nuovo_nome and password==nuova_password:
    cambio=input("vuoi cambiare la password?:")
    cambio=cambio.lower()
    #cambio password e utente
    #se è si vuole effettuare il cambio
    if cambio=="si":
        scelta=int(input("A quale domanda segreta vuoi rspondere?\n animale prefrito(1)\n colore preferito(2):"))
        if scelta==1:
            animale_preferito=input("inserisci animale preferito")
            if animale_preferito==nuovo_animale_preferito:
                nome_cambiato=input("Inserisci un nome diverso")
                password_cambiata=input("Inserisci una password diversa:")
                nome=nome_cambiato
                password=password_cambiata
            else:
                print("la domanda segreta è sbagliata")
        else:
            colore_preferito=input("Inserisci il colore preferito:")
            if colore_preferito==nuovo_colore_preferito:
                nome_cambiato=input("Inserisci un nome diverso")
                password_cambiata=input("Inserisci una password diversa:")
                nome=nome_cambiato
                password=password_cambiata 
            else:
                print("la domanda segreta è sbagliata")
    else: 
        print("benvenuto")
else:
    scelta=int(input("A quale domanda segreta vuoi rspondere?\n animale prefrito(1)\n colore preferito(2):"))
    if scelta==1:
            animale_preferito=input("inserisci animale preferito")
            if animale_preferito==nuovo_animale_preferito:
                nome_cambiato=input("Inserisci un nome diverso")
                password_cambiata=input("Inserisci una password diversa:")
                nome=nome_cambiato
                password=password_cambiata
            else:
                print("la domanda segreta è sbagliata")
    else:
        colore_preferito=input("Inserisci il colore preferito:")
        if colore_preferito==nuovo_colore_preferito:
            nome_cambiato=input("Inserisci un nome diverso")
            password_cambiata=input("Inserisci una password diversa:")
            nome=nome_cambiato
            password=password_cambiata 
        else:
            print("la domanda segreta è sbagliata")
    
    
        

