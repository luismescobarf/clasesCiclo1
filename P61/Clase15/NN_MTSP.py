import sys

#Requerimiento: recibimos una colección de coordenadas
# de los nodos que constituyen una red o grafo, y se requiere
# obtener la matriz de distancias correspondientes para cómputos
# de optimización

#Alternativas de codificación

#1) Lista de listas representando la red:
#La lista general es la red y cada posición de la lista
#son los nodos.

#Estrictamente listas
red = [
    ['A',8,11],
    ['B',7,8],
    ['C',9.5,5],
    ['D',9,7],
    ['E',10,10],
]

#Lista de listas y la coordenada es una tupla
red = [
    ['A',(8,11)],
    ['B',(7,8)],
    ['C',(9.5,5)],
    ['D',(9,7)],
    ['E',(10,10)],
]

#Lista de tuplas que contienen la pareja ordenada en una tupla
red = [
    ('A',(8,11)),
    ('B',(7,8)),
    ('C',(9.5,5)),
    ('D',(9,7)),
    ('E',(10,10)),
]
#print(red[0][1][0])

#Red representad con un diccionario
red = {
    'A':(8,11),
    'B':(7,8),
    'C':(9.5,5),
    'D':(9,7),
    'E':(10,10)
}

redDiccionarioAnidado = {
    'A':{'x':8,'y':11},
    'B':{'x':7,'y':8},
    'C':{'x':9.5,'y':5},
    'D':{'x':9,'y':7},
    'E':{'x':10,'y':10},
}
#Componente en x del punto A -> redDicccionarioAnidado['A']['x']

#Distancia euclidiana 2D -> TSP recibiendo los puntos como tuplas o listas 
def distanciaEUC_2D(punto1,punto2):
    return  int((((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)**(1/2))+0.5)

#Distancia euclidiana 2D -> TSP recibiendo los puntos como diccionarios
def distanciaEUC_2D_V2(punto1,punto2):
    return  int((((punto1['x'] - punto2['x'])**2 + (punto1['y'] - punto2['y'])**2)**(1/2))+0.5)

#Generar un iterable o colección o contenedor con todas las posibles conexiones que hay en la red
#Red o grafo completo (Todos con Todos)

#Ejemplo de representación de la matriz de distancias (cientos de km)
coleccionConexiones = {
    'Armenia-Pereira':1,
    'Armenia-Cali':4,
    'Armenia-Manizales':2
    #.
    #.
    #.
}

#Variaciones de la representación de la red
redSesion = [
    {'nombre':'Armenia','x':8,'y':11},
    {'nombre':'Pereira','x':7,'y':8},
    {'nombre':'Cali','x':9.5,'y':5},
    {'nombre':'Cartago','x':9,'y':7},
    {'nombre':'Manizales','x':10,'y':10},
]

# #Consultas sobre la red
# print('Autonumérico:',redSesion[0])
# print('Detalle de las coordenadas->','coordenada en x del punto:',redSesion[0]['x'])
# print('Detalle de las coordenadas->','nombre del punto:',redSesion[0]['nombre'])

#Algoritmo (Pseudocódigo)
# 0) Inicializar contenedores
# 1) Para cada i-ésimo nodo de la red:
# 2)  Para cada j-ésimo nodo de la red:
# 3)      Si i diferente de j:
# 4)            Agregar a la colección de conexiones la conexión de i a j (EUC2d -> TSP)

#Traducción a Python
conexiones = dict()
for i,nodo_i in enumerate(redSesion):
    for j,nodo_j in enumerate(redSesion):
        if i != j:
            conexiones[ nodo_i['nombre']+"-"+nodo_j['nombre'] ] = distanciaEUC_2D_V2(nodo_i,nodo_j)

#Revisar diccionario de conexiones
# [print(conexion) for conexion in conexiones.items()]
# print(conexiones)
import pprint as pp
pp.pprint(conexiones)

#Queremos saber la distancia entre Cartago y Manizales:
print('Distancia consultada Cartago-Manizales: ', conexiones['Cartago-Manizales'])

#Construir solución TSP -> Vecino más cercano (pseudocódigo o algoritmo)
# 1) Seleccionar un punto para iniciar itinerario.
# 2) Mientras haya ciudades sin cubrir:
# 3)      Obtener todas las salidas desde la última ciudad agregada al itinerario a las ciudades sin cubrir
# 4)      Ordenar las salidas desde la última ciudad
# 5)      Agregar la "mejor" salida al itinerario
# 6) Agregar el retorno a la primera ciudad
# 7) Mostrar itinerario

#Construir solución mTSP -> Vecino más cercano limitando los viajes (pseudocódigo o algoritmo)
# 1) Iniciar programación de itinerarios (coleccionar itinerarios o jornadas TSP).
# 2) Seleccionar un punto para iniciar itinerario.
# 3) Mientras haya ciudades sin cubrir:
# 4)      Obtener todas las salidas desde la última ciudad agregada al itinerario actual a las ciudades sin cubrir
# 5)      Identificar la "mejor" salida
# 6)      Si es viable (carga de trabajo) agregar la ciudad al itinerario:
# 7)            Agregar la "mejor" salida al itinerario actual
# 8)      De lo contrario:
# 9)            Cierre el itinerario actual
# 10)            Agregarlo a la programación de itinerario o jornadas (colección)
# 11)            Abrir un nuevo itinerario con la mejor salida
# 12) Revisar si hay un itinerario pendiente no cerrado, cerraro y agregarlo en las jornadas







# 5)      Agregar la "mejor" salida al itinerario
# 6) Agregar el retorno a la primera ciudad
# 7) Mostrar itinerario



#Traducción a Python
print('----Algoritmo Vecino Más Cercano (NN Nearest Neighbour)')
itinerario = list()#Lista con los nombres de las ciudades o puntos
ciudadInicial = redSesion[-1]['nombre']#Selecciono una ciudad inicial arbitraria
itinerario.append(ciudadInicial)
ciudadesSinCubrir = set()
for ciudad in redSesion:
    if ciudad['nombre'] != ciudadInicial:
        ciudadesSinCubrir.add(ciudad['nombre'])
#Salida de diagnóstico
# print('Itinerario->',itinerario)
# print('Ciudades Sin Cubrir ->',ciudadesSinCubrir)
while len(ciudadesSinCubrir) > 0: #Mientras haya ciudades sin cubrir:
    listadoSalidas = list()
    for ciudadPendiente in ciudadesSinCubrir:
        llaveConexion = itinerario[-1] + '-' + ciudadPendiente
        listadoSalidas.append( (ciudadPendiente, conexiones[llaveConexion]) )
    # #Salida diagnóstico
    # print('Listado Salidas:',listadoSalidas)
    # sys.exit(1)

    #Seleccionar la mejor salida
    mejorSalida = listadoSalidas[0]
    for salida in listadoSalidas[1:]:
        if mejorSalida[1] >= salida[1]:
            mejorSalida = salida

    #Agregar la mejor
    itinerario.append(mejorSalida[0])

    #Actualizamos el conjunto de control
    ciudadesSinCubrir.remove(mejorSalida[0])

#Agregamos el retorno
itinerario.append(ciudadInicial)

#Mostrar el itinerario generado
print('Itinerario: ',itinerario)

















