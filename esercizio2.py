def numero_primo(n):
    #Dividiamo per tutti i numeri più tra 1 ed n. 
    #Il resto per una di queste è 0 allora non è primo 
    #elif resto!=0 è primo
    for i in range(2,n):
        divisori=[]
        if n%i == 0 : 
            isprime = False 
            print(n,'non è un numero primo...')
            divisori.append(i)
            divisore=min(divisori)
            return isprime, divisore
           
        else :
            isprime = True
            print(n,' è un numero primo')
            return isprime, n
    
while True:
    #chiedi nome
    #chiedi numero n più piccolo di 100
    numeri_primi=[]
    nome = input('Nome: \n')
    num = int(input('Numero tra 1 e 100: \n'))
    bol, divis=numero_primo(num)
    cas=num//divis
    if bol==False:
        for i in range(divis,cas):
            print(divis*i)
        

    else:
        numeri_primi.append(num)    