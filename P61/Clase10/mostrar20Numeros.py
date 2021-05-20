#Requerimiento: mostrar en pantalla los números
#del 1 al 20.

#Objetivo: El mismo requerimiento

# #Traducción Python:
# print(1)
# print(2)
# print(3)
# .
# .
# .

#Aprovechamos la flexibilidad del while
# x = 1
# while(x<=20):
#     print(x,end=" ")
#     x += 1

#Acercar la notación del while al for
# x = 0
# while(x<20):    
#     x += 1
#     print(x,end = " ")

# #Versión tipo for -> Python (4 versiones)
#Nota! -> Siempre es estrictamente menor al limSup
# 1) Especificamos limSup (Defecto: limInf:0,avance:1)
# 2) Especificamos limInf, limSup (Defecto: avance:1)
# *3) Especificamos limInf, limSup, avance (for en lenguajes con tipado rígido)
# 4) Especificamos solamente cuántas veces sucede algo sin llevar variables de control

#Versión 1 for para el requerimiento
# for x in range(20):
#     print(x+1,end=' ')

#Versión 2 for para el requerimiento
# for x in range(1,21):
#     print(x,end=' ')

#Versión 3 para el requerimiento
# for x in range(1,21,1):
#     print(x,end=' ')

#Variación del requerimiento (mostrar sólo impares)
# for x in range(1,21,2):
#     print(x,end=' ')

#Versión 4 para el requerimiento
x = 1
for _ in range(20):
    print(x,end=" ")
    x += 1






