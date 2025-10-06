"""
Exercicio 2.3. Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius. Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.
"""

grados = 28
def conversion(grado):
    f = (grado - 32) * (5/9)
    print(f)
conversion(grados)
