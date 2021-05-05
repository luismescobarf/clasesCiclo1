"""3) Escribir un algoritmo que reciba cuatro números
y reporte la diferencia de los dos primeros,
reporte el producto del tercero y el cuarto,
reporte el promedio de los cuatro números."""

#Objetivo general -> Reportar cómputos numéricos del enunciado

#Algoritmo:
#1) Almacenar los cuatro números en variables para procesar.
#2) Calcular la diferencia de los dos primeros números y almacenarla.
#3) Calcular el producto del tercer y cuarto número y almacenarlo.
#4) Calcular el promedio de los cuatro números y almacenarlo.
#5) Reportar diferencia
#6) Reportar producto
#7) Reportar promedio

#Traducción
n1 = 15
n2 = 25
n3 = 40
n4 = -20
variable_1 = n1 - n2
variable_2 = n3 * n4
#variable_3 = (n1 + n2 + n3 + n4) / 4
#Funciones nativas (subsistemas o algoritmos modularizados específicos)
"""sum()
max()
min()
len()
range()"""
variable_3 = sum( (n1,n2,n3,n4) ) / len( (n1,n2,n3,n4) )
print("la diferencia entre el primero y el segundo es" , variable_1)
print("el producto entre el tercero y el cuarto es" , variable_2)
print("el promedio es" , variable_3)