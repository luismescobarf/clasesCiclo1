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
# 2) Coleccionarlas las transferencias de los cajeros solicitados
# 3) Obtener las que se realizaron en el último trimestre (Marzo, Abril y Mayo de 2021)

#Traducción a Python con enfoque declarativo:

# 1) Sacar la información de los cajeros modelo 101 y 2017
def esModelo101(modelo):
    return modelo==101

def esModelo2017(modelo):
    return modelo==2017

def cajerosModelosRequeridos(modelo):
    return any([esModelo101(modelo), esModelo2017(modelo)])

print('Cajeros con toda la información de los modelos solicitados')
listadoCajerosModelos = list(filter( lambda x: cajerosModelosRequeridos(x[1]['modeloCajero']), caso1.items() ))
pp.pprint(listadoCajerosModelos)
print('Número de cajeros con el modelo solicitado->',len(listadoCajerosModelos))

# #Diccionario
# palabra = "hola"
# diccionario = dict( zip(range(len(palabra)),palabra)  )
# pp.pprint(diccionario)

# #Llaves, valores, o los ítems (llave,valor)
# print( diccionario.keys() )
# print( diccionario.values() )
# print( diccionario.items() )







