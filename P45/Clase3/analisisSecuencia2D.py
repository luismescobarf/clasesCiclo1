'''Se requiere una función que calcule la distancia promedio
que existe en una sucesión (secuencia) de 4 puntos.'''

#1) Asignar valores en X y Y para puntos uno y dos
#2) Aplicar distancia euclidiana y almacenar
#3) Asignar valores en X y Y para puntos dos y tres
#4) Aplicar distancia euclidiana y almacenar
#5) Asignar valores en X y Y para puntos tres y cuatro
#6) Aplicar distancia euclidiana y almacenar
#7) Sumar las tres distancias almacenadas
#8) Dividir en el numero de distancias
#9) Obtener la menor distancia de la secuencia
#10) Obtener la mayor distancia de la secuencia
#11) Reportar los análisis hechos en la secuencia

x1 = 3
y1 = 10
x2 = 1
y2 = 1
x3 = 2
y3 = 2
x4 = 4
y4 = 4

from libreriaGeomArit import distanciaEuclidiana
dist1 = distanciaEuclidiana(x1,y1,x2,y2)
dist2 = distanciaEuclidiana(x2,y2,x3,y3)
dist3 = distanciaEuclidiana(x3,y3,x4,y4)

disTotal = sum((dist1,dist2,dist3))
print('Distancia total: ', disTotal)

disProm = disTotal / len((dist1,dist2,dist3))
print('Distancia promedio: ', disProm)

distMenor = min( (dist1,dist2,dist3) )
print('Distancia menor: ', distMenor)

distMayor = max( (dist1,dist2,dist3) )
print('Distancia mayor: ', distMayor)

# #Salida de diagnóstico
# print("-------------------")
# print("dist1:",dist1)
# print("dist2:",dist2)
# print("dist3:",dist3)