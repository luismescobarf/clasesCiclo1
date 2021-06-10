#Requerimiento: se le solicita al usuario n coordenadas
#por teclado. Debe ingresarlas colocando primero el nombre del 
#punto que representa la coordenada, y a continuación los valores
#en x y y que componen la coordenada (seperadas por espacios). 
# Coleccionarlas y al final y aplicar un corrimiento dado a todas las coordenadas.

#Ejemplo:
# 'Bogotá' 12.5 4.8
# 'A' 7 10

# Corrimiento en X -> 1
# Corrimiento en Y -> 2

# 'Bogotá'    13.5    6.8
# 'A'         8       12

#Algoritmo
# 1) El usuario ingresa la cantidad de puntos solicitados.
# 2) Los puntos deben ser coleccionados en el formato string float float
# 3) Aplicar el corrimiento a cada una de las componentes

#Totalmente Procedural estructurado
n = 3
corrimientoX = 4
corrimientoY = 1
coleccionPuntos = []
for _ in range(n):
    coordenada = input('Ingrese coordenadas: ')
    coordenada = coordenada.split(' ')
    coordenada[1] = float(coordenada[1])
    coordenada[2] = float(coordenada[2])
    coleccionPuntos.append(coordenada)
print('Colección de puntos')
print(coleccionPuntos)

for i in range(len(coleccionPuntos)):
    coleccionPuntos[i][1] = coleccionPuntos[i][1] + corrimientoX
print('Colección con corrimiento en x aplicado:')
print(coleccionPuntos)

for i in range(len(coleccionPuntos)):
    coleccionPuntos[i][2] = coleccionPuntos[i][2] + corrimientoY
print('Colección con corrimiento en y aplicado:')
print(coleccionPuntos)







#Funciones de primera clase y de orden superior

#Aprovechando map y reduce

