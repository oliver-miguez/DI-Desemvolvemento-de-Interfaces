#Funcións

def nome_da_funcion(parametro1,parametro2):
    #Instruccions
    print("parametro1:",parametro1)
    print("parametro2:",parametro2)

nome_da_funcion(4,2)
nome_da_funcion(parametro2=4.5,parametro1="Esto cambia el orden de aparción del parámetro")

#para indicar parametros que poden ir de poucos a infinitos usamos o "*" , en estos casos el tipo de valor que representa son tuplas
def repetir_mensaxe(mensaxe, veces = 1, *mais_mesaxes):
    print(type(mais_mesaxes))
    print("temos un total de", str(len(mais_mesaxes)), "parametros extra")
    print(mensaxe * veces)
    for outraMensaxe in mais_mesaxes:
        print(outraMensaxe * veces)

#Si a la hora de llamar a la función no especificamos el total de voces por defecto pondra 1 tal y como la creamos en la función ( voces = 1 )
repetir_mensaxe("Ola ",6,"adeus ","benvido ","python ","java ","godot",3.5)

def persoa (nome,dni,**mais_datos):
    print("O nome é:",nome)
    print("O DNI é:",dni)
    for dato in mais_datos.keys():
        print("O dato ",dato,"é ",mais_datos[dato])
persoa("oliver","7862",fecha = 2, nCasa = 17,apelido = "miguez")