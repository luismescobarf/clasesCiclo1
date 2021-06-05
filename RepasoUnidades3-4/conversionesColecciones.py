#Principales

#Cadena a lista: aprovechando la mutabilidad de la lista para actualizar la cadena
cadena = 'misionTIC'
lista = list(cadena)
lista[0] = lista[0].upper()
lista[-1] = lista[-1].lower()
cadena = ''.join(lista)
print(cadena)

#Eliminar repeticiones convirtiendo cadena a conjunto (perdemos el orden)
cadena = 'hhoolaaa'
conjunto = set(cadena)
print("Versión conjunto de la cadena: ",conjunto)
cadena = ''.join(conjunto)
print("Versión de la cadena sin repeticiones: ",cadena)

#Convertir cadena a diccionario -> satisfacer la llave
cadena = 'prueba'
diccionario = dict()
for i,caracter in enumerate(cadena):
    diccionario[i] = caracter
print('Diccionario resultante: ',diccionario)

diccionario = dict( zip( range(len(cadena)) , cadena )  )
print('Conversión a Diccionario en una sola línea',diccionario)
