class Persona:
    """Clase para definir unha persoa"""
    def __init__(self, nome,dni,edade):
        self.nome = nome
        self.dni = dni
        self.edade = self.comprobar_edad(edade)


    def comprobar_edad(self,edad):
        if 0 <= edad < 100:
            return edad
        else:
            return 0



p = Persona("Manuel", "354L",35)
p.edade = -1
print(p.edade)
print(p.nome)


class Posto:
    def __init__(self,tarea,horario,remuneracion,formacion):
        self.tarea = tarea
        self.horario = horario
        self.remuneracion = remuneracion
        self.formacion = formacion

class Traballador (Posto, Persona):
    def __init__(self, nome, dni, edad, tarea, horario, remuneracion,formacion,NUSS):
        super().__init__(nome,dni,edad)
        super().__init__(tarea,horario,remuneracion,formacion)
        self.NUSS = NUSS

        
