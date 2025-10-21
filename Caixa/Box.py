import sys
import  CaixaCor

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget, QLabel

"""
Posibles colores:
   "aquaMarine"
    "blue"
    "green"
    "grey"
"""


"""
Ventana del ejercicio de Esentia, bloques coloreados
"""
class Box(QMainWindow): # QMainWindow, es la base de la ventana principal, donde colocar menús, barras, etc.
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Box")  # Título de la ventana

        caixaH = QHBoxLayout()

        # Bloque 1
        caixaV1 = QVBoxLayout()
        caixaV1.addWidget(CaixaCor.CaixaCor("blue"))
        caixaV1.addWidget(CaixaCor.CaixaCor("green"))
        caixaV1.addWidget(CaixaCor.CaixaCor("red"))
        caixaH.addLayout(caixaV1)

        caixaH.addWidget(CaixaCor.CaixaCor("yellow"))

        # Bloque 2
        caixaV2 = QVBoxLayout()
        caixaV2.addWidget(CaixaCor.CaixaCor("pink"))
        caixaV2.addWidget(CaixaCor.CaixaCor("aquaMarine"))
        caixaH.addLayout(caixaV2)

        # Creamos una referencia a un widget y le damos como layout a "CaixaH"
        # De esa manera podremos observar los bloques coloreados
        wid = QWidget()
        wid.setLayout(caixaH)
        self.setCentralWidget(wid)

        self.show()

if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    ventana = Box()
    aplication.exec()
