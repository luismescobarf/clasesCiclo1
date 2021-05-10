#Objetivo: detectar mayores de edad
#para realizar el informe correspondiente
#al requerimiento.

#Algoritmo pseudocódigo general
# 1) Recoger 4 edades y almacenarlas.
# 2) Recoger la edad vigente como mayoría
# de edad.
# 3) Verificar quiénes son mayores de edad 
# y contarlos (acumulador).
# 4) Si hay por lo menos dos mayores de edad,
# calcular el promedio de edad de estos.
# 5) Dependiendo del número de mayores de edad
# realizar reporte acumulado de mayores y promedio.

# edad1 = int(input('Ingrese la edad del primer participante: '))
# edad2 = int(input('Ingrese la edad del segundo participante: '))
# edad3 = int(input('Ingrese la edad del tercer participante: '))
# edad4 = int(input('Ingrese la edad del cuarto participante: '))
# Mayoria_edad = int(input('Ingrese la mayoría de edad vigente: '))

def requerimiento(edad1,edad2,edad3,edad4,Mayoria_edad):
    numMayoresEdad = 0
    edadAcumuladaME = 0
    #Revisar el primer integrante
    if edad1>=Mayoria_edad:
        numMayoresEdad += 1
        #numMayoresEdad = numMayoresEdad +1
        edadAcumuladaME += edad1
        #edadAcumuladaME = edadAcumuladaME + edad1
    #Revisar el segundo integrante
    if edad2>=Mayoria_edad:
        numMayoresEdad += 1
        #numMayoresEdad = numMayoresEdad +1
        edadAcumuladaME += edad2
        #edadAcumuladaME = edadAcumuladaME + edad1
    #Revisar el tercer integrante
    if edad3>=Mayoria_edad:
        numMayoresEdad += 1
        #numMayoresEdad = numMayoresEdad +1
        edadAcumuladaME += edad3
        #edadAcumuladaME = edadAcumuladaME + edad1
    #Revisar el tercer integrante
    if edad4>=Mayoria_edad:
        numMayoresEdad += 1    
        #numMayoresEdad = numMayoresEdad +1
        edadAcumuladaME += edad4
        #edadAcumuladaME = edadAcumuladaME + edad1
    #Revisar para realizar el reporte
    if numMayoresEdad >= 2:
        promedioMayoresEdad = edadAcumuladaME / numMayoresEdad
        return f"Participación Aprobada! Número de Acudientes: {numMayoresEdad} Promedio Edad Acudientes: {promedioMayoresEdad}"        
    else:
        return f"Participación Rechazada"

print(requerimiento(7,8,9,10,18))
print(requerimiento(18,18,9,10,18))

