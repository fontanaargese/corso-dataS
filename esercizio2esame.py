# Creare un sistema ripetibile che  permetta di registrarsi 
#( NOME, INT1, INT2, INT3 ) e di superare il login solo se fornisco La somma delle tre variabili intere e nome 
    
cliente={"fontana": 50}                   #creo un dizionario con i clienti
logok=False
def login():                                    #definisco una funzione login
    nuovo=input("sei un nuovo utente?: ")             #chiedo se sei nuvo utente
    nuovo=nuovo.lower() 
    if nuovo=="si":
        print("registrati")                          #se si lo faccio registrare inserendo nome e 3 numeri e inserisco
        nome=input("fornisci il tuo nome: ")          #nel dizionario la chiave-valore =nome:somma
        int1=int(input("inserisci il primo numero: "))
        int2=int(input("inserisci il secondo numero: "))
        int3=int(input("inserisci il terzo numero: "))
        sum=int1+int2+int3
        cliente[nome]=sum
    else:
        nome=input("inserisci il nome: ")
        somma=int(input("inserisci la somma dei tuoi 3 interi"))          #altrimenti faccio entrare verificando che chiave valore esiste
        if nome in cliente.keys() and somma in cliente.values():          #nel dizionario
            logok=True                                                    #come valore di return definisco un True che 
            print("benvenuto")                                            #poi potrà essere utlizzato per verificar eil login
            return logok                                                
        else:                                                               
            print("hai sbagliato password")                        
            return logok
            
print(cliente)
login()                                                #test
print(cliente)