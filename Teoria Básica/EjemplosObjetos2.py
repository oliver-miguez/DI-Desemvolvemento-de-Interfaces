'''
"""
Otra forma de plantear el super()
"""
class Persona:
    """Clase para definir una persona"""
    def __init__(self,nome,dni,edade,**outros):
        self.nome = nome
        self.dni = dni
        self.edade = self.comprobarEdade(edade)

    def comprobarEdade(self,edade):
        if (edade>=0) and edade <100:
            return edade #id
        else:
            return 0

class Posto:
    def __init__(self,tarea,horario,salario,formacion,**outros):
        self.tarea = tarea
        self.horario = horario
        self.salario = salario
        self.formacion = formacion

class Trabajador (Persona,Posto):
    def __init__(self,nome,dni,edade,tarea,horario,salario,formacion,NUSS):
        super().__init__(nome=nome,dni=dni,edade=edade,tarea=tarea,horario=horario,salario=salario,formacion=formacion) #aqui el super recoge de las dos clases
        self.NUSS = NUSS

t2 = Trabajador("Juan",5679,45,"Soldador",7,2300,"CM","13515/UN")
print(t2.nome)
'''


#POLIMORFISMO
#Encapsulacion
class Persona3:
    """Clase para definir una persona con encapsulación"""

    def __init__(self, nome, dni, edade):
        self.__nombre = nome #el __ lo hace "Private" entre comillas
        self.__dni = dni
        self.__edad = edade # Usamos el setter automáticamente

    # Getter de nombre
    def getNombre(self):
        return self.__nombre

    # Setter de nombre
    def setNombre(self, nombre):
        self.__nombre = nombre

    # Getter de edad
    def getEdad(self):
        return self.__edad

    # Setter de edad
    def setEdad(self, edad):
        if 0 <= edad < 100:
            self.__edad = edad
        else:
            self.__edad = 0

    # Getter de DNI
    def getDni(self):
        return self.__dni

    # Setter de DNI
    def setDni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.__dni = dni
        else:
            self.__dni = ""

    def __str__(self):
        return "Nome: "+ self.nombre + " \nDni: "+ self.dni

    def __eq__(self, other):
        print("Propio:"+ self.dni)
        print("Outro: "+ other.dni)
        return self.dni == self.__dni

    def __ne__(self,other):
        return self.dni != other.dni

    def __len__(self):
        return 3


    # Creación de propiedades para controlar el acceso
    nombre = property(getNombre, setNombre)
    edad = property(getEdad, setEdad)
    dni = property(getDni, setDni)


p3 = Persona3("Pepe", "36456789", 19)
p4 = Persona3("Pepe", "36456789", 19)
print(p3.dni)
#p3.dni = "12345678X"  # Si se cambia y no cumple la condicion del set no funciona
print(p3.dni)
p3.edad = 120 # Intenta asignar una edad inválida
print(p3.edad) # El setter lo corrige a 0
print(p3._Persona3__dni)#otra forma
print(p3)

print(p3==p4) #como solo tenemos comparado el dni , si el dni coincide a pesar de que el resto no será siempre true
print(p3.__len__()) # retorna 3

lista = []
print(lista.__len__()) #retorna 0 porque no tiene valores añadidos la lista / las listas tienen su propio len