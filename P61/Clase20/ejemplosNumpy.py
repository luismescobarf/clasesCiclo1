#Numpy
#Instalando el Anaconda -> Entorno del sistema
#Gestor de paquetes de Python (cmd, powershell)
#Disponible lo importamos en nuestras soluciones
import numpy as np

#Generar nuestras primeras colecciones tipo numpy (arreglo)
arreglo1 = np.array([[1,2],[3,4]])
print('Tipo',type(arreglo1))
print('Contenido')
print(arreglo1)
print("Dimensiones",np.shape(arreglo1))

#Diferencia acceso -> tuplas
print('Contenido esquina inferior derecha:',arreglo1[1,1])

#Convirtiendo tipos
lista = [[2,3,4,56],[2,3,4,56],[1,2],[1]]
arreglo2 = np.array(lista)
print(arreglo2)

#Generaciones automáticas numpy
arregloCeros = np.zeros((5,3))
print(arregloCeros)

arregloUnos = np.ones((5,3))
print(arregloUnos)

arregloRango = np.arange(1,10,2)
print(arregloRango)

#Incorporar el arreglo
lista.append(arregloCeros)
print("Nuevo valor de la lista:",lista)
print("Tipo del último elemento:",type(lista[-1]))
print("Tipo del primer elemento:",type(lista[0]))

#Arreglo con valores aleatorios -> límite superior de los valores
arregloAleatorio = np.random.randint(5,size=10)
print('Arreglo aleatorio')
print(arregloAleatorio)

matrizAleatoria = np.random.randint(-5,10,size=(6,6))
print('Matriz aleatoria')
print(matrizAleatoria)

#Recorrer la matriz generada para mirar el acceso
print('Recorriendo con variables auxiliares')
for fila in matrizAleatoria:
    for columna in fila:
        print(columna,end=',')
    print()

#Recorrer la matriz generada para mirar el acceso con subíndices (tuplas)
print('Recorriendo con subíndices')
for i in range(len(matrizAleatoria)):
    for j in range(len(matrizAleatoria[i])):
        print(matrizAleatoria[i,j],end=' ')
    print()

#Generar una matriz de forma aleatoria seleccionando elementos d eun contenedor
frutas = ['manzana','naranja','piña','mora','feijoa','limon']
arrSelAleatoria = np.random.choice(frutas, 5)
print('Arreglo:')
print(arrSelAleatoria)

matSelAleatoria = np.random.choice(frutas, (3,3), p=[0.1,0.1,0.1,0.1,0.1,0.5])
#matSelAleatoria = np.random.choice(frutas, (3,3))
print('Matriz:')
print(matSelAleatoria)

#Operaciones numpy
matOperaciones = np.random.randint(0,3,size=(3,3))
print('Matriz generada para operaciones')
print(matOperaciones)

#Suma de todas las columnas
print('Suma de cada columna')
print(np.sum(matOperaciones,axis=0))

#Suma de todas las filas
print('Suma de cada filas')
print(np.sum(matOperaciones,axis=1))

#Rangos de la matriz (submatrices)
print('Suma de la columna con índice 2')
print(np.sum(matOperaciones[:,2]))

#Extraer el rango
submat = matOperaciones[0:2,0:2]
print(submat)
print('Sumatoria de filas de la submatriz')
print(np.sum(submat,axis=1))
print('Sumatoria de columnas de la submatriz')
print(np.sum(submat,axis=0))

#Mostrar diagonal y calcular su sumatoria
diagonal = matOperaciones.diagonal()
print('Diagonal obtenida ->',diagonal)
print('Sumatoria de la diagonal->',np.sum(diagonal))

# #Mostrar sumatoria diagonal matriz irregular
# matIrregular = np.random.randint(0,3,size=(4,3))
# print('Matriz irregular')
# print(matIrregular)
# print('Diagonal irregular: ',matIrregular.diagonal())
# print('Sumatoria diagonal matriz irregular-> ',np.sum( matIrregular.diagonal() ))

#Espejo
print('Matriz antes de espejo')
print(matOperaciones)
print('Espejo columnas')
espejo = np.fliplr(matOperaciones)
print(espejo)

#Diagonal contraria
print('Diagonal contraria')
print(  espejo.diagonal()  )

#Transpuesta
transpuesta = np.transpose(matOperaciones)
print("Transpuesta")
print(transpuesta)





