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

class Traballador (Persona):
    def __init__(self, nome, dni, edad, NUSS, salario, formacion):
        super().__init__(nome,dni,edad)
        self.NUSS = NUSS
        self.salario = salario
        self.formacion = formacion