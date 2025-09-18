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
    }
    """

    numeros2 = [1, 2, 3, 4, 5, 1234,10,9,123,432]

    for indice in range ( 3,10,3): # Empieza por el tercer valor , 10 es el valor a obtener final, y el ultimo 3 es porque va de 3 en 3
        print(numeros2[indice])

var= [1,2,3]
def funcion(parametro):
    parametro[0]= 3
    parametro[1]= 4
    parametro[2]= 5
funcion(var) # la variable var actuaria como "parametro de la función "funcion"
print(var)

print("suma:")
def funcion2(lista):
    suma = 0
    for num in lista:
        suma = suma + num
        return suma
print(funcion2(var))

print("suma,media")
def media(lista):
    suma = 0
    for num in lista:
        suma = suma + num
    return suma, suma/len(lista)
_,m = media(var) # solo ejecuta el valor de la derecha del return en este caso suma/len(lista)
tupla = media(var)
print(m)
print(tupla)