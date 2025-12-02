import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject


class ExemploGrid(Gtk.Window):
    def __init__(self):
        listaCabeceiraAlbara = ['Código','Descripción','Cantidade', 'Prezo ud', 'Prezo Total']
        listaDetalleAlbara = [['00012','descripcion',100,0.004,0.2],
                              ['00013', 'descripcion2', 200, 0.003, 0.3],
                              ['00014', 'descripcion3', 300, 0.002, 0.4],
                              ['00015', 'descripcion4', 400, 0.001, 0.5]]

        builder = Gtk.Builder()
        builder.add_from_file("Glade2.glade")
        wndPrincipal = builder.get_object("wndPrincipal")
        trvDetalleAlbará = builder.get_object("trvDetalleAlbará")
        sinais= {"on_wdnPrincipal_delete": Gtk.main_quit,
                 "on_cmbNumAlbara_changed": self.on_cmbNumAlbara_changed,
                 "on_btnEngadir_clicked": self.on_btnEngadir_clicked,
                 "on_btnEditar_clicked": self.on_btnEditar_clicked,
                 "on_btnBorrar_clicked": self.on_btnBorrar_clicked,
                 "on_btnAceptar_clicked": self.on_btnAceptar_clicked,
                 "on_btnCancelar_clicked": self.on_btnCancelar_clicked}
        builder.connect_signals(sinais)

        modelo = Gtk.ListStore(str,str,int,float,float)
        for entrada in listaDetalleAlbara:
            modelo.append(entrada)
        trvDetalleAlbará.set_model(modelo)



        for i, columna in enumerate (listaCabeceiraAlbara):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(columna,celda,text = i)
            trvDetalleAlbará.append_column(columna)

        '''
        OTRA FORMA    
        for i in range (len(listaCabeceiraAlbara)):
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn(columna,celda,text = i)
        '''


    def on_cmbNumAlbara_changed(self,combo):
        pass
    def on_btnEngadir_clicked(self,boton):
        pass
    def on_btnEditar_clicked(self,boton):
        pass
    def on_btnBorrar_clicked(self,boton):
        pass
    def on_btnAceptar_clicked(self,boton):
        pass
    def on_btnCancelar_clicked(self,boton):
        pass
if __name__ == "__main__":
    ExemploGrid()
    Gtk.main()