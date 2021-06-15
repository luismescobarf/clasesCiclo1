#Librería para arreglos o matrices
import numpy as np
import random

#Crear colecciones tipo numpy -> arreglos
arreglo1 = np.array([ [1,2], [3,4] ])
print(arreglo1)
print('Tipo->',type(arreglo1))

arreglo2 = np.array([ [1,2], [3,4,5,6] ])
print(arreglo2)
print('Tipo->',type(arreglo2))

lista = [[1,2,3],[4,5,6]]
print(type(lista))
arreglo3 = np.array(lista)
print(arreglo3)
print('Tipo->',type(arreglo3))

arregloGenerado = np.zeros( 5 )
print(arregloGenerado)

matrizGenerada = np.zeros( (3,4) )
print(matrizGenerada)

matrizGenerada = np.ones( (5,5) )
print(matrizGenerada)

arregloRango = np.arange(1,6,2)
print(arregloRango)

arregloAleatorio = np.random.randint(-5, 5, size=7 )
print(arregloAleatorio)

departamentos = ['Valle','Tolima','Cesar','Atlántico']
arregloDepartamentos = np.random.choice( departamentos, 3, p=[0.1,0.1,0.6,0.2] )
print(arregloDepartamentos)

matrizDepartamentos = np.random.choice( departamentos, (3,4), p=[0.1,0.1,0.6,0.2] )
print(matrizDepartamentos)

requerimientoJahleel = np.array(departamentos)
np.random.shuffle(requerimientoJahleel)
print('Sin repeticiones y orden aleatorio')
print(requerimientoJahleel)

#Consultas (recorrer extraer partes del contenedor)
matrizAletoria = np.random.randint(-5, 5, size=(6,6) )
print(matrizAletoria)

#Consultar tamaño
# print('Número de filas->',len(matrizAletoria))
# print('Número de columnas->',len(matrizAletoria[0]))
# print('Forma de la matriz ->',np.shape(matrizAletoria))
# print('Tipo de la forma ->',type(np.shape(matrizAletoria)))

# #Acceder a valores o a posiciones
# print('Valor de la esquina superior izquierda-> ', matrizAletoria[0,0] )
# print('Valor de la diagonal-> ', matrizAletoria[2,2] )

submatriz = matrizAletoria[1:4,1:]
print(submatriz)

#Recorridos for -> con variables auxiliares o temporales, con subíndices
print('Recorrido 1 matrizAleatoria')
for fila in matrizAletoria:
    for columna in fila:
        print(columna,end=' ')
    print()

print('Recorrido 2 matrizAleatoria')
for i in range(len(matrizAletoria)):
    for j in range(len(matrizAletoria[i])):
        print(matrizAletoria[i,j],end=' ')
    print()

matrizAletoria = np.random.randint(3, size=(3,3) )
print(matrizAletoria)

#Operaciones
# sumatoriaColumnas = np.sum(matrizAletoria,axis=0)
# print(sumatoriaColumnas)

# sumatoriaFilas = np.sum(matrizAletoria,axis=1)
# print(sumatoriaFilas)

# print("Sumatoria de toda la matriz->",np.sum(matrizAletoria))

print("Diagonal de la matriz:")
print(matrizAletoria.diagonal())

print("Transpuesta (Visualizaciones)")
print(matrizAletoria.transpose())

print("Espejo de las columnas")
print( np.fliplr(matrizAletoria) )

print("Diagonal contraria")
print(np.fliplr(matrizAletoria).diagonal())

print("Efecto sobre la matriz original")
print(matrizAletoria)

print('Ubicación de los valores iguales a 2')
print( np.where(matrizAletoria==2)  )



















