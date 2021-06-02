#Guardar cada uno de los elementos de una colección tipo cadena en un diccionario

#Versión con los conocimientos de la unidad 1-3:
cadena = 'hola'
diccionarioCadena = dict()

#Primera forma
# diccionarioCadena['primerValor'] = cadena[0]
# diccionarioCadena['segundoValor'] = cadena[1]
# diccionarioCadena['tercerValor'] = cadena[2]
# diccionarioCadena['cuartoValor'] = cadena[3]
# print(diccionarioCadena)

#Segunda forma
# for i,letra in enumerate(cadena):
#     diccionarioCadena[ 'Valor' + str(i) ] = letra
# print(diccionarioCadena)

#Generando colección de índices (llaves para el diccionario)
llaves = list(range(len(cadena)))
print("Llaves del futuro diccionario")
print(llaves)
print("Valores del futuro diccionario")
print(cadena)
print('Mostrar tuplas que constituirán el diccionario')
for i in range(len(cadena)):
    print( (llaves[i],cadena[i]) )
coleccionTuplas = zip( llaves,cadena )
print('Resultado del zip:',tuple(coleccionTuplas))
#Conversión completa
diccionarioCadena = dict( zip( range(len(cadena)),cadena ) )
print(diccionarioCadena)

# #Ilustrando un poco de zip
# nombres =       ['Juan','Luis','Ana']
# edades =        (12,15,22)
# tipoSangre =    ['A+','O+','AB+']
# palabra =       'Tripulante'
# listadoPacientes = list(zip(nombres,edades,tipoSangre,palabra))
# print(listadoPacientes)

#Colecciones que podemos extraer del diccionario
print('Llaves del diccionario: ',diccionarioCadena.keys())
print('Valores del diccionario: ',diccionarioCadena.values())
print('Items del diccionario: ', diccionarioCadena.items())







