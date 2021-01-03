NumeroTxT=[]
Tres_Repetidas_contador = 0
dos_Repetidas_contador = 0
ninguna_Repetida= 0
Xcrit=16.92

Numero=open("rnP.txt").read() #numeros psudoAleatorios de python
#NumeroTxT=open("Rn.txt").read() 
Numero=Numero.split(",")
Numero.pop()

print("PRUEBA DE POKER 3 CARTAS")

for i in Numero:
    convertirN=int(i)
    NumeroTxT.append(convertirN)

for i in range(0, len(NumeroTxT)):

    carta1=round(NumeroTxT[i] / 100) % 10
    carta2=round(NumeroTxT[i] / 10) % 10
    carta3=round(NumeroTxT[i] ) % 10

    if carta1 == carta2 and carta1 == carta3:
        Tres_Repetidas_contador +=1
    elif (carta1 == carta2 or carta1 == carta3) or (carta2 == carta3):
        dos_Repetidas_contador +=1
    
    elif carta1 != carta2 and carta1 != carta3:
        ninguna_Repetida +=1

print(Tres_Repetidas_contador, "tres iguales")
print(ninguna_Repetida, "ninguna repetida")
print(dos_Repetidas_contador, "dos iguales dos iguales")



suma = Tres_Repetidas_contador+dos_Repetidas_contador+ninguna_Repetida
FE_3R = 0.01*suma
FE_2R = 0.27*suma
FE_NR = 0.72*suma

def fefo(FE,FO):
    return ((FE-FO)**2)/FE

Xcalculado1=fefo(FE_3R,Tres_Repetidas_contador)
Xcalculado2=fefo(FE_2R,dos_Repetidas_contador)
Xcalculado3=fefo(FE_NR,ninguna_Repetida)
 

Xcalculado = Xcalculado1+Xcalculado2+Xcalculado3


if Xcalculado > Xcrit:
    print("El Xcalculado : ", Xcalculado, "es mayor que el XCritico :",Xcrit," por lo tanto este Generador no pasa la prueba")

elif Xcalculado  <= Xcrit:
    print("El Xcalculado : ", Xcalculado, "es menor que el XCritico :",Xcrit," por lo tanto este Generador si pasa la prueba")





print(Xcalculado2)
    
