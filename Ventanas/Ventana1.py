import sys
import Ventana2
from  PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox)

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
                #self.lblEtiqueta.setText("Ola "+ nome + " encantado/a de coñecerte")
                self.lblEtiqueta.setText(nome)

    """
    Permite cambiar de ventana
    """
    def cambio_ventana(self):
        if self.ventana_secundaria is None: # si la referencia a la otra ventana  es nula
            self.ventana_secundaria = Ventana2.Ventana2(self) # crea una referencia a la otra ventana
        self.hide() # se oculta la ventana 1
        self.ventana_secundaria.show() # muestra la ventana 2

    """
    MUDADO A on_chk_mayusculas_toogled
    Se ejecuta cuando se presiona el botón mayúsculas
    Transforma la etiqueta a mayúsculas
    
    def boton_mayusculas_presionado(self):
        if self.btnMayusculas.isChecked(): # Si está seleccionado el botón de mayúsculas
            self.lblEtiqueta.setText(self.lblEtiqueta.text().upper()) # Transforma el texto en mayúscula
            self.mayusculas = True
        else:
            self.lblEtiqueta.setText(self.lblEtiqueta.text().lower()) # Transforma el texto en minúscula
            self.mayusculas = False
    """

    """
    De pendiendo si es o no mayúscula permite escribir SOLO en mayúscula o SOLO en minúscula
    """
    def on_btnSaudo_text_change(self):
        if self.mayusculas:
            self.txtSaudo.setText(self.txtSaudo.text().upper())
        else:
            self.txtSaudo.setText(self.txtSaudo.text().lower())

    """
    Es lo mismo que el método mudado pero ahora en vez de un botón normal es un check
    """
    def on_chk_mayusculas_toogled(self):
        if self.chkMaiusculas.isChecked(): # Si está seleccionado el botón de mayúsculas
            self.lblEtiqueta.setText(self.lblEtiqueta.text().upper()) # Transforma el texto en mayúscula
            self.txtSaudo.setText(self.txtSaudo.text().upper())
            self.mayusculas = True
        else:
            self.lblEtiqueta.setText(self.lblEtiqueta.text().lower()) # Transforma el texto en minúscula
            self.txtSaudo.setText(self.txtSaudo.text().lower())
            self.mayusculas = False

    """
    Define la estructura de la ventana
    """
    def __init__(self):
        super().__init__()

        # Referencias
        self.ventana_secundaria = None # Referencia para usar en "cambio_ventana"

        # Configuración de tamaño y título de esta ventana
        self.setWindowTitle("Ventana 1") # Título de la ventana
        self.setMinimumSize(500,300) # Tamaño de la ventana

        # Configuración del label inicial
        self.lblEtiqueta = QLabel("OLA A TODOS!") # Primer label, cambia cuando este se modifica
        fonte = self.lblEtiqueta.font() # Administrar la fuente de letra
        fonte.setPointSize(30) # Tamaño de la letra
        self.lblEtiqueta.setFont(fonte) # Proporciona a self ese tamaño de letra
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignHCenter) # Ajustar el texto, centrarlo
        self.lblEtiqueta.setText("OLA A TODOS E TODAS!") # Muestra un texto

        # Metodo para la introducción de texto por una barra
        self.txtSaudo = QLineEdit()

        # Configuración de la barra de introducción de datos
        self.txtSaudo.setPlaceholderText("Introduce un texto") # Texto que muestra la barra de introducción de texto
        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)
        self.txtSaudo.textChanged.connect(self.on_btnSaudo_text_change)
        
        # Configuración del botón de saudo
        btnSaudo = QPushButton ("Saudo") # Crea un botón con ese nombre
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked) # Crea una conexión con la función "on_btnSaudo_clicked"
        
        # Configuración del botón de cambiar ventana
        btnCambio = QPushButton("Cambiar") # Botón para cambiar de escena
        btnCambio.clicked.connect(self.cambio_ventana) # Crea una conexión con la función "cambio_ventana"

        """
        MUDAMOS ESTE BOTON POR chkMaiusculas
        # Configuración del botón de mayúsculas
        self.btnMayusculas = QPushButton("Mayúsculas")
        self.btnMayusculas.setCheckable(True) # le añadimos un self para verificar su estado en otros métodos
        self.btnMayusculas.setChecked(True)
        self.btnMayusculas.toggled.connect(self.boton_mayusculas_presionado)
        self.mayusculas = True
        """
        # Configuración del check de mayúsculas
        # En vez de ser un botón como el anterior ( el mudado ) es un recuadro de check
        self.chkMaiusculas = QCheckBox("MAYÚSCULAS")
        self.chkMaiusculas.setChecked(True) # Aparece de principio seleccionado
        self.chkMaiusculas.toggled.connect(self.on_chk_mayusculas_toogled)
        self.mayusculas = True

        # Almacenar el contenido de botones, labels , etc
        caixaV = QVBoxLayout()

        # Añade a la ventana los elementos anteriores
        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaudo)
        caixaV.addWidget(btnSaudo)
        caixaV.addWidget(btnCambio)
        #caixaV.addWidget(self.btnMayusculas) # Metodo mudado
        caixaV.addWidget(self.chkMaiusculas)

        # Almacena todos los caixaV
        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)

        # Muestra la ventana
        self.show()

"""
Ejecuta la ventana
"""
if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    fiestra = Ventana1()
    aplication.exec()
