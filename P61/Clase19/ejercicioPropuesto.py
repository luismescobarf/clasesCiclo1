from casosGenerados import *
import pprint as pp

#1)Obtener todas las transferencias realizadas en el último trimestre en los cajeros
#de modelo 101,2017
#2)Obtener todas las consignaciones realizadas en el último trimestre en los cajeros
#de modelo 101,2017 que se encuentran fuera de servicio
#3) Todas las transacciones de los cajeros cerrados que pertenecen a la firma integrada
# -> Convencional: Ciclando y con condicionales
# -> Funcional: Map, Filter, Zip o Reduce

# #Ejemplo de acceso
# print(caso1['25u8sBP']['transacciones'][0])

# print('Llaves del dataset (diccionario)')
# print(caso1.keys())

# print('Llaves del dataset (diccionario)')
# print(caso1['25u8sBP'].keys())


#1)Obtener todas las transferencias realizadas en el último trimestre en los cajeros
#de modelo 101,2017

#Algoritmo (Pseudocódigo)
#1) Obtener los cajeros (con toda su información) de los modelos solicitados
#2) Extraer las transacciones de esos cajeros de los modelos solicitados
#3) Filtrar las transferencias (solamente este tipo de transacciones interesan para el requerimiento)
#4) Filtramos las transferencias del último trimestre (marzo, abril y mayo de 2021)

#Imperativa
def req1Imperativa(caso):

    #Contenedor o colección que va a recibir las transferencias
    listaTransacciones = list()

    #Recorrer todos los cajeros
    for idCajero, infoCajero in caso.items():
        #Filtrar los cajeros de los modelos que nos interesan
        if infoCajero['modeloCajero']==101 or infoCajero['modeloCajero']==2017:            
            for transaccion in infoCajero['transacciones']:
                #Filtrar las transferencias de las transacciones
                if transaccion['tipoMovimiento'] == 'transferencia':
                    #Filtrar aquellas transferencias que correpsonden al último trimestre
                    if transaccion['fechaMovimiento'][3:] == '03-2021' or transaccion['fechaMovimiento'][3:] == '04-2021' or transaccion['fechaMovimiento'][3:] == '05-2021':
                        listaTransacciones.append(transaccion)
    return listaTransacciones#Retornamos el contenedor

#Declarativa

def req1DeclarativaV3(caso):

    from functools import reduce

    #Traducción del algoritmo planteado
    #1) Obtener los cajeros (con toda su información) de los modelos solicitados 101 y 2017

    #Filtrar -> Predicado e iterable (colección)

    def cajeroModelosSolicitados(cajero):
        #return cajero[1]['modeloCajero']==101 or cajero[1]['modeloCajero']==2017
        return any([cajero[1]['modeloCajero']==101,cajero[1]['modeloCajero']==2017])   

    #2) Extraer las transacciones de esos cajeros de los modelos solicitados  

    def obtenerTransacciones(tuplaInfoCajeros):
        return tuplaInfoCajeros[1]['transacciones']
    
    #3) Filtrar las transferencias (solamente este tipo de transacciones interesan para el requerimiento) 

    def esTransferencia(transaccion)  :
        return transaccion['tipoMovimiento']=='transferencia'     

    #4) Filtramos las transferencias del último trimestre (marzo, abril y mayo de 2021) (03-2021,04-2021,05-2021)
    def esDelUltimoTrimestre(transaccion):
        fecha = transaccion['fechaMovimiento']
        return any([ fecha[3:]=='03-2021', fecha[3:]=='04-2021', fecha[3:]=='05-2021' ])

    #Aplicar todos los pasos y retornar el iterable del requerimiento
    return filter(esDelUltimoTrimestre,filter(esTransferencia,  reduce(lambda acumulador=list(), elemento=dict(): acumulador + elemento , map(obtenerTransacciones, filter(cajeroModelosSolicitados,caso.items())))))    

def req1DeclarativaV2(caso):

    #Traducción del algoritmo planteado
    #1) Obtener los cajeros (con toda su información) de los modelos solicitados 101 y 2017

    #Filtrar -> Predicado e iterable (colección)

    def cajeroModelosSolicitados(cajero):
        #return cajero[1]['modeloCajero']==101 or cajero[1]['modeloCajero']==2017
        return any([cajero[1]['modeloCajero']==101,cajero[1]['modeloCajero']==2017])

    cajerosSeleccionados = filter(cajeroModelosSolicitados,caso.items())
    #pp.pprint(cajerosSeleccionados)
    #print(cajerosSeleccionados)

    #2) Extraer las transacciones de esos cajeros de los modelos solicitados
    listaListasTransacciones = map(lambda x:x[1]['transacciones'],cajerosSeleccionados)
    #pp.pprint(listaListasTransacciones)
    from functools import reduce
    listaTransacciones = reduce(lambda acumulador=list(), elemento=dict(): acumulador + elemento ,listaListasTransacciones)
    #pp.pprint(listaTransacciones)

    #3) Filtrar las transferencias (solamente este tipo de transacciones interesan para el requerimiento)
    transferencias = filter(lambda x:x['tipoMovimiento']=='transferencia',  listaTransacciones)
    #pp.pprint(transferencias)

    #4) Filtramos las transferencias del último trimestre (marzo, abril y mayo de 2021) (03-2021,04-2021,05-2021)
    def esDelUltimoTrimestre(transaccion):
        fecha = transaccion['fechaMovimiento']
        return any([ fecha[3:]=='03-2021', fecha[3:]=='04-2021', fecha[3:]=='05-2021' ])

    listadoRequerimiento = filter(esDelUltimoTrimestre,transferencias)

    #Retorno de la colección con la información solicitada en el requerimiento
    return listadoRequerimiento

def req1Declarativa(caso):

    #Traducción del algoritmo planteado
    #1) Obtener los cajeros (con toda su información) de los modelos solicitados 101 y 2017

    #Filtrar -> Predicado e iterable (colección)

    def cajeroModelosSolicitados(cajero):
        #return cajero[1]['modeloCajero']==101 or cajero[1]['modeloCajero']==2017
        return any([cajero[1]['modeloCajero']==101,cajero[1]['modeloCajero']==2017])

    cajerosSeleccionados = list(filter(cajeroModelosSolicitados,caso.items()))
    #pp.pprint(cajerosSeleccionados)
    #print(cajerosSeleccionados)

    #2) Extraer las transacciones de esos cajeros de los modelos solicitados
    listaListasTransacciones = list(map(lambda x:x[1]['transacciones'],cajerosSeleccionados))
    #pp.pprint(listaListasTransacciones)
    from functools import reduce
    listaTransacciones = list(reduce(lambda acumulador=list(), elemento=dict(): acumulador + elemento ,listaListasTransacciones))
    #pp.pprint(listaTransacciones)

    #3) Filtrar las transferencias (solamente este tipo de transacciones interesan para el requerimiento)
    transferencias = list( filter(lambda x:x['tipoMovimiento']=='transferencia',  listaTransacciones))
    #pp.pprint(transferencias)

    #4) Filtramos las transferencias del último trimestre (marzo, abril y mayo de 2021) (03-2021,04-2021,05-2021)
    def esDelUltimoTrimestre(transaccion):
        fecha = transaccion['fechaMovimiento']
        return any([ fecha[3:]=='03-2021', fecha[3:]=='04-2021', fecha[3:]=='05-2021' ])

    listadoRequerimiento = list( filter(esDelUltimoTrimestre,transferencias) )

    #Retorno de la colección con la información solicitada en el requerimiento
    return listadoRequerimiento

#Llamados a las funciones de consulta
print('Solución Declarativa')
resDeclarativa = req1Declarativa(caso1)
pp.pprint(resDeclarativa)
print('Solución Imperativa')
resImperativa = req1Imperativa(caso1)
pp.pprint(resImperativa)

print('Comparación Consultas')
print('OK Num de Transferencias') if len(resDeclarativa)==len(resImperativa) else print('ERROR Num de Transferencias')
print('OK Mismo Contenido') if resDeclarativa==resImperativa else print('ERROR Contenido')

print('Solución Declarativa Sin Conversiones')
resDeclarativa2 = req1DeclarativaV2(caso1)
pp.pprint(list(resDeclarativa2))

print('Solución Declarativa Sin Conversiones Aplicando la función a los iterables resultantes')
resDeclarativa3 = req1DeclarativaV3(caso1)
pp.pprint(list(resDeclarativa3))


