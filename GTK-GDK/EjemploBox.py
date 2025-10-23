import gi
import CaixaCor
gi.require_version("Gtk","3.0")
from gi.repository import Gtk


class EjemploBox(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de uso de box layout")

        caixa = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10)
        caixav1 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 10)

        # 1º Elemento de "Caixa"
        caixav1.pack_start(CaixaCor.CaixaCor('red'), True, True, 5)
        caixav1.pack_start(CaixaCor.CaixaCor('blue'), True, True, 5)
        caixav1.pack_start(CaixaCor.CaixaCor('green'), True, True, 5)

        caixa.pack_start(caixav1,True,True,5) # Añade a la caja la primera vertical

        caixa.pack_start(CaixaCor.CaixaCor('Yellow'), True, True, 5) # Añade una caja central

        # 2º Elemento de "Caixa"
        caixav2 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 10)
        caixav2.pack_start(CaixaCor.CaixaCor('orange'), True, True, 5)
        caixav2.pack_start(CaixaCor.CaixaCor('purple'), True, True, 5)

        caixa.pack_start(caixav2,True,True,5) # Añade a la caja la segunda vertical

        self.add(caixa) # Añade a "Caixa a la pantalla"
        self.connect("delete-event",Gtk.main_quit) # Necesario
        self.show_all() # Muesta la pantalla

# Ejecuta la ventana
if __name__ == "__main__":
    EjemploBox()
    Gtk.main()

