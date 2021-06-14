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

matrizAleatoria = np.random.randint(3,5,size=(6,6))
print('Matriz aleatoria')
print(matrizAleatoria)

#Recorrer la matriz generada para mirar el acceso


