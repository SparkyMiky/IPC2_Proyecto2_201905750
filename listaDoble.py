from nodoDoble import nodoDoble

class listaDoble:
    def __init__(self, id, cantidadComponentes, tiempoEnsamblaje):
        print('creando lista doble')
        self.cabecera = None
        self.ultimo = None
        self.id = id
        self.cantidadComponentes = int(cantidadComponentes)
        self.tiempoEnsamblaje = tiempoEnsamblaje
        self.size = 0
        self.rellenar(self.cantidadComponentes)
        self.posicionBrazo = 0

    def add(self, dato):
        print('rellenando')
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
            print(nodoAux.dato.nombre)
            nodoAux = nodoAux.siguiente

    def buscar(self, nombre):
        nodoAux = self.cabecera
        while nodoAux != None:
            if(nodoAux.dato.nombre == nombre):
                return nodoAux. dato
            nodoAux = nodoAux.siguiente
        if nodoAux == None:
            return None