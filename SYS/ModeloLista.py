import sys

from PyQt6.QtCore import  Qt, QAbstractListModel

class ModeloFollas (QAbstractListModel):
    def __init__(self, follas = None):
        super().__init__()

        self.follas = follas or [] # Si me pasan un valor, guardamos valor , si no creamos una lista

    # Devuelve la información de la lista de "self.follas"
    # Indice: es obligatorio
    # Rol: Lo que hará --> DisplayRole(Según modelo ViewModel, este sirve para mostrar el texto principal de una celda o elemento,
    # DecorationRole, EditRole, ToolTipRole
    def data(self,indice,rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            texto = self.follas [indice.row()]
            return texto

    # Cuenta los datos almacenados en la lista de "self.follas"
    # Devuelve la dimensión de la lista
    def rowCount(self, indice):
        return len(self.follas)