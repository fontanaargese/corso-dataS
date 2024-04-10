registro_visitatori = []                                       #creo una lista visitatori esterns

class Museo:
    def __init__(self, registro):                                  #definizione di una classe museo che vuole solo come paramentro il registro
        self.registro = registro

    def visualizza_visitatori(self):
        print("Ecco la lista dei visitatori: ", self.registro)

class Visitatore(Museo):
    def __init__(self, nome, ID, registro):
        super().__init__(registro)
        self.nome = nome
        self.ID = ID
        registro_visitatori.append([self.nome, self.ID])


museo = Museo(registro_visitatori)

# Creazione di visitatori e aggiunta al registro
while True:
    nome=input("inserisci il nome:")
    id=int(input("inserisci ID:"))
    visitatore=Visitatore(nome,id,registro_visitatori)
    altro=input("vuoi inserire altro: ")
    altro=altro.lower()
    if altro=="no":
        break


# Visualizzazione dei visitatori
museo.visualizza_visitatori()