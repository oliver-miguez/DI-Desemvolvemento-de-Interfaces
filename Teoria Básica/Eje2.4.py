"""
 Utilice o programa anterior para xerar unha táboa de conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10.
"""

def conversion():
    fare = 0
    while fare <= 120:
        grados = (fare - 32) * 5 / 9
        fare += 10
        print(grados)
conversion()

