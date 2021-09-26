from nodoLista import nodoLista

class listaSimple:
    def __init__(self):
        self.cabecera = None
        self.ultimo = None
        self.size = 0

    def add(self, dato):
        self.size += 1
        nodoAux = nodoLista(dato)
        if self.cabecera == None:
            self.cabecera = nodoAux
            self.ultimo = nodoAux
        else:
            self.ultimo.siguiente = nodoAux
            self.ultimo = nodoAux

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
    

