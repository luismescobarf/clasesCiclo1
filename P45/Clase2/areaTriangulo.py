#Objetivo: calcular el área de un triángulo

#Algoritmo (pseudocódigo)
#1. Obtener la altura del triángulo y almacenarla en una variable
#2. Obtener la base del triángulo y almacenarla en una variable
#3. Realizar el cálculo (base*altura)/2 y guardarlo
#4. Reportar el resultado almacenado

# def areaTriangulo(base,altura):
#     resultado = (base*altura)/2
#     return resultado

import libreriaGeometricas

#Transcripción a Python
altura = 12
base = 20
#areaTriangulo = (base*altura)/2
areaResultante = libreriaGeometricas.areaTriangulo(base,altura)
print("El área del triángulo es ", areaResultante)



