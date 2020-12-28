import math
NumeroTxT=open("Rn.txt").read()
NumeroTxT=NumeroTxT.split(",")
NumeroTxT.pop()
#datos de pruebas
#Numero=[0.41, 0.68, 0.89, 0.94, 0.74, 0.91, 0.55, 0.62, 0.36, 0.27, 0.19, 0.72, 0.75, 0.08, 0.54, 0.02, 0.01, 0.36, 0.16, 0.28, 0.18, 0.01, 0.95, 0.69, 0.18, 0.47, 0.23, 0.32, 0.82, 0.53, 0.31, 0.42, 0.73, 0.04, 0.83, 0.45, 0.13, 0.57, 0.63, 0.29]
#Numero=[0.08, 0.09, 0.23, 0.29, 0.42, 0.55, 0.58, 0.72, 0.89, 0.91,0.11, 0.16, 0.18, 0.31, 0.41, 0.53, 0.71, 0.73, 0.74, 0.84,0.01, 0.09, 0.30, 0.32, 0.45, 0.47, 0.69, 0.74, 0.91, 0.95,0.12, 0.13, 0.29, 0.36, 0.38, 0.54, 0.68, 0.86, 0.88, 0.91]
Numero=[]
Signos=["*"]
for i in NumeroTxT:
    convertirN=float(i)
    Numero.append(convertirN)

corridas=0
numerosPos=0
numerosNeg=0
U=0
S=0
N=len(Numero)


for i in range(0, len(Numero)-1):
    n1= Numero[i]
    n2= Numero[i+1]

    if n2>n1:
        Signos.append("+")
        numerosPos+=1
    else:
        Signos.append("-")
        numerosNeg+=1
    

for i in range(0, len(Signos)-1):
    if Signos[i] != Signos[i+1]:
        corridas+=1
    

print("")  
print("corridas: ",corridas)
print("numerosNeg: ",numerosNeg)
print("numerosPos: ",numerosPos)

U= (2*N-1)/3
S= (16*N-29)/90
Z= (corridas-U)/math.sqrt(S)

print("U=",U)
print("S=",S)
print("Z=",Z)

if Z>-1.96 and Z<1.96:
    print("Hay independencia")
else:
    print("No hay independencia")


def imprimirSignos(): 
    a= int(math.sqrt(len(Signos)))
    for i in range(0, len(Signos)):
        if i%a==0 and i>1:
            print("")
        print(Signos[i], end="")
            

imprimirSignos()
        

