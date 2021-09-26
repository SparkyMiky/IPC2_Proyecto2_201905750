from listaSimple import listaSimple
from nodoDoble import nodoDoble

class listaDoble:
    def __init__(self, id, cantidadComponentes, tiempoEnsamblaje):
        self.cabecera = None
        self.ultimo = None
        self.id = id
        self.cantidadComponentes = int(cantidadComponentes)
        self.tiempoEnsamblaje = tiempoEnsamblaje
        self.size = 0
        self.rellenar(self.cantidadComponentes)
        self.posicionBrazo = 0
        self.cambioPosicion = False
        self.nodoActual = ''
        self.ensamblados = listaSimple()

    def add(self, dato):
        self.size += 1
        nodoAux = nodoDoble(dato)
        if self.cabecera == None:
            self.cabecera = nodoAux
            self.ultimo = nodoAux
        else:
            self.ultimo.siguiente = nodoAux
            self.ultimo.siguiente.anterior = self.ultimo
            self.ultimo = nodoAux

    def rellenar(self, cantidadComponentes):
        j = 1
        for i in range(cantidadComponentes):
            self.add(j)
            j += 1

    def imprimir(self):
        nodoAux = self.cabecera
        while nodoAux != None:
            print(nodoAux.dato.id)
            nodoAux = nodoAux.siguiente

    def buscar(self, id):
        nodoAux = self.cabecera
        while nodoAux != None:
            if(nodoAux.dato.id == id):
                return nodoAux. dato
            nodoAux = nodoAux.siguiente
        if nodoAux == None:
            return None

    def avanzar(self):
        self.posicionBrazo += 1
        if self.nodoActual == '':
            self.nodoActual = self.cabecera
        else:
            self.nodoActual = self.nodoActual.siguiente

    def retroceder(self):
        self.posicionBrazo -= 1
        self.nodoActual = self.nodoActual.anterior

    def clear(self):
        self.ensamblados = listaSimple()
        self.posicionBrazo = 0