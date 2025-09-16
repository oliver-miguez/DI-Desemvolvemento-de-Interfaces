#SENTENCIA CONDICIONAIS

n1 = 5

if n1 > 5:
    print("hola")
elif n1 == 5:
    print("Numero igual")
elif n1 == 4:
    print("es un cuatro")
else:
    print("Adios")
    if n1 < 2:
        print("Este numero es muy pequeño")
    else:
        print("Es pequeño pero no tanto")

print("if finalizado ya estamos fuera del if")

#Operador Ternario
#vehiculoTipo = (vehiculo <= 3) ? "Auto" : "Moto"; JAVA
vehiculoTipo = "Coche" if n1 <= 3 else "Moto" # Python

#While
n2 = 0
while n2 < n1:
    n2+=1
    print(n2)

while n2 < 100:
    n2 += 2
    print(n2)
print("____________________")
#Do while
while True:
    print(n1)
    n1 += 1
    if n1 == 10:
        break