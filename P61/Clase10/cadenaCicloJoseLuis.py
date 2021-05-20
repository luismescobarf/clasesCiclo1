#Requerimiento: Se necesita una función que reciba una cadena y
#genere un mensaje en pantalla con los caracteres
#que la constituyen, separados por coma (horizontal)

#Variante Requerimiento Fredy Ignacio:
#Que además de la separación por comas, la cadena esté invertida

#Objetivo -> Mostrar entrada en pantalla separada por comas

#Algoritmo
#1) Capturar cadena
#2) Extraer cada una de los caracteres y por cada uno, 
#mostrarlo en pantalla acompañado de una coma

#Traducción -> Python

#Versión 1
# cadena = input("Ingrese una cadena: ")
# nuevaCadena = str()
# for i in range( len(cadena) ):
#     nuevaCadena = nuevaCadena + cadena[i] + ','
# print(nuevaCadena)

#Versión 2 Jorge Alexander
# cadena = input("Ingrese una cadena: ")
# for i in range( len(cadena) ):
#     print(cadena[i],end=",")

#Algoritmo Variante del requerimiento
#-> Antes del cómputo invertir la cadena
#-> Recorrer la cadena al revés durante el for

#Traducción de esta versión
#-> Antes del cómputo invertir la cadena
# cadena = input("Ingrese una cadena: ")
# cadena = cadena[::-1]
# for i in range( len(cadena) ):
#     print(cadena[i],end=",")

#Traducción de esta versión
#-> Recorrer la cadena al revés durante el for
# cadena = input("Ingrese una cadena: ")
# for i in range(-1,(len(cadena)+1)*-1,-1):
#     print(cadena[i],end=",")

#Traducción de esta versión
#-> Antes del cómputo invertir la cadena
#-> Variación en el rango del for
cadena = input("Ingrese una cadena: ")
for caracter in cadena[::-1]:
    print(caracter,end=",")
    



