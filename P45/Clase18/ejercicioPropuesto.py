from casosGenerados import *

#1)Obtener todas las transferencias realizadas en el último trimestre en los cajeros
#de modelo 101,2017
#2)Obtener todas las consignaciones realizadas en el último trimestre en los cajeros
#de modelo 101,2017 que se encuentran fuera de servicio
#3) Todas las transacciones de los cajeros cerrados que pertenecen a la firma integrada
# -> Convencional: Ciclando y con condicionales
# -> Funcional: Map, Filter, Zip o Reduce

#Visualizar por consola de una forma organizada y automática
import pprint as pp

#Extraer la información de un cajero
#pp.pprint(caso1['25u8sBP'])

# #Extraer transacciones del cajero
# print(type(caso1['25u8sBP']['transacciones']))
# pp.pprint(caso1['25u8sBP']['transacciones'])

#Primera transacción del cajero
# print('Primera transacción del cajero')
# print(caso1['25u8sBP']['transacciones'][0])

#1)Obtener todas las transferencias realizadas en el último trimestre en los cajeros
#de modelo 101,2017

# Algoritmo para (1)
# 1) Sacar la información de los cajeros modelo 101 y 2017
# 2) Coleccionar las transacciones de los cajeros de los modelos solicitados.
# 3) Filtrar las transferencias de las transacciones
# 4) Obtener las transacciones que se realizaron en el último trimestre (Marzo, Abril y Mayo de 2021)

#Traducción a Python con enfoque declarativo:

def requerimiento1(caso):

    # 1) Sacar la información de los cajeros modelo 101 y 2017
    def esModelo101(modelo):
        return modelo==101

    def esModelo2017(modelo):
        return modelo==2017

    def cajerosModelosRequeridos(modelo):
        return any([esModelo101(modelo), esModelo2017(modelo)])

    #print('Cajeros con toda la información de los modelos solicitados')
    cajerosModelo = list(filter( lambda x: cajerosModelosRequeridos(x[1]['modeloCajero']), caso.items() ))
    #cajerosModelo = list(filter( lambda x: x[1]['modeloCajero']==101 or x[1]['modeloCajero']==2017), caso1.items() ))
    #pp.pprint(cajerosModelo)
    #print('Número de cajeros con el modelo solicitado->',len(cajerosModelo))

    # #Diccionario
    # palabra = "hola"
    # diccionario = dict( zip(range(len(palabra)),palabra)  )
    # pp.pprint(diccionario)

    # #Llaves, valores, o los ítems (llave,valor)
    # print( diccionario.keys() )
    # print( diccionario.values() )
    # print( diccionario.items() )

    # 2) Coleccionar las transacciones de los cajeros de los modelos solicitados.

    listaListasTransacciones=list(map(lambda x:x[1]['transacciones'],cajerosModelo))
    #pp.pprint(listaListasTransacciones)

    #Concatenar los elementos de cada lista en una sola lista

    #Con un reduce
    from functools import reduce
    listaTransacciones = reduce( lambda acumulador=list(), elemento=dict() : acumulador + elemento, listaListasTransacciones )
    # pp.pprint(listaTransacciones)

    # 3) Filtrar las transferencias de las transacciones
    #transferencias = list(filter(lambda x:x['tipoMovimiento']=='transferencia',listaTransacciones))

    def esTransferencia(transaccion):
        return transaccion['tipoMovimiento']=='transferencia'

    transferencias = list(filter(esTransferencia,listaTransacciones))

    # print('Listado de transferencias')
    # pp.pprint(transferencias)

    # 4) Obtener las transacciones que se realizaron en el último trimestre (Marzo, Abril y Mayo de 2021)
    def perteneceAlUltimoTrimestre(transaccion):
        #Trimestre actual va desde 03-2021, 04-2021 y 05-2021 (marzo, abril y mayo)
        fecha = transaccion['fechaMovimiento']
        return any( [ fecha[3:]=='03-2021', fecha[3:]=='04-2021', fecha[3:]=='05-2021' ] )

    transferenciasUltimoTrimestre = tuple(filter(perteneceAlUltimoTrimestre,transferencias))
    # print()
    # print()
    # print()
    # print("Respuesta del requerimiento")
    # pp.pprint(transferenciasUltimoTrimestre)

    #Retornar la información extraída
    return transferenciasUltimoTrimestre


#Consulta del requerimiento 1 aplicada a varios casos
print('-------------Caso1')
print(requerimiento1(caso1))

print('-------------Caso2')
print(requerimiento1(caso2))









