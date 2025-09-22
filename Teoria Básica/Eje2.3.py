"""
Exercicio 2.3. Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius. Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.
"""


def conversion():
    fare = 0
    while fare <= 120:
        grados = (fare - 32) * 5 / 9
        fare += 10
        print(grados)
conversion()


