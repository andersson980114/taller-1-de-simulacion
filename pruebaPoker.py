#NumeroTxT=[0.7292, 0.7133, 0.7132, 0.7132 ]

NumeroTxT=open("rnP.txt").read() #numeros psudoAleatorios de python
#NumeroTxT=open("Rn.txt").read() 
NumeroTxT=NumeroTxT.split(",")
NumeroTxT.pop()

Numero=[]
for i in NumeroTxT:
    convertirN=float(i)
    Numero.append(convertirN)


for i in range(0, len(NumeroTxT)):
    carta1=int(NumeroTxT[i] * 10) % 10
    carta2=int(NumeroTxT[i] * 100) % 10
    carta3=int(NumeroTxT[i] * 1000) % 10
    carta4=int(NumeroTxT[i] * 10000) % 10
    #print (carta1)
    #print (carta2)
    #print (carta4)
    
    print(NumeroTxT[i])
    print(i, "posicion")
    print(carta4)



 
