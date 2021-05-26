#Nómina -> Lista grande (primel nivel)
#Empleado -> Lista con 2 o 3 valores: Nombre(s), Impustos (en tal caso), Salario
import pprint as pp #pretty print

nomina = [
    ['Ana',14000],
    ['María Fernanda',3000000],
    ['María Camila',3000000],
    ['Luis',700]
]

nominaLD = [
    { 'nombre':'Ana' , 'salario': 14000},
    { 'nombre':'María Fernanda' , 'salario': 3000000},
    { 'nombre':'María Camila' , 'salario': 3000000},
    { 'nombre':'Luis' , 'salario': 700}
]

pp.pprint(nominaLD)
#print(nominaLD)

#Consultas a la nómina
print('Primer empleado registrado: ',nominaLD[0])
print('Salario del Primer empleado registrado: ',nominaLD[0]['salario'])
print('Último empleado registrado: ',nominaLD[-1])
print('Segundo empleado registrado: ',nominaLD[1])
print('Salario del Segundo empleado registrado: ',nominaLD[1]['salario'])

#Recorrer nuestra lista de diccionarios (subíndices)
for i in range(len(nominaLD)):
    print(f"Subíndice: {i}")
    print(f"Nombre Empleado: { nominaLD[i]['nombre'] }")
    print(f"Salario : ${ nominaLD[i]['salario'] }")
    print( "----------" )

#Ordenamientos
salarios = [1000,230,180,8000]
print("Primera versión de salarios: ",salarios)
print("Mayor salario ",max( salarios ))
salarios = sorted(salarios,reverse=True)
print("Versión ordenada de salarios: ",salarios)

#Función que retorna un atributo del elemento de la colección (compuesta)
def retornarSalarioEmpleado(id,nominaLD):
    return nominaLD[id]['salario']

#lambda parametros de entrada : parametros de salida
retornoSalario = lambda id, nominaLD : nominaLD[id]['salario']

print('Salario consultado: ',retornarSalarioEmpleado(0,nominaLD) )
print('Salario consultado: ',retornarSalarioEmpleado(-1,nominaLD) )
print('Salario consultado: ',retornarSalarioEmpleado(1,nominaLD) )
print("--------------")
print('Salario consultado: ',retornoSalario(0,nominaLD) )
print('Salario consultado: ',retornoSalario(-1,nominaLD) )
print('Salario consultado: ',retornoSalario(1,nominaLD) )

print('Base de Datos de Nómina sin ordenar:')
pp.pprint(nominaLD)
nominaLD = sorted(nominaLD, key = lambda empleado : empleado['salario'], reverse=True )
print('Base de Datos de Nómina ordenada salario desc:')
pp.pprint(nominaLD)
nominaLD = sorted(nominaLD, key = lambda empleado : empleado['nombre'] )
print('Base de Datos de Nómina ordenada nombre desc:')
#pp.pprint(nominaLD)
[print(empleado) for empleado in nominaLD]

#Ordenamientos -> bubble sort, quick sort, slection, radix sort, merge sort.

#Recorrer un diccionario
diccionarioAna = nominaLD[0]
for llave,valor in diccionarioAna.items():
    print("Llave ->",llave,"Valor ->",valor)
print('---------')
for i,llave in enumerate(diccionarioAna.keys()):
    print(f"Llave {i}) {llave} ")
print('---------')
for i,valor in enumerate(diccionarioAna.values()):
    print(f"Valor {i}) {valor} ")
print('---------')



"""
#Codificación por lista anidada
print("Nomina Completa")
print(nomina)

print("Información de Ana")
print(nomina[0])
print("Salario de Ana")
print(nomina[0][1])
"""