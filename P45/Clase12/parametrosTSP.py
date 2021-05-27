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

redDiccionarioAnidado = {
    'A':{'x':8,'y':11},
    'B':{'x':7,'y':8},
    'C':{'x':9.5,'y':5},
    'D':{'x':9,'y':7},
    'E':{'x':10,'y':10},
}
#Componente en x del punto A -> redDicccionarioAnidado['A']['x']

#Distancia euclidiana (2D)
def distanciaEUC_2D(punto1,punto2):
    return  ((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)**(1/2)

def distanciaEUC_2D_V2(punto1,punto2):
    return  ((punto1['x'] - punto2['x'])**2 + (punto1['y'] - punto2['y'])**2)**(1/2)

#Función para el cálculo de la matriz de costos
def calcularMatrizCostos(red):
    #Generalizar para calcular todas las posibles conexiones
    matrizCostos = dict()
    M = 99999999
    for nombre_i,punto_i in red.items():
        for nombre_j, punto_j in red.items():
            costo = int()
            if nombre_i != nombre_j:
                #costo = int(distanciaEUC_2D(red[nombre_i],red[nombre_j]))
                costo = int(distanciaEUC_2D_V2(red[nombre_i],red[nombre_j]))                
                matrizCostos[ nombre_i+"-"+nombre_j ] = costo
            #else:
            #    costo = M
    return matrizCostos


#Matriz de costos de la red
############################

#Ejemplo distancia entre A y B:
distanciaA_B = { 'A-B': int(distanciaEUC_2D(red['A'],red['B'])) }
print(distanciaA_B)
        
matrizCostos = calcularMatrizCostos(redDiccionarioAnidado)
[print(llave,' ',valor) for llave,valor in matrizCostos.items()]

print(matrizCostos)




