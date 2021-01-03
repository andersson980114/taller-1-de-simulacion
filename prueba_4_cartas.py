NumeroTxT=[]
Cuatro_iguales_contador = 0
tres_iguales_una_diferete_contador =0
dos_iguales_dos_diferentes_contador = 0
dos_iguales_dos_iguales_contador = 0
ninguna_Repetida= 0
Xcrit=16.92

Numero=open("rnP.txt").read() #numeros psudoAleatorios de python
#NumeroTxT=open("Rn.txt").read() 
Numero=Numero.split(",")
Numero.pop()

print("PRUEBA DE POKER 4 CARTAS")

for i in Numero:
    convertirN=int(i)
    NumeroTxT.append(convertirN)

for i in range(0, len(NumeroTxT)):

    carta1 = carta1=round(NumeroTxT[i] /1000) % 10
    carta2=round(NumeroTxT[i] / 100) % 10
    carta3=round(NumeroTxT[i] / 10) % 10
    carta4=round(NumeroTxT[i] ) % 10



    if (carta1 == carta2 and carta1 == carta3 and carta4==carta3):
        Cuatro_iguales_contador +=1
    elif ((carta1 == carta2 and carta1 == carta3 and carta1 != carta4) 
          or (carta1 == carta2 and carta1 ==carta4 and carta1 != carta3) 
          or  (carta1 == carta3 and carta1 ==carta4 and carta1 != carta2) 
          or (carta4 == carta3 and carta4 ==carta2 and carta4 != carta1)):
          tres_iguales_una_diferete_contador +=1
    
    elif ((carta1 == carta2 and carta1 != carta3 and carta3 != carta4) 
          or (carta1 == carta3 and carta1 != carta2 and carta2 != carta4) 
          or (carta1 == carta4  and carta1 != carta2 and carta2 != carta3) 
          or (carta2 == carta3 and  carta2 != carta4  and carta4 != carta1) 
          or (carta2 == carta4 and carta2 != carta1 and carta1 != carta3)
          or (carta3 == carta4 and carta3 != carta1 and carta4)):
          dos_iguales_dos_diferentes_contador += 1
    elif ((carta1 == carta2 and carta1 != carta3 and carta3 == carta4)
          or (carta1 == carta3 and carta1 != carta2 and carta2 == carta4)
          or (carta1 == carta4 and carta1 != carta2 and carta2 == carta3)):
          dos_iguales_dos_iguales_contador +=1
    
    elif (carta1 != carta2 and carta2 != carta3 and carta3 != carta4):
        ninguna_Repetida +=1


    
print(tres_iguales_una_diferete_contador, "tres iguales")
print(ninguna_Repetida, "ninguna repetida")
print(dos_iguales_dos_iguales_contador, "dos iguales dos iguales")
print(dos_iguales_dos_diferentes_contador, "dos iguales dos diferentes")
print(Cuatro_iguales_contador, "four i")


suma = dos_iguales_dos_diferentes_contador + dos_iguales_dos_iguales_contador +ninguna_Repetida + Cuatro_iguales_contador +tres_iguales_una_diferete_contador
FE_3R = 0.036*suma
FE_2R2R = 0.027*suma
FE_2R2D = 0.4320*suma
FE_NR = 0.504*suma
FE_4R = 0.001*suma

def fefo(FE,FO):
    return ((FE-FO)**2)/FE

Xcalculado0=fefo(FE_NR,ninguna_Repetida)

Xcalculado2D=fefo(FE_2R2D,dos_iguales_dos_diferentes_contador)

Xcalculado2I=fefo(FE_2R2R,dos_iguales_dos_iguales_contador)

Xcalculado3=fefo(FE_3R,tres_iguales_una_diferete_contador)
Xcalculado4=fefo(FE_4R, Cuatro_iguales_contador)


 

Xcalculado = Xcalculado0+Xcalculado2D+Xcalculado2I+Xcalculado3+Xcalculado4


if Xcalculado > Xcrit:
    print("El Xcalculado : ", Xcalculado, "es mayor que el XCritico :",Xcrit," por lo tanto este Generador no pasa la prueba")

elif Xcalculado  <= Xcrit:
    print("El Xcalculado : ", Xcalculado, "es menor que el XCritico :",Xcrit," por lo tanto este Generador si pasa la prueba")





print(Xcalculado)
    
