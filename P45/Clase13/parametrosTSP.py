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

#Red representad con un diccionario
red = {
    'A':(8,11),
    'B':(7,8),
    'C':(9.5,5),
    'D':(9,7),
    'E':(10,10)
}

red = {
    'Armenia':{'x':8,'y':11},
    'Pereira':{'x':7,'y':8},
    'Cali':{'x':9.5,'y':5},
    'Cartago':{'x':9,'y':7},
    'Manizales':{'x':10,'y':10},
}
#Componente en x del punto A -> redDicccionarioAnidado['A']['x']

#Distancia euclidiana (2D)
def distanciaEUC_2D(punto1,punto2):
    return  int((((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)**(1/2))+0.5)

def distanciaEUC_2D_V2(punto1,punto2):
    return  int((((punto1['x'] - punto2['x'])**2 + (punto1['y'] - punto2['y'])**2)**(1/2))+0.5)

#Función para el cálculo de la matriz de costos
def calcularMatrizCostos(red):
    #Generalizar para calcular todas las posibles conexiones
    matrizCostos = dict()    
    for nombre_i,punto_i in red.items():
        for nombre_j, punto_j in red.items():            
            if nombre_i != nombre_j:
                #costo = int(distanciaEUC_2D(red[nombre_i],red[nombre_j]))
                costo = distanciaEUC_2D_V2(red[nombre_i],red[nombre_j])                
                matrizCostos[ nombre_i+"-"+nombre_j ] = costo
    return matrizCostos


#Matriz de costos de la red
############################

#Ejemplo distancia entre A y B:
distanciaA_B = { 'Armenia-Cali': distanciaEUC_2D_V2(red['Armenia'],red['Cali']) }
print(distanciaA_B)
        
matrizCostos = calcularMatrizCostos(red)
[print(llave,' ',valor) for llave,valor in matrizCostos.items()]

print(matrizCostos)

#Consultar la estrategia del vecino más cercano e intentar implementarla
#sobre esta codificiación del problema

# #Algoritmo o el pseudocódigo del Vecino Más Cercano
# 1) Establecer nodo o ciudad de partida
# 2) Iniciar el itinerario (tour) en la ciudad de partida establecida
# 3) Mientras tengamos ciudades sin cubrir o incluir en el itinerario
# 4)      Desde la última ciudad del itinerario generamos las salidas a las demás ciudades (no cubiertas)
# 5)      Seleccionar la mejor de las salidas
# 6)      Actualizar las ciudades sin cubrir
# 7)      Agregar al itinerio la mejor de las salidas
# 8) Agregar al itinerario el regreso a la ciudad inicial o de partida

#Traducción a Python
print('-----Algoritmo Heurístico del Vecino Más Cercano-----')
ciudadInicial = 'Manizales'
itinerario = list()
itinerario.append(ciudadInicial)
ciudadesSinCubrir = set(red.keys())
ciudadesSinCubrir.remove(ciudadInicial)
while len(ciudadesSinCubrir) > 0:
    listadoSalidas = list()
    for ciudadSalida in ciudadesSinCubrir:
        listadoSalidas.append(  (ciudadSalida, matrizCostos[ itinerario[-1]+'-'+ciudadSalida  ]) )
    listadoSalidas = tuple(listadoSalidas)
    
    
    












