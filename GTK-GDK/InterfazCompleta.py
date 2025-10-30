import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject

class InterfazCompleta(Gtk.Window):
    def __init__(self):
        super().__init__()

        # Primera Caja
        caixaH = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10) # Caja horizontal que recoge las dos columnas
        caixaV1 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10) # Columna vertical 1
        caixaV1 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10) # Columna vertical 2

        frame = Gtk.Frame() # Crear un elemento para el marco exterior, tipo frame para que tenga un estilo específico
        frame.set_label("Panel") # Añade un nombre al marco
        caixaH.pack_start(frame, True, True, 10) # Lo añade a "caixaH" con un padding de 10

        # Segunda Caja

        # Tercera Caja

        # Cuarta caja

        # Para mostrarlo
        self.add(caixaH)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    InterfazCompleta()
    Gtk.main()

