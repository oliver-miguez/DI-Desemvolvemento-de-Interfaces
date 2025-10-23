import sys
import  CaixaCor

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget, QLabel, QGridLayout

"""
Ventana del ejercicio de Esentia, bloques coloreados
"""
class ExemploGrid(QMainWindow): # QMainWindow, es la base de la ventana principal, donde colocar menús, barras, etc.
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid")  # Título de la ventana

        maia = QGridLayout() # Crear una malla (Grid)
        maia.addWidget(CaixaCor.CaixaCor("red")) # Le damos un color al primer objeto

        #El resto de objetos + su forma de estructurarse:
        #(widget,fila,columna,filas_ocupadas,columnas_ocupadas)
        maia.addWidget(CaixaCor.CaixaCor("blue"),0,1,1,2)
        maia.addWidget(CaixaCor.CaixaCor("green"),1,0,2,1)
        maia.addWidget(CaixaCor.CaixaCor("pink"),1,1,1,2)
        maia.addWidget(CaixaCor.CaixaCor("orange"),2,1,1,1)
        maia.addWidget(CaixaCor.CaixaCor("yellow"),2,2,1,1)

        # Contenedor que recoge todos los objetos anteriores
        wid = QWidget()
        # Los añade a "wid"
        wid.setLayout(maia)
        # Añade wid al widgetCentral, para que se vea por pantalla
        self.setCentralWidget(wid)
        # Muestra la ventana
        self.show()

if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    ventana = ExemploGrid()
    aplication.exec()
