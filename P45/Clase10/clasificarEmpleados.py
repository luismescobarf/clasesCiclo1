#Requerimiento: Se requiere una función que recoja la información
#de una cantidad determinada de empleados (nombre y salario). 
#Se espera recibir el nombre del empleado y el salario del empleado (dólares). 
# Retornar cuáles empleados deben pagar impuestos
#(salario superior a 10.000) en una lista. Retornar otra lista que contiene
#toda la nómina ingresada y mostrar en pantalla el salario promedio de los empleados
#registrados. Agregar en el listado de los empleados que pagan impuestos, el valor
#correspondiente (5%)

#Algoritmo:
# 1) Mientras el usuario esté ingresando nómina (quiera continuar):
# 2)      Coleccionar el empleado ingresado
# 3)      Si el empleado tiene un salario superior a 10.0000
#             Agregarlo en el listado de los que pagan impuestos
# 4) Calcular el salario promedio
# 5) Mostrarlo en pantalla
# 6) Retornar las listas correspondientes

#Traducción -> Python
def impuestosEmpleados():


    
    #El usuario está especificando la nómina
    continuar = True
    while continuar:
        infoEmpleado = input('Ingrese el nombre y salario (nom salario):').split(' ')

          


