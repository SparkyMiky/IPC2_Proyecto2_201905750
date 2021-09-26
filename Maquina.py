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

        segundos = 0
        ensamblando = False
        try:
            while len(instrucciones) != 0:
                segundos += 1
                print('Analizando el segundo '+str(segundos)+'----------------------------------------')
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
                            print('Linea '+linea+' avanzando hacia componente '+str(lineaProduccion.posicionBrazo))
                        elif lineaProduccion.posicionBrazo > componente:
                            lineaProduccion.retroceder()
                            lineaProduccion.cambioPosicion = True
                            print('Linea '+linea+' retrocediendo hacia componente '+str(lineaProduccion.posicionBrazo))
                        else:
                            if i == instrucciones[0] and ensamblando == False:
                                print("Linea "+linea+' esta ensamblando')
                                lineaProduccion.ensamblados.add(i)
                                ensamblando = True
                                lineaProduccion.cambioPosicion = True
                            else:
                                print('Linea '+linea+' no esta haciendo nada')
                                lineaProduccion.cambioPosicion = True
                    else:
                        continue

                if ensamblando == True:
                    instrucciones.pop(0)
                    ensamblando = False
        except Exception as e:
            print(e)




