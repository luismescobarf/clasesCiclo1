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
#             Agregarlo en el listado de los que pagan impuestos (con los impuestos)
# 4) Calcular el salario promedio
# 5) Mostrarlo en pantalla
# 6) Retornar las listas correspondientes (empleados y empleadosImp)

#Traducción -> Python
def impuestosEmpleados():

    #Colecciones
    bdEmpleados = list()
    #bdEmpleados = []
    empleadosImpuestos = list()
    #empleadosImpuestos = []
    
    #El usuario está especificando la nómina
    continuar = True
    while continuar:
        # informacionSinFormato = input('Ingrese el nombre y salario (nom salario):')
        # infoEmpleado = informacionSinFormato.split(' ')
        infoEmpleado = input('Ingrese el nombre y salario (nom salario):').split(' ')
        infoEmpleado[-1] = int(infoEmpleado[-1])#Formato numérico al salario

        #Coleccionar el empleado
        bdEmpleados.append(infoEmpleado)

        #Revisar si debe pagar impuestos
        #if infoEmpleado[-1] > 10000:
        if bdEmpleados[-1][-1] > 10000:
            #Colección (lista) empleados que pagan impuestos            
            #Por referencia
            #empleadosImpuestos.append(bdEmpleados[-1])
            #Por parámetro
            empleadosImpuestos.append(bdEmpleados[-1].copy())
            #empleadosImpuestos.append(list(bdEmpleados[-1]))
            #Agregar los impuestos en la penúltima posición            
            empleadosImpuestos[-1].insert( -1, empleadosImpuestos[-1][-1] * 0.05 )

        #Criterio de finalización del while indeterminado o loop
        if input("Ha terminado el registro? (s)").lower() == 's':
            continuar = False
    
    #Calcular el salario promedio general
    salarioPromedio = 0
    for empleado in bdEmpleados:
        salarioPromedio += empleado[-1]
    salarioPromedio = salarioPromedio / len(bdEmpleados)
    print(f"El slario promedio de la nómina ingresada es {salarioPromedio}")

    #Retornar los listados solicitados
    return bdEmpleados, empleadosImpuestos

#Sección principal
nomina, detalleEmpleadosPagandoImpuesto = impuestosEmpleados()
print('---Nómina completa---')
for i,empleado in enumerate(nomina):
    print(f"{i+1}) {empleado}")

print('---Empleados que pagan impuestos---')
for i,empleado in enumerate(detalleEmpleadosPagandoImpuesto):
    print(f"{i+1}) {empleado}")



    


          


