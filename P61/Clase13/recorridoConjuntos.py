#Alternativas de construcción del conjunto

#Mutando la cantidad de elementos
#Utilizar como departamentos sucritos
from typing import no_type_check, no_type_check_decorator


conjunto = set()
conjunto.add('Cundinamarca')
conjunto.add('Quindío')
conjunto.add('Tolima')
conjunto.add('Santander')
conjunto.add('Cesar')
conjunto.add('Valle')
conjunto.add('Huila')
conjunto.add('Meta')
conjunto.add('Boyacá')
conjunto.add('Antioquia')
print(conjunto)

# #Definición literal del conjunto
# conjunto = {'Valle','Meta','Cundinamarca','Antioquia'}
# print(conjunto)

#Requerimiento: Revisar de una base de datos de transacciones,
#los departamentos han hecho aportes y los que faltan por hacerlo. 
#Retornar un listado de cada grupo de departamentos.

#Requerimientos adicionales (propuestos -> Foro, Siguiente clase): 
# Cuál es el departamento que más ha aportado?
# Cuál es el promedio de aportes general?
# Si es un departamento que ha aportado varias veces, cuál es su promedio de aporte?

bdTransacciones = (
    { 'id':'A3456', 'depto':'Cundinamarca', 'concepto':'Puentes', 'valor':750 },
    { 'id':'B56G', 'depto':'Valle', 'concepto':'Parques', 'valor':100 },
    { 'id':'F78KL', 'depto':'Antioquia', 'concepto':'Vías', 'valor':540 },
    { 'id':'TG57', 'depto':'Tolima', 'concepto':'Reforestación', 'valor':200 },
    { 'id':'GBE32', 'depto':'Quindío', 'concepto':'Ciclorutas', 'valor':50 },
    { 'id':'67FJ', 'depto':'Tolima', 'concepto':'Mejoras y ornato', 'valor':300 },
    { 'id':'HHF56', 'depto':'Valle', 'concepto':'Hospitales', 'valor':1000 }
)

#Algoritmo:
# 1) Para cada transacción de la base de datos de transacciones:
# 2)      Revisar el departamento de la transacción
# 3)      Agregar el departamento al conjunto de departamentos aportantes
# 4) Obtener los depeartamentos que no han realizado aportes
# 5) Retornar los listados de departamentos solicitados

#Traducción a Python
def listadosDepartamentosAportes(bdTransacciones):
    #deptosPendientes = list()
    #deptosAportantes = list()
    deptosPendientes = set()
    deptosAportantes = set()
    # for transaccion in bdTransacciones:
    #     deptosAportantes.add(transaccion['depto'])
    for i in range(len(bdTransacciones)):
        deptosAportantes.add(bdTransacciones[i]['depto'])
    deptosPendientes = conjunto.difference(deptosAportantes)
    # deptosPendientes = list(deptosPendientes)
    # deptosAportantes = list(deptosAportantes)
    return list(deptosAportantes), list(deptosPendientes)

#Sección principal
listaDeptosAportantes, listaDeptosPendientes = listadosDepartamentosAportes(bdTransacciones)
print("---Aportantes---")
[print(x) for x in listaDeptosAportantes]
print("---Pendientes---")
[print(x) for x in listaDeptosPendientes]


            



    
