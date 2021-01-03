import numpy as np

#NumeroTxT=open("Rn.txt").read()
NumeroTxT=open("rnP.txt").read()#numeros psudoAleatorios de python
NumeroTxT=NumeroTxT.split(",")
NumeroTxT.pop()

Numero=[]
for i in NumeroTxT:
    convertirN=float(i)
    Numero.append(convertirN)

print("PRUEBA DE KOLMOGOROV")
FO=[0]*10
for i in Numero:
    if i >= 0.0 and i < 0.1:
        FO[0]+=1
    elif i >= 0.1 and i < 0.2:
        FO[1]+=1
    elif i >= 0.2 and i < 0.3:
        FO[2]+=1
    elif i >= 0.3 and i < 0.4:
        FO[3]+=1
    elif i >= 0.4 and i < 0.5:
        FO[4]+=1
    elif i >= 0.5 and i < 0.6:
        FO[5]+=1
    elif i >= 0.6 and i < 0.7:
        FO[6]+=1
    elif i >= 0.7 and i < 0.8:
        FO[7]+=1
    elif i >=0.8 and i < 0.9:
        FO[8]+=1
    elif i >=0.9 and i <= 1:
        FO[9]+=1

FOA=[]
foa=0 #acumula
for i in FO:
    foa+=i
    FOA.append(foa)

POA=[]
poa=0
for i in FOA:
    poa+=(i/FOA[-1])
    POA.append(poa)

PEA=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

PEAPOA=[]
for i in range(len(PEA)):
    peapoa=abs(PEA[i]-POA[i])
    PEAPOA.append(peapoa)


DMcal=max(PEAPOA)

if len(Numero)<=35:
    DMcrit=float(input(f"Por favor ingresa el DM critico para {len(Numero)} grados de libertad "))
else:
    DMcrit=1.36/np.sqrt(len(Numero))
if DMcal<=DMcrit:
    print("Si logro la prueba de uniformidad")
else:
    print("No logro la prueba de uniformidad")


print("FOA: ",FOA)
print("POA", POA)
print("PEA", PEA)
print("|PEA-POA|", PEAPOA)
print("DMcal", DMcal)