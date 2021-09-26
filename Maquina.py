from LineaProduccion import LineaProduccion
from producto import Producto
from listaSimple import listaSimple

class Maquina:
    def __init__(self,cantidadLineas, listaLineaProducciones,listaProductos):
        self.cantidadLineas = cantidadLineas
        self.listaLineaProducciones = listaLineaProducciones
        self.listaProductos = listaProductos

    def ensamblar(self, producto):
        prod = self.listaProductos.buscar(producto)
        instrucciones = prod.inst()
        print (instrucciones)

        complete = False
        a = 0
        while complete:
            for i in instrucciones:
                banderaComponente = False
                buffer = ''
                for c in i:
                    if c == 'C':
                        linea = buffer
                        buffer = ''
                        banderaComponente = True
                    elif banderaComponente == False:
                        buffer += c
                    else:
                        buffer += c
                componente = buffer




