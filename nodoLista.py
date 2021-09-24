class nodoLista:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def getDato(self):
        return self.dato

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, nodoLista):
        self.siguiente = nodoLista