import re

class Producto:
    def __init__(self, nombre, elaboracion):
        self.nombre = nombre
        self.elaboracion = elaboracion
        self.instrucciones = []

        i = 0
        estado = 0
        buffer = ''
        instruccion = False
        for c in elaboracion:
            if estado == 0:
                if c == 'L':
                    instruccion = True
                elif re.search('\d', c):
                    buffer += c
                elif c == 'C':
                    buffer += c
                elif c == 'p':
                    continue
                else:
                    if instruccion == True:
                        self.instrucciones.append(buffer)
                        buffer = ''
                        instruccion = False

    def inst(self):
        return self.instrucciones