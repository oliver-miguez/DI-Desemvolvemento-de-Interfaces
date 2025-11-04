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

        # Crear TreeView para mostrar los datos del ListStore(siempre igual)
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

        #Boton que siempre aparece al final del cuadro
        boton = Gtk.Button(label = "Button")
        caixaV2.pack_end(boton,False,False,2)

        # Recoge el contenido de las cajas verticales
        contido = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10) # Caja horizontal que recoge las dos columnas

        contido.pack_start(caixaV1, True, True, 10)
        contido.pack_start(caixaV2, True, True, 10)

        # Lo añade al frame "Panel"
        frame.add(contido)
        caixaH.pack_start(frame, True, True, 10)

        # SEGUNDA CAJA
        caixaTag = Gtk.Notebook() # Crea un contenedor con tags
        caixaH2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10) # Caja horizontal que recoge el contenedor de Tags

        caixaTag.set_border_width(5) # Establece el tamaño de cada uno de los tab

        # Añadiendo objetos a la ventana de Gtk.Notebook 1
        caixaVChkButtons = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10) # Columna vertical para los botones
        almacenBotones = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 10) # Almacena los botones check
        caixaTab1 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)

        # Botones checkeables
        check_button1 = Gtk.CheckButton(label = "Boton 1")
        check_button2 = Gtk.CheckButton(label = "Boton 2")
        check_button3 = Gtk.CheckButton(label = "Boton 3")
        check_button3.set_sensitive(False) # Deshabilita el botón 3

        # Los guarda para luego mostrarlos
        caixaVChkButtons.add(check_button1)
        caixaVChkButtons.add(check_button2)
        caixaVChkButtons.add(check_button3)

        # Barra que se mueve(no se como llamarla)
        slider = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 1)
        caixaTab1.pack_end(slider,False,False,2)


        # Los recoge en el almacén de botones
        almacenBotones.add(caixaVChkButtons)

        caixaTab1.add(almacenBotones) # Pagina 1

        caixaTag.append_page(caixaTab1) # Añade al notebook la primera ventana

        # Añade la caja que recoge todos los valores de notebook en una caja horizontal
        # Para colocarla al lado de la primera caja
        caixaH2.add(caixaTag)


        # Tercera Caja

        # Cuarta caja

        # Frame Global
        frameGlobal = Gtk.Frame() # Crea un frame total
        frameGlobal.set_label("PanelCaption")

        # Recoge cada una de las cajas de esta interfaz y las muestra
        contenedorGlobal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        contenedorGlobal.pack_start(caixaH,True,True,10)
        contenedorGlobal.pack_start(caixaH2,True,True,10)

        # Las añade al frame global para que se integre al cuadro "PanelCaption"
        frameGlobal.add(contenedorGlobal)

        # Muestra lo integrado hasta ahora
        caixaGrid.add(frameGlobal)

        # Para mostrarlo
        self.add(caixaGrid)

        self.connect("delete-event",Gtk.main_quit)
        self.show_all()



if __name__ == "__main__":
    InterfazCompleta()
    Gtk.main()

