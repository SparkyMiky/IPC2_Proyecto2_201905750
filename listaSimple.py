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

    def delete(self, dato):
        self.size -= 1
        nodoAux = self.cabecera
        if self.cabecera.dato == dato:
            self.cabecera = nodoAux.siguiente
        else:
            while nodoAux.siguiente != None:
                if nodoAux.siguiente.dato == dato:
                    if nodoAux.siguiente.siguiente != None:
                        nodoAux.siguiente = nodoAux.siguiente.siguiente
                    else:
                        nodoAux.siguiente = None                    
    

    def imprimir(self):
        nodoAux = self.cabecera
        while nodoAux != None:
            print(nodoAux.dato)
            nodoAux = nodoAux.siguiente

    def buscar(self, id):
        nodoAux = self.cabecera
        while nodoAux != None:
            if(nodoAux.dato.id == id):
                return nodoAux.dato
            nodoAux = nodoAux.siguiente
        

    
    def buscarP(self, nombre):
        nodoAux = self.cabecera
        while nodoAux != None:
            if(nodoAux.dato.nombre == nombre):
                return nodoAux. dato
            nodoAux = nodoAux.siguiente
        if nodoAux == None:
            return None

    def buscarInstruccion(self, instruccion):
        nodoAux = self.cabecera
        while nodoAux != None:
            if(nodoAux.dato == instruccion):
                return True
            nodoAux = nodoAux.siguiente
        if nodoAux == None:
            return False

    def reset(self):
        nodoAux = self.cabecera
        while nodoAux != None:
            nodoAux.dato.cambioPosicion = False
            nodoAux = nodoAux.siguiente

    def clear(self):
        nodoAux = self.cabecera
        while nodoAux != None:
            nodoAux.dato.clear()
            nodoAux = nodoAux.siguiente
    

