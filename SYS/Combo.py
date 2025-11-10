import sys
from mimetypes import inited

import ModeloLista
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QListView, QListWidget, QComboBox, QTextEdit, QGridLayout)

"""
Aprendiendo a usar el ComboBox en Python Qt
"""
class Combo(QMainWindow):
    """
    Metodo principal del programa
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo combobox QT")
        maia = QGridLayout() # Grid para colocar ordenadamente los layout

        self.nome_dni = [['Ana','Pepe','Juan'],['33333R','222222W','111111J']]

        caixaV = QVBoxLayout() # Sirve para crear cada una de las cajas que tienen sus diferentes funcionalidades

        txtCadro1 = QLineEdit() # Bloque donde podemos escribir texto
        txtCadro2 = QLineEdit() # Bloque donde podemos escribir texto

        self.cmbComboBox = QComboBox() # Lista desplegable
        #self.cmbComboBox.addItems(("hola","que","tal","estas")) # Añade estos texto al comboBox, OJO ponerlos entre paréntesis porque .addItems pide tuples no strings
        self.cmbComboBox.addItems(self.nome_dni[0]) # Otra forma de hacerlo con una lista de tuples
        self.cmbComboBox.currentIndexChanged.connect(self.on_cmbComboBox_currentIndexChanged) # Que ocurre cuando seleccionamos un objeto del comboBox
        self.cmbComboBox.currentTextChanged.connect(self.on_cmbComboBox_currentTextChanged)

        caixaV.addWidget(txtCadro1)  # Añade en el primer cuadro, tanto el texto 1 el 2 y el desplegable
        caixaV.addWidget(txtCadro2)
        caixaV.addWidget(self.cmbComboBox)
        maia.addLayout(caixaV,1,0,1,1) # Como caixaV es layout tiene que ser addLayout

        self.txeAreaTexto = QTextEdit() # Area donde podremos introducir texto
        maia.addWidget(self.txeAreaTexto,1,1,1,1) # Aquí como txtArea no es un layout, se le añade con widget



        # MOSTRAR LO DISEÑADO ANTERIORMENTE(OBLIGATORIO)
        aux = QWidget()
        aux.setLayout(maia)
        self.setCentralWidget(aux)
        self.show()


    """
    Lo que ocurre cuando seleccionamos una opción del ComboBox
    Al seleccionar una opción mostrará tanto el nombre del usuario como su DNI
    indice: indice de cada una de las opciones del comboBox
    """
    def on_cmbComboBox_currentIndexChanged(self, indice):
        print(self.cmbComboBox.itemText(indice)) # Muestra por consola la opción escogida del comboBox
        self.txeAreaTexto.setPlainText("Has seleccionado el usuario: "+ self.cmbComboBox.itemText(indice)+ " con el dni: "+ self.nome_dni[1][indice] ) # Muestra en el bloque de texto el texto seleccionado del comboBox


    """
    Muestra el usuario seleccionado
    texto: recoge el valor del string del indice seleccionado del comboBox
    """
    def on_cmbComboBox_currentTextChanged(self, texto):
        print("El combo tiene seleccionado el elemento: "+ texto)


# EJECUTA LA VENTANA(OBLIGATORIO)
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Combo()
    aplicacion.exec()