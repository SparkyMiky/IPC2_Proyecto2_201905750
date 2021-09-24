import xml.etree.ElementTree as ET
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication
from LineaProduccion import LineaProduccion
from producto import Producto
from Maquina import Maquina
from Simulacion import Simulacion
from listaSimple import listaSimple

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.configuracionbutton.clicked.connect(self.loadConfiguracion)
        self.simulacionbutton.clicked.connect(self.loadSimulacion)

    def loadConfiguracion(self):
        listaLineas = listaSimple()
        listaProductos = listaSimple()
        try:
            ruta = QFileDialog.getOpenFileName(filter='Xml Files (*.xml)')
            archivo = open(ruta[0], 'r')
            contenido = archivo.read()
            archivo.close()
            self.contenido = contenido
            print(self.contenido)

            tree = ET.parse(f)
            root = tree.getroot()
 
            for elem in root:
                if elem.tag == 'CantidadLineasProduccion':
                    cantidadLineas = elem.text
                elif elem.tag == 'ListadoLineasProduccion':
                    for subelem in elem:
                        if subelem.tag == 'LineaProduccion':
                            for subsubelem in subelem:
                                if subsubelem.tag == 'Numero':
                                    numero = subsubelem.text
                                elif subsubelem.tag == 'CantidadComponentes':
                                    cantidadComponentes = subsubelem.text
                                else:
                                    tiempoEnsamblaje = subsubelem.text
                        lineaProduccion = LineaProduccion(numero, cantidadComponentes,tiempoEnsamblaje)
                        listaLineas.add(lineaProduccion)
                elif elem.tag == 'ListadoProductos':
                    for subelem in elem:
                        if subelem.tag == 'Producto':
                            for subsubelem in subelem:
                                if subsubelem.tag == 'nombre':
                                    nombre = subsubelem.text
                                elif subsubelem.tag == 'elaboracion':
                                    elaboracion = subsubelem.text
                                producto = Producto(nombre, elaboracion)
                                listaProductos.add(producto)
                maquina = Maquina(cantidadLineas,listaLineas,listaProductos)

            return maquina
        except Exception as e:
                pass

    def loadSimulacion(self):
        try:
            ruta = QFileDialog.getOpenFileName(filter='Xml Files (*.xml)')
            archivo = open(ruta[0], 'r')
            contenido = archivo.read()
            archivo.close()
            self.contenido = contenido
            print(self.contenido)

            tree = ET.parse(f)
            root = tree.getroot()
            listaProductos = listaSimple()
            for elem in root:
                if elem.tag == 'Nombre':
                    nombre = elem.text
                elif elem.tag == 'ListadoProductos':
                    for subelem in elem:
                        if subelem.tag == 'Producto':
                            nombreProducto = subelem.text
                        listaProductos.add(nombreProducto)
                simulacion = Simulacion(nombre, listaProductos)
            return simulacion
        except Exception as e:
                pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ventana()
    GUI.show()
    sys.exit(app.exec_())
