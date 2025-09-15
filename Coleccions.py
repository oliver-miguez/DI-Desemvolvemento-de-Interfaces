"""
Coleccións:

1ºListas
2ºTuplas
3ºDiccionarios

"""

#Listas

l = [23,"Bugario",1,"Hola",[1,2,3,45],-123,-12,2, 3 +4j, True, 1+2,1.2]
print(type(l))
print(l)

l[1] = "Bugario Brugs" #substituye el 2º valor de la lista por el nuevo
l[-2] = False

print(l[1]) #imprime el 2 valor de la lista
print(l[-2]) #imprime el 3 valor empezando por el final