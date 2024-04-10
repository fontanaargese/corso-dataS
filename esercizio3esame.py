class Panino:                                                                   #definisco una classe panino con attributi
    def __init__(self,pane,riempimento,salsa,nome):
        self.pane=pane
        self.riempimento=riempimento
        self.salsa=salsa
        self.nome=nome
    def visualizza(self):                                                  #per la  classe panino definisco la funzione visualizza panino
        print("il tuo panino ha:",self.pane,self.riempimento,self.salsa, "e si chiama : ", self.nome)

lista_burger=[]
while True:                                                                  #creo un ciclo while dove faccio inserire i dati all'utente
    pane=input("seleziona il pane:")
    riempimento=input("seleziona il riempimento:")
    salsa=input("seleziona la salsa: ")
    nome=input("scegli un nome: ")
    burger=Panino(pane,riempimento,salsa,nome)
    lista_burger.append([burger.nome,burger.riempimento,burger.salsa,burger.nome])
    burger.visualizza()
    altro=input("vuoi creare un altro panino?: ")
    altro=altro.lower()
    if altro=="no":
        break
    
print(lista_burger)