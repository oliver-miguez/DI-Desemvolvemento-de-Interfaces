# Importa la librería GObject Introspection, necesaria para PyGObject.
import gi

# Especifica que se requiere la versión 3.0 de GTK.
gi.require_version("Gtk", "3.0")
# Importa los módulos GTK (widgets), Gdk (gráficos) y GObject (base).
from gi.repository import Gtk, Gdk, GObject


# Define la clase principal, heredando de Gtk.Window para crear la ventana.
class EjemploTree(Gtk.Window):
    # --- Manejadores de Eventos ---

    # Método que se ejecuta cuando se hace clic en la casilla de la columna 'Falecido'.
    # celda: el Gtk.CellRendererToggle que disparó el evento.
    # fila: la ruta (path) de la fila que se ha alternado.
    # modelo: el Gtk.ListStore (datos) pasado como dato extra.
    def on_celdaFalecido_toogled(self, celda, fila, modelo):
        print('Clicamos en ', fila)
        # Invierte el valor booleano (True/False) en la columna 4 del modelo para esa fila.
        modelo[fila][4] = not modelo[fila][4]

    # Método que se ejecuta cuando el usuario termina de editar la columna de texto 'Nome'.
    # cadroTexto: el nuevo texto introducido por el usuario.
    # numero: el índice de la columna (pasado como dato extra: 1 para 'Nome').
    # modelo: el Gtk.ListStore.
    def on_celdaNome_edited(self, celda, fila, cadroTexto, numero, modelo):
        print("Editamos: ", numero, fila, cadroTexto)
        # Comprueba si la columna editada es la columna 'Nome' (índice 1).
        if numero == 1:
            # Actualiza el valor en la columna 1 ('Nome') de la fila editada.
            modelo[fila][1] = cadroTexto

    # --- Constructor de la Ventana ---
    def __init__(self):
        # Llama al constructor de la clase padre (Gtk.Window).
        super().__init__()
        # Establece el título de la ventana.
        self.set_title("Ejemplo de Treeview en árbol")

        # Crea un contenedor vertical con espacio de 6 píxeles entre elementos.
        caixav = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # Crea el modelo de datos (ListStore) con los tipos de columna:
        # (str Dni, str Nome, int Edade, str Xénero, bool Falecido)
        modelo = Gtk.ListStore(str, str, int, str, bool)

        # Datos iniciales para cargar en la tabla.
        listaUsuarios = [('1234H', 'Ana Perez', 34, 'Muller', False),
                         ('4321T', 'Pepe Diz', 78, 'Home', True)]

        # Itera sobre la lista y añade cada usuario como una fila al modelo.
        for usuario in listaUsuarios:
            modelo.append(usuario)

        # Crea el widget principal de la tabla, asignándole el modelo de datos.
        trvVista = Gtk.TreeView(model=modelo)

        # Configuración de las columnas 0 ('Dni') y 1 ('Nome').
        for i, tituloColumna in enumerate(('Dni', 'Nome')):
            # Renderer para mostrar texto.
            celda = Gtk.CellRendererText()
            # Permite la edición del texto en esta celda.
            celda.set_property("editable", True)
            # Conecta el evento 'edited' al método on_celdaNome_edited.
            # Los argumentos i y modelo se pasan como datos extra.
            celda.connect("edited", self.on_celdaNome_edited, i, modelo)
            # Crea la columna, asociando el renderer 'celda' con el texto de la columna 'i' del modelo.
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            # Añade la columna al TreeView.
            trvVista.append_column(columna)

        # Configuración de la columna 2 ('Edade').
        # Renderer para mostrar una barra de progreso.
        celda = Gtk.CellRendererProgress()
        # Asocia el valor de la barra de progreso con la columna 2 del modelo (la edad, int).
        columna = Gtk.TreeViewColumn('Edade', celda, value=2)
        trvVista.append_column(columna)

        # Configuración de la columna 3 ('Xénero').
        celda = Gtk.CellRendererText()
        # Asocia el texto con la columna 3 del modelo.
        columna = Gtk.TreeViewColumn('Xénero', celda, text=3)
        trvVista.append_column(columna)

        # Configuración de la columna 4 ('Falecido').
        # Renderer para mostrar una casilla de verificación.
        celda = Gtk.CellRendererToggle()
        # Asegura que la casilla sea interactiva.
        celda.set_property("sensitive", True)
        # Conecta el evento 'toggled' al método on_celdaFalecido_toogled, pasando el modelo.
        celda.connect("toggled", self.on_celdaFalecido_toogled, modelo)
        # Asocia el estado activo/inactivo de la casilla con la columna 4 (el booleano).
        columna = Gtk.TreeViewColumn('Falecido', celda, active=4)
        trvVista.append_column(columna)

        # Añade el TreeView a la caja vertical.
        # True, True, 5: Expande y rellena el espacio disponible con un padding de 5.
        caixav.pack_start(trvVista, True, True, 5)

        # Añade la caja vertical (que contiene el TreeView) a la ventana.
        self.add(caixav)
        # Conecta el evento de cierre de ventana a la función Gtk.main_quit.
        self.connect("delete_event", Gtk.main_quit)
        # Muestra todos los widgets.
        self.show_all()


# --- Punto de Ejecución Principal ---
if __name__ == "__main__":
    # Crea una instancia de la ventana.
    EjemploTree()
    # Inicia el bucle principal de GTK para que la ventana se muestre y sea interactiva.
    Gtk.main()