from LineaProduccion import LineaProduccion
from producto import Producto
from listaSimple import listaSimple

class Maquina:
    def __init__(self,cantidadLineas, listaLineaProducciones,listaProductos):
        self.cantidadLineas = cantidadLineas
        self.listaLineaProducciones = listaLineaProducciones
        self.listaProductos = listaProductos

    def ensamblar(self, producto):
        pass
