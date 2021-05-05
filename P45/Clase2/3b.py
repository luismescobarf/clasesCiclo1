"""3b) Escribir un algoritmo que reciba cuatro números
y reporte la diferencia de los dos primeros,
reporte el producto del tercero y el cuarto,
reporte el promedio descartando el menor de los números."""

#Objetivo general -> Reportar cómputos numéricos del enunciado

#Algoritmo:
#1) Almacenar los cuatro números en variables para procesar.
#2) Calcular la diferencia de los dos primeros números y almacenarla.
#3) Calcular el producto del tercer y cuarto número y almacenarlo.
#4) Obtener el menor de los números ingresados y almacenarlo.
#5) Calcular el promedio de los cuatro números, descartando el menor
#  y almacenarlo.
#6) Reportar diferencia
#7) Reportar producto
#8) Reportar promedio

#Traducción
n1 = 15
n2 = 25
n3 = 40
n4 = -20
variable_1 = n1 - n2
variable_2 = n3 * n4
menorNumero = min( (n1,n2,n3,n4) )
variable_3 = ( sum( (n1,n2,n3,n4) ) - menorNumero ) / (len( (n1,n2,n3,n4) ) - 1)
variable_3 = round(variable_3,2)
print("la diferencia entre el primero y el segundo es" , variable_1)
print("el producto entre el tercero y el cuarto es" , variable_2)
print("el promedio es" , variable_3)