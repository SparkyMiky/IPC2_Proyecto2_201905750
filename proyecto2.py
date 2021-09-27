import xml.etree.ElementTree as ET
import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QTableWidget, QTableWidgetItem
from producto import Producto
from Maquina import Maquina
from Simulacion import Simulacion
from listaSimple import listaSimple
from listaDoble import listaDoble
from Simulacion import Simulacion

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui_app.ui", self)
        self.configuracionbutton.clicked.connect(self.loadConfiguracion)
        self.simulacionbutton.clicked.connect(self.loadSimulacion)
        self.maquina = ''
        self.pushButton.clicked.connect(self.inicarSimulacion)
        self.reportesbutton.clicked.connect(self.crearReportes)
        self.simulaciones = []
        self.simulaciones1 = listaSimple()
        self.SimulacionCombo.currentIndexChanged[str].connect(self.reload)
        self.ayudabutton.clicked.connect(self.showDatos)

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
            self.SimulacionCombo.clear()
            self.ProductosCombo.clear()
            ruta = QFileDialog.getOpenFileName(filter='Xml Files (*.xml)')
            tree = ET.parse(ruta[0])
            root = tree.getroot()
            listaProductos = []

            for elem in root:
                if elem.tag == 'Nombre':
                    nombre = elem.text.strip()
                elif elem.tag == 'ListadoProductos':
                    for subelem in elem:
                        if subelem.tag == 'Producto':
                            nombreProducto = subelem.text.strip()
                        listaProductos.append(nombreProducto)
            simulacion = Simulacion(nombre, listaProductos)
            self.simulaciones.append(simulacion)
            self.simulaciones1.add(simulacion)

            for i in self.simulaciones:
                self.SimulacionCombo.addItem(i.nombre)



        except Exception as e:
                print(e)

    def reload(self):
        try:
            self.ProductosCombo.clear()
            selected = self.SimulacionCombo.currentText()
            simulacion = self.simulaciones1.buscarP(selected)
            for i in simulacion.listaProductos:
                self.ProductosCombo.addItem(i)
        except Exception as e:
            print(e)

    def inicarSimulacion(self):
        try:
            self.label_3.setVisible(False)
            self.tableWidget.clear()
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)

            texto = self.ProductosCombo.currentText()
            datos = self.maquina.ensamblar(texto)

            self.tableWidget.setColumnCount(int(self.maquina.cantidadLineas)+1)
            for i in range(int(self.maquina.cantidadLineas)+1):
                if i == 0:
                    self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem('Tiempo'))
                else:
                    self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem('Linea '+str(i)))
            datos.reverse()
            fila = 0
            for registro in datos:
                columna = 0
                self.tableWidget.insertRow(fila)
                for elemento in registro:
                    if elemento == registro[0]:
                        self.tableWidget.setItem(fila,columna, QTableWidgetItem('Segundo '+elemento))
                    else:
                        self.tableWidget.setItem(fila,columna, QTableWidgetItem(elemento))
                    columna += 1 
            self.show()
            self.label_3.setText('Tiempo optimo: '+str(self.maquina.segundo))
            self.label_3.setVisible(True)

        except Exception as e:
            print(e)
    
    def crearReportes(self):
        try:
            simulacion = self.SimulacionCombo.currentText()
            texto = self.ProductosCombo.currentText()
            self.maquina.crearXml(simulacion, texto)
            self.maquina.crearHtml(texto)
        except Exception as e:
            print(e)       

    def showDatos(self):
        self.label_4.setText('Rony Omar Miguel Lopez, 201905750')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ventana()
    GUI.show()
    sys.exit(app.exec_())
