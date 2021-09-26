import xml.etree.ElementTree as ET
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication
from producto import Producto
from Maquina import Maquina
from Simulacion import Simulacion
from listaSimple import listaSimple
from listaDoble import listaDoble

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.configuracionbutton.clicked.connect(self.loadConfiguracion)
        self.simulacionbutton.clicked.connect(self.loadSimulacion)
        self.maquina = ''
        self.pushButton.clicked.connect(self.inicarSimulacion)

    def loadConfiguracion(self):
        listaLineas = listaSimple()
        listaProductos = listaSimple()
        try:
            ruta = QFileDialog.getOpenFileName(filter='Xml Files (*.xml)')

            tree = ET.parse(ruta[0])
            root = tree.getroot()
 
            for elem in root:
                if elem.tag == 'CantidadLineasProduccion':
                    cantidadLineas = elem.text.strip()
                elif elem.tag == 'ListadoLineasProduccion':
                    for subelem in elem:
                        if subelem.tag == 'LineaProduccion':
                            for subsubelem in subelem:
                                if subsubelem.tag == 'Numero':
                                    numero = subsubelem.text.strip()
                                elif subsubelem.tag == 'CantidadComponentes':
                                    cantidadComponentes = subsubelem.text.strip()
                                else:
                                    tiempoEnsamblaje = subsubelem.text.strip()
                        lineaProduccion = listaDoble(numero, cantidadComponentes,tiempoEnsamblaje)
                        listaLineas.add(lineaProduccion)
                elif elem.tag == 'ListadoProductos':
                    for subelem in elem:
                        if subelem.tag == 'Producto':
                            for subsubelem in subelem:
                                if subsubelem.tag == 'nombre':
                                    nombre = subsubelem.text.strip()
                                elif subsubelem.tag == 'elaboracion':
                                    elaboracion = subsubelem.text
                            producto = Producto(nombre, elaboracion)
                            listaProductos.add(producto)
            self.maquina = Maquina(cantidadLineas,listaLineas,listaProductos)   

            return self.maquina
        except Exception as e:
                print(e)

    def loadSimulacion(self):
        try:
            ruta = QFileDialog.getOpenFileName(filter='Xml Files (*.xml)')

            tree = ET.parse(ruta[0])
            root = tree.getroot()
            listaProductos = listaSimple()
            for elem in root:
                if elem.tag == 'Nombre':
                    nombre = elem.text.strip()
                    self.SimulacionCombo.addItem(nombre)
                elif elem.tag == 'ListadoProductos':
                    for subelem in elem:
                        if subelem.tag == 'Producto':
                            nombreProducto = subelem.text.strip()
                            self.ProductosCombo.addItem(nombreProducto)
                        listaProductos.add(nombreProducto)
            simulacion = Simulacion(nombre, listaProductos)
            return simulacion
        except Exception as e:
                print(e)

    def inicarSimulacion(self):
        try:
            texto = self.ProductosCombo.currentText()
            print('Producto a ensamblar '+texto)
            self.maquina.ensamblar(texto)
        except Exception as e:
            print(e)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ventana()
    GUI.show()
    sys.exit(app.exec_())
