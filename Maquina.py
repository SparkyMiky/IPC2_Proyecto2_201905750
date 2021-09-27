
import threading
class Maquina:
    def __init__(self,cantidadLineas, listaLineaProducciones,listaProductos):
        self.cantidadLineas = cantidadLineas
        self.listaLineaProducciones = listaLineaProducciones
        self.listaProductos = listaProductos

    def ensamblar(self, producto):
        prod = self.listaProductos.buscarP(producto)
        instrucciones = prod.inst()
        print(instrucciones)
        self.listaLineaProducciones.clear()

        segundo = 0
        ensamblando = False
        datos = []
        try:
            while len(instrucciones) != 0:
                segundo += 1
                tupla=()
                fila = ['Segundo '+str(segundo)]
                for i in range(self.listaLineaProducciones.size):
                    fila.append('No hacer nada')
                
                
                self.listaLineaProducciones.reset()

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
                    componente = int(buffer)

                    lineaProduccion = self.listaLineaProducciones.buscar(linea)
                    if lineaProduccion.cambioPosicion == False and lineaProduccion.ensamblados.buscarInstruccion(i) != True:
                        if lineaProduccion.posicionBrazo < componente:
                            lineaProduccion.avanzar()
                            lineaProduccion.cambioPosicion = True
                            fila[int(linea)] = " Mover brazo - componente "+str(lineaProduccion.posicionBrazo)
                        elif lineaProduccion.posicionBrazo > componente:
                            lineaProduccion.retroceder()
                            lineaProduccion.cambioPosicion = True
                            fila[int(linea)] = " Mover brazo - componente "+str(lineaProduccion.posicionBrazo)
                        else:
                            if i == instrucciones[0] and ensamblando == False:
                                fila[int(linea)] = " ensamblando - componente "+str(lineaProduccion.posicionBrazo)
                                segundo += (lineaProduccion.tiempoEnsamblaje-1)
                                lineaProduccion.ensamblados.add(i)
                                ensamblando = True
                                lineaProduccion.cambioPosicion = True
                            else:
                                lineaProduccion.cambioPosicion = True
                    else:
                        continue 
                tupla = tuple(fila)
                datos.append(tupla)
                

                if ensamblando == True:
                    instrucciones.pop(0)
                    ensamblando = False
            return datos
        except Exception as e:
            print(e)




