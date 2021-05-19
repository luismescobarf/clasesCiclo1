#Objetivo: mostrar en pantalla los 20 primeros números enteros

# #Algoritmo:
# 1) Mostrar el número 1
# 2) Mostrar el número 2
# .
# .
# .
# 3) Finalizar cuando todos los 20 números han sido mostrados

# #Traducción
# print(1)
# print(2)
# .
# .
# .
# print(20)

#Requerimiento en versión while (mientras)
# x = 1
# while x <= 20:
#     print(x)
#     x = x + 1

#Requerimiento en versión for (para)

#Tener en cuenta las variantes (siempre es estrictamente menor que limSuperior)
# Primera variante: range(limSuperior) -> LímInf: 0, Avance: 1
# Segunda variante: range(limInferior,limSuperior) -> Avance: 1
# Tercera variante: range(limInferior,limSuperior,Avance) 

# #Primera variante
# for x in range(20):
#     print(x+1,end='-')

# #Segunda variante
# for x in range(1,21):
#     print(x,end="-")

# #Tercera variante
# for x in range(1,21,1):
#     print(x,end="-")




