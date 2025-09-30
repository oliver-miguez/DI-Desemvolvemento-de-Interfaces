"""
Coleccións:

1ºListas
2ºTuplas
3ºDiccionarios

"""

#LISTAS

l = [23,"Bugario",1,"Hola",[1,2,3,45],-123,-12,2, 3 +4j, True, 1+2,1.2]
print(type(l))
print(l)

l[1] = "Bugario Brugs" #substituye el 2º valor de la lista por el nuevo
l[-2] = False

print(l[1]) #imprime el 2 valor de la lista
print(l[-2]) #imprime el 3 valor empezando por el final

print(l[4][2])#recoge el 3 valor de la lista que esta dentro de l

#Slicing
print(l[2 : 5]) #coge los valores de la lista del 2 al 5 excluyendo al 5 -> [1, 'Hola', [1, 2, 3, 45]]
print(l[1][2:6]) #Tambien funciona con Strings
print(l[1][2:-2])
print(l[:1])#Coge solo el primero
print(l[1:])#Todos menos el primero
print(l[1:6:2]) #Coge valores del 1 al 5 de dos en dos
print(l[::-1])#Recorres la lista al reves

#TUPLAS

t = (2,5,2+4j, "Bugario", [22,3,5,6],3,9) #Cuando esto se declara asi , no se puede modificar
print(t)
#t[2] = "mondongo" -> NO FUNCIONA, ya que intenta cambiar un valor, n
t[4][2]= "Cambiazo" #como el valor [4] es una lista y no una tupla se puede cambiar su valor
print(t)

t2 = 3,
print(t2)

#DICCIONARIOS

d = {
    1: "Un",
    2: "Dous",
    3: "Tres",
    4: "Catro",

}
#Muestra el valor "3:" del diccionario
print(d[3])
#Se pueden reasingnar valores
d[3] = "three"
print(d[3])


l2 = [1,2,3]
l3 = list([1,2,3])#lista
l4 = list((1,2,3))#tupla

t3 = tuple() #la tupla vacía no sirve para nada
t4 = tuple(l3) #se puede crear una tupla a partir de una lista
l3 [0] = 1000
print(t4) # no muestra el 1000 porque ya lo tiene almacenado el valor 1
print(t4,l3)
d2 = {1:"I",2:"II",3:"III"}
d3 = dict() #diccionario vacío

l2.append([3,2,1]) #inserta el objeto
l2.extend([3,2,(1,5,"h"),1]) #inserta los valores del objetos , los valores de la coleccion
l2.insert(3,"Obxeto no 4º lugar") # añade un objetos en una posicion deseada
print(l2.count(1))#cuenta y muestra el total de 1 que tiene mi prgrama , en este caso 2
print(l2)
print(l2.index(3,3,7)) #devuelve el valor de la posicion donde encuentre el valor 3, en este caso la posicion
extraido = l2.pop(5) #devuelve el valor de la lista en la posicion 5 y lo elimina
print("Valor extraido:", extraido)

l2.remove(3) #elimina la primera coincidencia con ese valor de la lista
print(l2)
l2.reverse() # da la vuelta a la lista
print(l2)
l3 = l2[::-1] # l2 sigue igual , pero invertida
print(l3)
l4 = [3,5,6,3,10,23,2]
#print(l2.sort(reverse=True))#Ordena la lista de manera inversa

l5 = ["Un","Dous","Tres", "Catro","Cinco","Seis"]
print(l5.sort(key=len))

#Ordenar en base a la altura
taboa_alturas = [("Manuel",1.82), ("Pepe",2.05), ("Ana", 1.76) ]

def altura(persoa):
    return persoa[1]

taboa_alturas.sort(key=altura)
print(taboa_alturas)


def saudar(lingua):
    def saudar_es():
        print("Hola")
    def saudar_gl():
        print("Ola")
    def saudar_en():
        print("Hello")
    def saudar_it():
        print("Chiao")
    #Diccionario
    func_saudo = {"es": saudar_es, #no ponemos parentesis porque solo hacemos referencia a ellas , no las ejecutamos, si le ponemos asi: saudar_es() -> Dará error

                  "gl": saudar_gl,
                  "en": saudar_en,
                  "it": saudar_it
                  }
    return func_saudo[lingua]
f = saudar("it") # para dar la referencia a la funcion de saudo
print(f)#solo muestra la referencia
f() #Muestra el valor de la referencia, mostrando CHIAO
saudar("en")() #Otra forma


#Filtrar
l6 = [1,2,3,4]

def es_par(n):
    return n%2 == 0

l2 =  filter(es_par,l6)#compara los números pares similares a los de l6
for n in l2:
    print(n)
#otra forma
l2 = filter(lambda n: n%2 == 0,l6)

#filter,map,reduce importantes en python2 pero prescindibles en python3
#Comprension de listas para sustituir a filter , map , reduce
#Transformaciones
l7 = [1,2,3,4,5]
l3 = [n+1 for n in l7] # le sumamos 1 a cada elemento de l cambia los valores de l3
print(l3)

l4 = [n for n in l7 if n % 2 == 0] # le da a l4 los valores pares de l7
print(l4)


#ignorando los valoes mayores a cuatro transforma los valores de la lista en "+" y "*"
m = ['+', "*"]
z = []
for s in m:
    for n in l7:
        if n<4:
            z.append(n*s)
print(z)

#otra forma con la transformacion
z2 = [n*s for s in m
      for n in l7
      if n<4]
print(z2)

#Generadores
x2 = (n**2 for n in l7)#Objeto generador /esto no es una lista / genera datos en el instante que se necesite
print(x2) # solo da la referencia al generador

#Muestra los numeros del generador
for n in x2:
    print(n)

# Podemos crear nuestros propios generadores
def meu_range(fin ,inicio = 0,salto=1):
        while inicio <= fin :
            yield inicio # retorna o valor pero sigue ejecutando el while a diferencia del return que me sacaria fuera del bucle
            inicio = inicio + salto
x3 = meu_range(100,2,15)

l8 = [n for n in x3] # almacena los numeros generados

#for n in x3:
#    print(n)

print(l8)

#Decoradores , añaden funcionalidades a una función si modificar la original,suelen usarse para testeos de metodos que aun no tienen
def funcion_necesita_decoracion():
    print("Preciso decoracion")

def meu_decorador(funcion_orixinal):
    def funcion_envolvente():
        print("Instruccions de antes da funcion orixinal")
        funcion_orixinal()
        print("Instruccions para despois da funcion orixinal")
    return funcion_envolvente # no se devuelven con parentesis

# Una forma de mostrarla con la decoracion
#funcion_decorada = meu_decorador(funcion_necesita_decoracion) # no le añadimos los parentesis en la variable funcion orixinal
#funcion_decorada()

#Otra forma
@ meu_decorador
def funcion_necesaria_decoracion():
    print("Preciso decoracion")

funcion_necesaria_decoracion()

# AUTORIZAR

autenticado = True
def require_autenticacion(f):
    def funcion_decorada(*args, **kwargs): # Con este codigo de aqui hacemos que la funcion necesite autentificación
        if autenticado:
            return f(*args,**kwargs)
        else:
            print("Erro: O usuario non está autorizado")

    return funcion_decorada

@require_autenticacion # con esta marca damos la autorización
def sauda():
    print("hola")

sauda()
#Tambien con está: require_autentication(sauda)()


#crea un ficheiro añadiendo los datos del calculo de la suma , resta y multiplicación
def log (ficheiro_log):
    def decorador_log(func):
        def decorador_function(*args,**kwargs):
            with open(ficheiro_log,'a') as ficheiro_aberto:
                saida = func(*args, **kwargs)
                ficheiro_aberto.write(f"{saida}\n")
        return decorador_function
    return decorador_log

@log('ficheiro.log')
def suma(a, b):
    return a + b

@log('ficheiro.log')
def resta(a, b):
    return a - b

@log('ficheiro.log')
def mult (a, b):
    return  a * b

suma(1,1)
resta(7,23)
mult(2,9)

log('ficheiro.log')(suma)(2,2) #otra forma para crear la suma, etc



