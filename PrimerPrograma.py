#Tipos de Comentarios

#Comentario simple
"""
Este é un comentario multiliña
onde podemos escribir calquera
texto que desexamos
"""

'''
Os comentarios multiliña ou de documantación
tamén funcionan con comiñas simples
'''
# 1º NUMEROS EN PYTHON

#Enteiros
numEnteiros = 5
print(type(numEnteiros))

#Coma Flotante
numDecimal = 5.6
numDecimal2 = 0.1e-5
print(type(numDecimal))
print(type(numDecimal2))

#Booleanos
booleano = True #El True o el False siempre van en mayúscula
print(type(booleano))
#Complexos
complexo = 2.3 + 9.3j
print(type(complexo)) #Type sirve para imprimir el tipo de la variable

#Cadeas
#Las comillas, se pueden usar tanto comillas simples como comillas dobles
cadea  = "Esto é unha cadea marcada con comillas 'dobles'"
cadea2 = 'Esto é unha cadea marcada con comillas "simples"'
print(cadea)
print(cadea2)


#OPERADORES ARITMÉTICOS
# + -> Suma
# - -> Resta o negación
# * -> Multiplicación
# / -> División
# ** -> Exponente (DEVUELVE DECIMALES)
# // DivisiónEntera (NO DEVUELVE DECIMALES)
# % Tanto por ciento (DEVUELVE  EL RESTO)



#OPERADORES ARITMÉTICOS
# + -> Suma
# - -> Resta o negación
# * -> Multiplicación
# / -> División
# ** -> Exponente (DEVUELVE DECIMALES)
# // DivisiónEntera (NO DEVUELVE DECIMALES)
# % Tanto por ciento (DEVUELVE  EL RESTO)


#OPERADORES A NIVEL DE BIT
# & -> And
# | -> Or
# ^ -> Xor (Es una tabla especial, buscarla)
# ~ -> Not (~2)

# >> -> Sirve para dividir, no redondea, se divide por potencias de 2 ( 2, 4, 8, 16, 32, 64)
#print(5>>2) = 2  -> Divide 5 entre 4 sin devolver el resto
#print (10 >> 2) -> Divide 10 entre 4
#print(20>>4) = 1 -> Divide 20 entre 8
#print(5>>2) -> 5 * 4

# << -> Sirve para multiplicar, Se multiplica por potencias de 2 ( 2, 4, 8, 16, 32, 64)
#print(5 << 5) -> 5 * 32

#OPERAORES DE CADEA
cad = "un"
cad2 ="dous"

print(cad + cad2)
print(cad*10)