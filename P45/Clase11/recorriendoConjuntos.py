conjunto = set()

conjunto.add('elemento1')
conjunto.add('elemento2')
conjunto.add('elemento2')
conjunto.add('elemento2')

lista = ['elemento1','elemento1','elemento1','elemento2']
print('Contenido de la lista ',lista)

#Eliminar repeticiones
#listaSinRepeticiones = []
listaSinRepeticiones = list()
for e in lista:
    if  e not in listaSinRepeticiones:
        listaSinRepeticiones.append(e)
print("Lista filtrada: ", listaSinRepeticiones)

#lista = list(set(lista))
#print('Versión sin repeticiones ',lista)

conjuntoAnimales = {'Perro','Gato','Caballo', 12}
print("Conjunto de Animales: ",conjuntoAnimales)

print("Recorrido por los elementos del conjunto")
for animal in conjuntoAnimales:
    print(animal)


# listaCopiada = lista.copy()
# print('Lista generada con copy',listaCopiada)





print("Mostrar inicialización del conjunto: ",conjunto)
print(type(conjunto))