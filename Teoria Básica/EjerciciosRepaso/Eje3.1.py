"""
Exercicio 3.1. Escribir dúas funciones que permitan calcular:
A cantidade de segundos nun tempo dado en horas, minutos e segundos.
A cantidade de horas, minutos e segundos dun tempo dado en segundos.
"""

def segundos(hora,minuto,segundos):
    h = hora * 3600
    m = minuto * 60
    oper = h + m + segundos
    print("La hora en segundos es: ", oper)

segundos(15,54,17)
def a_segundos(segundos):
    horas = 0
    minutos = 0
    while segundos > 59:
        minutos += 1
        segundos -= 60

    while minutos > 59:
        horas += 1
        minutos -= 60

    print("horas:", horas,"minutos: ",minutos, "segundos:", segundos)

a_segundos(20000)