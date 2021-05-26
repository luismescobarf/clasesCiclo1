#Ejemplo para tuplas -> Coleccionar información y que no se modifique

#Obtuvimos coordenadas de un punto
valor_x = 12
valor_y = 23
punto1 = ( valor_x, valor_y, 'La Candelaria' )
valor_x = 18
valor_y = 77
punto2 = ( valor_x, valor_y, 'Chapinero')
puntosRecogida = (punto1, punto2)

#Recorriendo la tupla de tuplas
print("Mostrando Puntos de Recogida")
for i,punto in enumerate(puntosRecogida):
    print(i+1," ",punto)

print("Mostrando Puntos de Recogida con Subíndice")
for i in range(len(puntosRecogida)):
    print(i+1," ",puntosRecogida[i])

print("Mostrando Componente en X de los Puntos de Recogida")
for i,punto in enumerate(puntosRecogida):
    print(i+1," Componente en X: ",punto[0])
    #print(i+1," Componente en Y: ",punto[1])
    #print(i+1," Barrio: ",punto[2])

print("Mostrando Componente en Y de los Puntos de Recogida con Subíndice")
for i in range(len(puntosRecogida)):    
    print(i+1," Componente en Y: ",puntosRecogida[i][1])    

"""
print("Puntos de recogida -> ",puntosRecogida)

print('Tupla con el punto 1',punto1)
print('Tipo de dato del punto 1',type(punto1))
print('Tamaño de la tupla',len(punto1))

print('Tupla con el punto 2',punto2)
print('Tipo de dato del punto 2',type(punto2))
print('Tamaño de la tupla',len(punto2))

tupla = (3.5,4.8,3.9)
print('La sumatoria de los elementos de la tupla: ',round(sum( tupla ),2))
"""
