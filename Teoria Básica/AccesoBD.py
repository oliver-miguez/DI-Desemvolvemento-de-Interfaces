# DB-API
import sqlite3 as dbapi

print(dbapi.apilevel) # Versión
print(dbapi.threadsafety) # Si su valor es 3, totalmente usable por todos los hilos (Valores entre 0-3), revisar que hace el resto de valores
print(dbapi.paramstyle) # Utiliza el estilo de "?", para sqlite tenemos que construir las consultas con "?", para llamar a los parámetros
try:
    bbdd = dbapi.connect('baseDatos.dat')
    print(bbdd) # Muestra si hay conexion
except dbapi.StandarError:
    print("Erro o abrir a base de datos")
try:
    cursor = bbdd.cursor()
except dbapi.StandarError:
    print("Erro o crear o cursor")
'''
try:
    #cursor.execute("""create table usuarios( dni text, nome text, edade int)""")

    cursor.execute("""insert into usuarios values('1234R','Ana',23)""")
    cursor.execute("""insert into usuarios values('12341231E','Paco',63)""")
    cursor.execute("""insert into usuarios values('4321F','Jacinto',90)""")

    bbdd.commit()

except dbapi.DatabaseError as e:
    print("Error ao crear a taboa",e)
'''
try:
    cursor.execute("""Select dni, nome, edade From usuarios Where dni = ?""",('1234R',))
    for rexistro in cursor.fetchall():
        print("Dni: ", rexistro[0])
        print("Nome",rexistro[1])
        print("Edad",rexistro[2])
except dbapi.DatabaseError as e:
    print("Error al recibir los datos de la base ",e)

bbdd.close()
