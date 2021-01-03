x=int (input("Por favor ingresa la semilla: "))
print("")

a=int (input("Por favor ingresa el multiplicador: "))
print("")

c=int (input("Por favor ingresa el incremento: "))
print("")

m=int (input("Por favor ingresa el modulo: "))
print("")

Rn=[]
Almacen=[x]
while True: 
    Xn1= (a*x+c)%m
    if Xn1 in Almacen:
        break
    else: 
        Almacen.append(Xn1)
        x=Xn1
        rn=x/m
        Rn.append(rn)

print(Almacen)
print(Rn)

Numero=open("Rn.txt","w+")
for i in Rn: 
    Numero.write(str(i))
    Numero.write(",")
Numero.close()