
import threading
class Maquina:
    def __init__(self,cantidadLineas, listaLineaProducciones,listaProductos):
        self.cantidadLineas = cantidadLineas
        self.listaLineaProducciones = listaLineaProducciones
        self.listaProductos = listaProductos
        self.segundo = ''
        self.datos = ''

    def ensamblar(self, producto):
        prod = self.listaProductos.buscarP(producto)
        instrucciones = prod.inst()
        self.listaLineaProducciones.clear()

        self.segundo = 0
        ensamblando = False
        self.datos = []
        
        try:
            while len(instrucciones) != 0:
                self.added = ''
                self.segundo += 1
                tupla=()
                fila = [str(self.segundo)]
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
                                self.segundo += (lineaProduccion.tiempoEnsamblaje-1)
                                self.added = lineaProduccion.tiempoEnsamblaje
                                lineaProduccion.ensamblados.add(i)
                                ensamblando = True
                                lineaProduccion.cambioPosicion = True
                            else:
                                lineaProduccion.cambioPosicion = True
                    else:
                        continue 
                if ensamblando == True:
                    fila[0] = str(self.segundo-self.added)+' - '+str(self.segundo)

                    instrucciones.pop(0)
                    ensamblando = False
                    
                tupla = tuple(fila)
                self.datos.append(tupla)
                

                
            return self.datos
        except Exception as e:
            print(e)

    def escribirArchivo(self,ruta, contenido):
        archivo = open(ruta, 'w')
        archivo.write(contenido)
        archivo.close()

    def crearXml(self, simulacion, producto):
        inicio = '<SalidaSimulacion>\n\t<Nombre>\n\t\t'+simulacion+'\n\t</Nombre>\n\t<Producto>\n\t<Nombre>\n\t\t'+producto+'\n\t</Nombre>\n\t<TiempoTotal>\n\t\t'+str(self.segundo)+'\n\t<TiempoTotal>\n\t<ElaboracionOptima>\n'
        segundo = 1
        self.datos.reverse()
        for i in self.datos:
            linea = 0
            for j  in i:
                if j == i[0]:
                    linea += 1
                    continue
                else:
                    inicio += '\t\t<Tiempo NoSegundo="'+str(i[0])+'">\n\t\t\t<LineaEnsamblaje NoLinea="'+str(linea)+'">\n\t\t\t\t'+i[linea]+'\n\t\t\t</LineaEnsamblaje>\n'
                linea += 1
            segundo += 1
        fin = '\t\t\t</Tiempo>\n\t\t</ElaboracionOptima>\n\t</Producto>\n</SalidaSimulacion>'
        self.escribirArchivo(producto+'.xml',inicio + fin)
        

    def crearHtml(self,producto):
        try:
            inicio = '<!DOCTYPE html><html lang="en"><head><style type="text/css"><title>Reportes</title></style></head><body><center><h1>'+producto+'</h1></center><center>'
            inicio += '<p><table border="1" bordercolor="#000000" cellpadding="10" cellspacing="0"><caption>"Tabla de Simualacion"</caption>'
            i=0
            inicio += '<tr>'
            while i<=int(self.listaLineaProducciones.size):
                if i == 0:
                    inicio += '<th> Tiempo </th>'
                else:
                    inicio += '<th> Linea '+str(i)+' </th>'
                i += 1
            inicio += '</tr>'

            for i in self.datos:
                inicio += '<tr>'
                for j in i:
                    if j == i[0]:
                        inicio += '<td> Segundo '+str(j)+'</td>'
                    else:
                        inicio += '<td>'+j+'</td>'
                inicio += '</tr>'  
            inicio += '<h2> Tiempo total utilizado'+str(self.segundo)+' </h2>'          
            fin = '</center></body></html>'
            self.escribirArchivo(producto+'.html',inicio+fin)
        except Exception as e:
            print(e)

    def crearGraphviz(self):
        pass





