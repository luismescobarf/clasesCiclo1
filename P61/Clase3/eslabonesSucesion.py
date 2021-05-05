"""Objetivo:    Obtener la distancia promedio de la sucesión de 4 puntos,
                la longitud de la menor conexión y la longitud de la mayor conexión"""

#Algoritmo (pseudocódigo)
# 1) Cargar los cuatro puntos.
# 2) Calcular la distancia entre el punto 1 y el punto 2 y almancerla.
# 3) Calcular la distancia entre el punto 2 y el punto 3 y almancerla.
# 4) Calcular la distancia entre el punto 3 y el punto 4 y almancerla.
# 6) Obtener la distancia promedio de la secuencia y almacenarla.
# 7) Obtener la menor longitud de conexión y almacenarla.
# 8) Obtener la mayor longitud de conexión y almacenarla.
# 9) Reportar la distancia promedio, menor y mayor conexiones

#Traducción Lenguaje -> Python
from geometricasMatematicas import distEUC as euc2D
from geometricasMatematicas import promedio3Conexiones as p3c
x1 =  4
y1 =  5
#----------------------------
x2 =  6
y2 =  6
#----------------------------
x3 =  7
y3 =  5
#----------------------------
x4 =  8
y4 =  5.5
#----------------------------
d_1_2 = euc2D(x1,x2,y1,y2)
d_2_3 = euc2D(x2,x3,y2,y3)
d_3_4 = euc2D(x3,x4,y3,y4)
longitudPromedio = p3c(d_1_2,d_2_3,d_3_4)
longitudMinima = min( (d_1_2,d_2_3,d_3_4) )
longitudMaxima = max( (d_1_2,d_2_3,d_3_4) )
print("La distancia promedio = ",longitudPromedio)
print("La menor distancia = ",longitudMinima)
print("La mayor distancia = ",longitudMaxima)

# #Salidas de diagnóstico
# print("----------------------")
# print("d_1_2 =",d_1_2)
# print("d_2_3 =",d_2_3)
# print("d_3_4 =",d_3_4)





