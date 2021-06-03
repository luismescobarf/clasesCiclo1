#Colecciones:
# 1) Cadenas
# 2) Listas
# 3) Tuplas
# 4) Conjuntos
# 5) Diccionarios

#Convertir cadenas a los demás (menos diccionario)
# cadena = 'mesopotamia'
# lista = list()
# for caracter in cadena:
#     lista.append(caracter)
# print(lista)
# --------------------
# cadena = 'mesopotamia'
# lista = list(cadena)
# print(lista)
# lista[4] = lista[4].upper()
# print(lista)
# #--------------------
# cadena = 'mesopotamia'
# tupla = tuple(cadena)
# print(tupla)
#--------------------
# cadena = 'mesopotamia'
# conjunto = set(cadena)
# print(conjunto)

#Convertir listas a los demás contenedores
lista = ['m', 'e', 's', 'o', 'p', 'o', 't', 'a', 'm', 'i', 'a']
# cadena = str()
# for caracter in lista:
#     cadena += caracter
# print(cadena)
# cadena = ''.join(lista)
# print(cadena)
#------------------------
# tupla = tuple(lista)
# print(tupla)
#------------------------
# lista = ['m', 'e', 's', 'o', 'p', 'o', 't', 'a', 'm', 'i', 'a',12,12,55,66,66]
# conjunto = set(lista)
# print(conjunto)
#---------------

# #Diccionario a los demás contenedores:
# diccionario = { (12,'Armenia'):'p',1:'a',2:'t',3:'o','valor':'o'}
# diccionario[ (12,'Armenia') ] = 'G'
# llaves = set(diccionario.keys())
# valores = set(diccionario.values())
# items = list(diccionario.items())
# print("Llaves: ",llaves,type(llaves))
# print("Valores: ",valores,type(valores))
# print("Items: ",items,type(items))

# #Armar la cadena únicamente con los valores
# cadenaValores = ''.join(list(diccionario.values()))
# print(cadenaValores)
# #Armar la cadena únicamente con los valores (sin repeticiones)
# cadenaValores = ''.join(set(diccionario.values()))
# print(cadenaValores)

#De los demás iterables a diccionarios
# cadena = '12 patos'
# diccionarioValores = dict()
# for i,letra in enumerate(cadena):
#     diccionarioValores[ 'Etiqueta_'+str(i) ] = letra
# print(diccionarioValores)
# -------------------------------
# cadena = '12 pp atos'
# diccionarioLlaves = dict()
# for i,letra in enumerate(set(cadena)):
#     diccionarioLlaves[ letra ] = i
# print(diccionarioLlaves)
# print('Cadena -> ',len(cadena))
# print('Diccionario -> ',len(diccionarioLlaves))

# cadena = '12 pp atos'
# diccionarioLlaves = dict()
# for i,letra in enumerate(set(cadena)):
#     diccionarioLlaves[ letra ] = i
# print(diccionarioLlaves)
# print('Cadena -> ',len(cadena))
# print('Diccionario -> ',len(diccionarioLlaves))

#Comprensión de listas
lista = ['m', 'e', 's', 'o', 'p', 'o', 't', 'a', 'm', 'i', 'a']
[ print(x,end='-') for x in lista ]
print()

#Generar una nueva lista con los elementos de la anterior
nuevaListaAleternado = [ lista[i] for i in range(0,len(lista),2) ]
print(nuevaListaAleternado)

#Nueva lista en mayúsculas
listaMayusculas = [ letra.upper() for letra in lista ]
print(listaMayusculas)

#Lista de vocales de la lista ingresada (condicional) (sin repeticiones)
vocalesLista = set([ letra for letra in lista if letra in {'a','e','i','o','u'} ])
print(vocalesLista)

#Requerimiento Héctor: diferencia de listas (conjuntos)
lista1 = ['a',2,'b','c','i','u',12,33,'perro','3',(12,55)]
lista2 = ['a',2,(12,55),'yate',33]
diferenciaListas = [ e for e in lista1 if e not in lista2 ]
print(diferenciaListas)

#Comprensión de listas -> Diccionario
#Convertir la cadena a un diccionario donde esta constituye los valores
#Forma convencional (no pythonista)
# cadena = '12 patos'
# diccionarioValores = dict()
# for i,letra in enumerate(cadena):
#     diccionarioValores[ 'Etiqueta_'+str(i) ] = letra
# print(diccionarioValores)
cadena = '12 patos'
diccionario = { 'Etiqueta_'+str(i):letra for i,letra in enumerate(cadena) }
print(diccionario)
diccionario = { letra:'Etiqueta_'+str(i) for i,letra in enumerate(cadena) }
print(diccionario)

#En una sola línea (máximo 2) -> solicitar n números al usuario y retornar
#la lista de los números que son múltiplos o de 5 o de 3. Pendiente promedio de los números

#Conversión a diccionario teniendo colecciones
llaves = ['a',2,'b','c','i','u',12,33,'perro','3',(12,55)]
valores = ['a',2,(12,55),'yate',33]
"""coleccionParejas = list(zip(llaves,valores))
print()
print()
print(coleccionParejas)"""
diccionario = dict(zip(llaves,valores))
print(diccionario)

cadena = 'mesopotamia'
diccionario = dict(zip(range(len(cadena)),cadena))
print(diccionario)











