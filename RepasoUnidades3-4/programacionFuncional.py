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

def operacion(signo):
    if signo == '+':
        def suma(a=0,b=0):
            return a+b
        #sumaEnVariable = suma
        return suma
    elif signo == '-':
        def resta(a=0,b=0):
            return a-b
        return resta
    else:
        def funcion(a,b):
            return (a,b)
        return funcion

def calculadora(signo,a,b):
    #Dependiendo del signo que reciba, solicita la construcción de una función
    funcionGenerada = operacion(signo)
    return funcionGenerada(a,b)

# print('Calculadora Funcional')
# print(calculadora(input('Signo->'),int(input('a->')),int(input('b->'))))
# print(calculadora(input('Signo->'),int(input('a->')),int(input('b->'))))
# print(calculadora(input('Signo->'),int(input('a->')),int(input('b->'))))

#Map, filter, reduce

#Map -> Función que recibe otra función para aplicársela a cada elemento de una colección
coleccion = list(range(1,20,3))
print("Colección :",coleccion)
#Procesos:
def decrementar(elemento):
    return elemento-1
def incrementar5(elemento):
    return elemento+5
def elevarCuadrado(elemento):
    return elemento**2
#Decrementar todos los elementos de la colección
#print(list(map(decrementar,coleccion)))
print(list(map(lambda elemento:elemento-1,coleccion)))
print(list(map(incrementar5,coleccion)))
print(list(map(elevarCuadrado,coleccion)))

#Filtrado -> predicado (función que retorna un valor booleano)
def esPar(valor):
    return valor%2==0
#Solamente los pares de la colección
print(list( filter(esPar,coleccion) ))

#Reduce para realizar una productoria de la colección
from functools import reduce
print(reduce( lambda acumulador=1,valor=int(): acumulador*valor, coleccion   ) )

#Map convertir en una cadena la colección
cadena = ''.join(list(map(lambda x:str(x)+' ',coleccion)))
print("Versión Cadena Colección: ",cadena, type(cadena))

#Map convertir en una cadena la colección sin repeticiones
#Insertar repeticiones
coleccion.append(4)
coleccion.append(4)
coleccion.append(19)
coleccion.append(7)
print('Antes del proceso: ',coleccion)
cadena = ''.join(set(map(lambda x:str(x)+' ',coleccion)))
print("Versión Cadena Colección: ",cadena, type(cadena))

#Map convertir en una cadena la colección sin repeticiones y en orden
#Insertar repeticiones
coleccion.append(4)
coleccion.append(4)
coleccion.append(19)
coleccion.append(7)
print('Antes del proceso: ',coleccion)
cadena = ''.join(sorted(list(set(map(lambda x:str(x)+' ',coleccion)))))
print("Versión Cadena Colección: ",cadena, type(cadena))



    





