import gi
from gi.repository.Gio import ListStore

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject

class InterfazCompleta(Gtk.Window):
    def __init__(self):
        super().__init__()
        caixaGrid = Gtk.Grid()

        # PRIMERA CAJA
        caixaH = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10) # Caja horizontal que recoge las dos columnas
        caixaV1 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10) # Columna vertical 1
        caixaV2 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10) # Columna vertical 2

        frame = Gtk.Frame() # Crear un elemento para el marco exterior, tipo frame para que tenga un estilo específico
        frame.set_label("Panel") # Añade un nombre al marco

        # Cosas que contendrá "caixaV1"
        store = Gtk.ListStore(str) # Crea una lista de una sola columna que solo aceptara strings
        store.append(["Hola"])
        store.append(["Prueba"])
        store.append(["Otra Cosa"])

        # Crear TreeView para mostrar los datos del ListStore
        treeview = Gtk.TreeView(model=store)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Contido", renderer, text=0)
        treeview.append_column(column)

        caixaV1.pack_start(treeview, True, True, 0)

        caixaH.pack_start(frame, True, True, 10)

        # Botones Redondeados
        button1 = Gtk.RadioButton.new_with_label_from_widget(None, "Button 1")
        caixaV2.add(button1) # Añade los botones a la caja vertical

        button2 = Gtk.RadioButton.new_with_label_from_widget(button1, "Button 2")
        caixaV2.add(button2)

        button3 = Gtk.RadioButton.new_with_label_from_widget(button1, "Button 3")
        caixaV2.add(button3)

        boton = Gtk.Button("Button")
        caixaV2.add(boton)

        contido = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10) # Caja horizontal que recoge las dos columnas

        contido.pack_start(caixaV1, True, True, 10)
        contido.pack_start(caixaV2, True, True, 10)

        frame.add(contido)
        caixaH.pack_start(contido, True, True, 10)

        # SEGUNDA CAJA

        # Tercera Caja

        # Cuarta caja

        # Frame Global
        frameGlobal = Gtk.Frame() # Crea un frame total
        frameGlobal.set_label("PanelCaption")
        frameGlobal.add(caixaH)

        caixaGrid.add(frameGlobal)


        # Para mostrarlo
        self.add(caixaGrid)

        self.connect("delete-event",Gtk.main_quit)
        self.show_all()



if __name__ == "__main__":
    InterfazCompleta()
    Gtk.main()

