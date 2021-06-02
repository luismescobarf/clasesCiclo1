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

# #Algoritmo o el pseudocódigo del Vecino Más Cercano MTSP (Jornadas del Agente)
# 1) Establecer nodo o ciudad de partida (radicado el Agente)
# 2) Preparar contenedor de jornadas
# 3) Iniciar el itinerario (tour) en la ciudad de partida establecida
# 4) Mientras tengamos ciudades sin cubrir o incluir en los itinerarios
# 5)      Desde la última ciudad del itinerario actual generamos las salidas a las demás ciudades (no cubiertas)
# 6)      Seleccionar la mejor de las salidas
# 7)      Si agregar la ciudad no supera el tiempo máximo de jornada:
# 8)            Agregar la ciudad (mejor de las salidas) al itinerario actual (crecimiento)
# 9)      De lo contrario:
# 10)            Cerrar itinerario con el retorno y agregarlo a las jornadas (días)
# 11)            Abrir el itinerario con la mejor ciudad que no fue acomodada en el itinerario anterior
# 12)     Actualizar las ciudades sin cubrir
# 13) Si el itinerario que estaba en construcción no fue agregado a las jornadas:
# 14)    Agregarlo
# 15) Mostrar las jornadas
# 16) Generar indicadores de las jorandas

#Traducción a Python
print('-----Algoritmo Heurístico del Vecino Más Cercano MTSP-----')
#Inicialización del tour y el conjunto de control de ciudades cubiertas
ciudadInicial = 'Manizales'
itinerario = list()
itinerario.append(ciudadInicial)
ciudadesSinCubrir = set(red.keys())
ciudadesSinCubrir.remove(ciudadInicial)
jornadasTSP = list()#Separar en jornadas para regreso del agente viajero
duracionMaxJornada = 9
#Sección principal del algoritmo (cubrir todas las ciudades como ciclo hamiltoniano)
while len(ciudadesSinCubrir) > 0:
    #Construir el listado con las posibles salidas desde la última ciudad ingresada en el itinerario
    listadoSalidas = list()
    for ciudadSalida in ciudadesSinCubrir:
        listadoSalidas.append(  (ciudadSalida, matrizCostos[ itinerario[-1]+'-'+ciudadSalida  ]) )
    listadoSalidas = tuple(listadoSalidas)
    #Seleccionar la mejor salida
    mejorSalida = listadoSalidas[0]
    for salida in listadoSalidas[1:]:
        if mejorSalida[1] > salida[1]:
            mejorSalida = salida

    #Antes de actualizar itinerario, revisar si es una jornada viable
    duracion = 0
    for i in range(len(itinerario)-1):
        duracion += matrizCostos[itinerario[i]+'-'+itinerario[i+1]]
    duracion += matrizCostos[itinerario[-1]+'-'+mejorSalida[0]]
    duracion += matrizCostos[mejorSalida[0]+'-'+ciudadInicial]
    if duracion <= duracionMaxJornada:
        #Actualizar el itinerario
        itinerario.append(mejorSalida[0])        
    else:
        #Cerrar el itinerario actual
        itinerario.append(ciudadInicial)
        #Agregarlo al listado de las jornadas
        jornadasTSP.append(list(itinerario))
        #Abrir itinerario nuevo
        itinerario.clear()
        itinerario = [ciudadInicial,mejorSalida[0]]
    
    #Actualizar el conjunto (entrando en el itinerario la ciudad ahora está cubierta)
    ciudadesSinCubrir.remove(mejorSalida[0])    

#Ingresar el último itinerario si hace falta
itinerario.append(ciudadInicial)
if jornadasTSP[-1] != itinerario:
    jornadasTSP.append(list(itinerario))

#Visualizar los itinerarios generados
print(':::::Itinerarios::::::')
[print(jornada) for jornada in jornadasTSP]

#Función para calcular duración de los itinerarios
def calcularDuracion(itinerario,matrizCostos):
    duracion = 0
    for i in range(len(itinerario)-1):
        duracion += matrizCostos[itinerario[i]+'-'+itinerario[i+1]]    
    return duracion

#Generar contenedor ampliado de los itinerarios
print('Diccionario Detalle Jornadas')
jornadasDetalle = dict()
for i,jornada in enumerate(jornadasTSP):
    jornadasDetalle[f"Jornada{i+1}"] = { 'itinerario':jornada, 'duracion':calcularDuracion(jornada,matrizCostos)}

#Mostrar en pantalla
[print(llave,valor) for llave,valor in jornadasDetalle.items()]

#Ejercicio propuesto: Obtener la duración promedio del diccionario generado

# #Cuantificar la calidad de la solución
# fo = 0
# for i in range(len(itinerario)-1):
#     fo += matrizCostos[itinerario[i]+'-'+itinerario[i+1]]
# print("Función Objetivo (calidad) solución = ",fo)
    

    
    
    












