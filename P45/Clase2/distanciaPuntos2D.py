#Programa que calcula la distancia de dos coordenadas en el plano cartesiano

#Objetivo => Usar la formula euclidiana para hallar la distancia entre dos coordenadas en el plano cartesiano

""" Pasos para solucionarlo

1.Definir y almacenar el valor de X1
2.Definir y almacenar el valor de Y1
3.Definir y almacenar el valor de X2
4.Definir y almacenar el valor de Y2
5.Aplicar y almacenar el resultado de la formula euclidiana
5.Formula euclidiana (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)
6.Mostrar el resultado
"""
"""
0) Los paréntesis -> Cambiar el orden!!!
1) Potencias (Primero de derecha a izquierda)
2) Multiplicaciones y las divisiones (Primero de izquierda a derecha)
3) Sumas y restas (Primero de izquierda a derecha)
"""
X1 = 4
Y1 = 5
X2 = 0
Y2 = 0
formula = (((X2 - X1) ** 2) + ((Y2 - Y1) ** 2)) ** (1/2)
print("La distacia es: ", formula)