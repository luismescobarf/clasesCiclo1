#Algoritmo
#Entradas: radio
#Proceso: cálculo pi*r*r
#Reportar la salida

# def areaCirculo(radio):
#     pi = 3.1416
#     radioCuadrado  = radio**2
#     area = pi * radioCuadrado
#     return area

#print("Mostrando el valor de pi:", pi)

from libreriaGeometricas import areaCirculo

#& hallar el area de un circulo
radio = 34
#pi = 3.1416
#radioCuadrado  = radio**2
#area = pi * radioCuadrado
#area = areaCirculo(radio)
print('el area del circulo es:', areaCirculo(radio))