"""
Exercicio 7.1. Escribir unha función que reciba unha tupla de elementos e indique si se encontran ordenados de menor a maior ou non.
"""
tupla_datos = 1,2,3,4,5

def orden(tupla):
    primer_numero = 0
    for num in tupla:
        primer_numero = tupla[0]
        if num >= primer_numero:
            primer_numero = num
            print("De momento ordenada")
        else:
            print("no esta ordenada")
            break

orden(tupla_datos)