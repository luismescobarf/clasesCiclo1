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

matrizAletoria = np.random.randint(-5, 5, size=(7,7) )
print(matrizAletoria)

#Consultas (recorrer extraer partes del contenedor)











