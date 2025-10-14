import sys
import Ventana2
from  PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)

"""
Ventana 1 del programa
"""
class Ventana1 (QMainWindow):

    """
    Modifica el texto principal y vacía el valor de la barra donde se introducen datos
    """
    def on_btnSaudo_clicked(self):
        nome = self.txtSaudo.text() # crea una variable nome con formato de texto
        if self.txtSaudo.text() != "": # si es nulo el valor introducido
            if self.txtSaudo.text().isdigit(): # o es un número
                self.txtSaudo.clear() # muestra un error
                self.lblEtiqueta.setText("Nome non permitido")
            else:
                self.txtSaudo.clear() # Si no muestra un texto con el nombre añadido
                self.lblEtiqueta.setText("Ola "+ nome + " encantado/a de coñecerte")

    """
    Permite cambiar de ventana
    """
    def cambio_ventana(self):
        if self.ventana_secundaria is None: # si la referencia a la otra ventana  es nula
            self.ventana_secundaria = Ventana2.Ventana2(self) # crea una referencia a la otra ventara
        self.hide() # se oculta la ventana 1
        self.ventana_secundaria.show() # muestra la ventana 2

    """
    Se ejecuta cuando se presiona el botón mayúsculas
    """
    def boton_mayusculas_presionado(self):
        pass
        # TODO , por acabar

    """
    Define la estructura de la ventana
    """
    def __init__(self):
        super().__init__()

        self.ventana_secundaria = None # Referencia para usar en "cambio_ventana"

        self.setWindowTitle("Ventana 1") # Titulo de la ventna
        self.setMinimumSize(500,300) # Tamaño de la ventana

        self.lblEtiqueta = QLabel("Ola a todos") # Primer label, cambia cuando este se modifica

        fonte = self.lblEtiqueta.font() # Administrar la fuente de letra
        fonte.setPointSize(30) # Tamaño de la letra
        self.lblEtiqueta.setFont(fonte) # Proporciona a self ese tamaño de letra
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignHCenter) # Ajustar el texto, centrarlo
        self.lblEtiqueta.setText("Ola a todos") # Muestra un texto

        self.txtSaudo = QLineEdit() # Para la introducción de texto por una barra

        self.txtSaudo.setPlaceholderText("Introduce un texto") # Texto que muestra la barra de introducción de texto
        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)

        btnSaudo = QPushButton ("Saudo") # Crea un botón con ese nombre
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked) # Crea una conexión con la función "on_btnSaudo_clicked"

        btnCambio = QPushButton("Cambiar") # Botón para cambiar de escena
        btnCambio.clicked.connect(self.cambio_ventana) # Crea una conexión con la función "cambio_ventana"

        btnMayusculas = QPushButton("Mayúsculas")
        btnMayusculas.setCheckable(True)
        btnMayusculas.toggle().connect(self.boton_mayusculas_presionado)
        self.mayusculas = True

        caixaV = QVBoxLayout() # Almacenar

        # Añade a la ventana los elementos anteriores
        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaudo)
        caixaV.addWidget(btnSaudo)
        caixaV.addWidget(btnCambio)

        container = QWidget() # Almacenar
        container.setLayout(caixaV)
        self.setCentralWidget(container)

        self.show() # Muestra la ventana

"""
Ejecuta la ventana
"""
if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    fiestra = Ventana1()
    aplication.exec()
