#Funcións

def nome_da_funcion(parametro1,parametro2):
    #Instruccions
    print("parametro1:",parametro1)
    print("parametro2:",parametro2)

nome_da_funcion(4,2)
nome_da_funcion(parametro2=4.5,parametro1="Esto cambia el orden de aparción del parámetro")

def repetir_mensaxe(mensaxe, veces = 1):
    print(mensaxe * veces)

#Si a la hora de llamar a la función no especificamos el total de voces por defecto pondra 1 tal y como la creamos en la función ( voces = 1 )
repetir_mensaxe("Ola ",5)