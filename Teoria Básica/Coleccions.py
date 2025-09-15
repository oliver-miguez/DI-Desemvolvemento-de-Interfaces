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

t = (2,5,2+4j, "Bugario", (22,3,5,6),3,9) #Cuando esto se declara asi , no se puede modificar
#t[2] = "mondongo" -> NO FUNCIONA, ya que intenta cambiar un valor, n
