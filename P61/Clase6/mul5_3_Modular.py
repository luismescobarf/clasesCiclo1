#Objetivo -> Contar los múltiplos de 3 y múltiplos de 5
#en la entrada

#Algoritmo -> Diagrama de Flujo

#Traducción -> Python
from logicaMul3_5 import *
from interfazMul3_5 import *

#Interacción
a,b,c = recoleccionEntradas()

#Lógica
contadorMul3, contadorMul5 = clasificarEntradas(a, b, c)

#Interacción
reporteMultiplos(contadorMul3,contadorMul5)
