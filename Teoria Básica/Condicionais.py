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
        print("true")
        break
    else:
        print("false")

print("____________________")

#FOR IN
numeros = [1,2,3,4,5,1234]
suma = 0
for numero in numeros:
    print(numero)
    suma = suma + 1

print(suma)

print("____________________")


d = {
    1:"un",
    2:"dous",
    3:"tres",
    4:"catro",
    5:"cinco"
}

for valor in d:
    print(valor) #muesta las claves del diccionario| 1,2,3
    print(d[valor])#muestra el valor propio de cada clave| "un","dous"...

print("____________________")

for indicie in range(5): #Range valores desde el 0 al 5 sin incluir el 5
    print("indice:",indicie)
    print(numeros[indicie])
    """
    JAVA
    for(int i = 0; i < 5; i++){
    System.out.println(i);
    System.out.println(numeros[i]);
    """