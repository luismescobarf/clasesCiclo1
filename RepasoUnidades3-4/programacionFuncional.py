import pprint as pp

#Comprensión de Listas
lista = [
    [1,2,3],
    [1,55,3],
    ['Palabra',(9,1),10.6]
]
print(lista)
#Imprimir en líneas separadas
print("Mostrando elementos en líneas separadas")
for elemento in lista:
    print(elemento)
#Versión en comprensión de listas
print('-----------------------')
[print(elemento) for elemento in lista]

#Generar los números cuadrados a partir de los números del 1 al 10
cuadrados = list()
for num in range(1,11):
    cuadrados.append(num**2)
print('1 al 10 elevado al cuadrado: ',cuadrados)
print('-------')
#cuadradosNuevos = [ expresion iteraciones condicionales sobre las iteraciones ]
cuadradosNuevos = [ num**2 for num in range(1,11) ]
print('Colección Generada Comprensión de Listas: ',cuadradosNuevos)
print('-------')
diccionarioCuadrados = { num:num**2 for num in range(1,11) }
pp.pprint(diccionarioCuadrados)
print('-------')
diccionarioCuadradosPares = { num:num**2 for num in range(1,11) if num%2==0 and (num**2)%2==0 }
pp.pprint(diccionarioCuadradosPares)

#Programación funcional
#Minimizar el número de asignaciones
#Funciones de primera clase (variables), funciones de orden superior (reciben o retornan funciones)

def calculadora(signo):

    #Dependiendo del signo que reciba, solicita la construcción de una función
    pass





