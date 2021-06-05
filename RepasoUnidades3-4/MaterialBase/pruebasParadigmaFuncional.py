#Importar las definiciones de los diccionarios
from casosGenerados import *
import random
from functools import reduce


#Básicos de paradigma de programación funcional (enfoque de Python)
#-----------------------------------------------------------------
#Minimizar actualizaciones de variables (asignaciones), dado que Python es híbrido.
#Funciones de primera clase y funciones de orden superior

#Definir calculadora de forma funcional
def calculadora(signo,a,b):
    #Construir la función solicitada por el signo
    operacion = construirOperacion(signo)
    #Aplicar la función a los operandos y retornar el resultado
    return operacion(a,b)

#Función de orden superior (retorna una función como variable)
def construirOperacion(signo):

    #Retornar alguna de las funciones de primera clase
    if signo == '+':
        def suma(a=0,b=0):
            return a+b
        return suma
    elif signo == '-':
        def resta(a=0,b=0):
            return a-b
        return resta
    elif signo == '*':
        def multiplicacion(a=0,b=0):
            return a*b
        return multiplicacion
    elif signo == '/':
        def division(a=0,b=1):
            return a/b
        return division
    else:
        print(f"Signo {signo} inválido!")
        def funcionSinEfectos(a,b):
            return a,b
        return funcionSinEfectos

#Sección principal
#print("El resultado de la operación ingresada es = ", calculadora( input('Signo:'), int(input('a->')), int(input('b->'))))

#Maper -> Aplicar una función recibida a cada uno de los elementos de una lista
def mapeador(funcion,lista): 
    #Generar un nuevo iterable del mismo tipo (programación imperativa)
    nuevaLista = [0] * len(lista)
    for i in range(len(lista)):
        nuevaLista[i] = funcion( lista[i] )    
    return nuevaLista
    # #Alternativa funcional/híbrida de Python
    # return [ funcion(elemento) for elemento in lista ]    
    
#Funciones para aplicar
def cuadrado(x):
    return x**2

def cubo(x):
    return x**3

def decremento(x):
    return x-1

def incremento(x):
    return x-1

def operacion(x,constante):
    return (x**2)+constante

#Sección principal
#-----------------

#Generar colección
n = 10
numeros = list(range(1,n+1))

#Mapeador parcial
print("Elevados al cuadrado:", mapeador(cuadrado,numeros))
print("Elevados al cubo:", mapeador(cubo,numeros))
print("Decrementados:", mapeador(decremento,numeros))
print("Incrementados:", mapeador(incremento,numeros))
print('------------------------------------------------------')
print("Aplicando operación:", mapeador(lambda x:x+2,numeros))

#Map, filter, reduce, zip
frutas = [
    ['manzana',200,True],
    ['pera',100,False],
    ['piña',10,True],
    ['banano',200,False],
    ['naranja',1000,True],
    ['palta',500,False]
]

#Decrementar a la mitad el pedido de cada una de las frutas (ejemplo de map)
pedidosDecrementados = list(map( lambda x:[x[0],x[1]//2] , frutas ))
print("Resultado de la aplicación del map: ",pedidosDecrementados)

#Extraer las frutas que empiezan por p y dividir entre dos la cantidad que se va a pedir

#Predicado -> Empieza o no por P (mayúscula para cubrir ambos casos)
def empiezaPorP(fruta):
    return fruta[0][0].upper() == 'P'

#Realización del filtro
frutasP = list(filter(empiezaPorP, frutas))
print("Resultado del filtro letra p: ",frutasP)

#Disminución del pedido
def descuento(fruta):    
    fruta[1] = fruta[1]//2
    return fruta
listadoFrutasProcesado = list( map(descuento,frutasP) )
print("Decremento únicamente a las que tienen letra P -> ",listadoFrutasProcesado)

#Dividir entre dos el pedido de todas las frutas que deben pagar impuestos (map de una función más elaborada)

def dividirPedidoCondicionado(fruta):
    if fruta[-1]:
        fruta[1] = fruta[1]//2
    return fruta
print('Listado de frutas antes del proceso:')
[print(x) for x in frutas]

frutas = list( map(dividirPedidoCondicionado, frutas) )

print('Listado de frutas después del proceso:')
[print(x) for x in frutas]

#Generar ids con las frutas
def agregarID(fruta):    
    id = fruta[0][0]+fruta[0][-1]+str(fruta[1])+str(int(fruta[-1]))
    fruta.insert(0, id)
    return fruta
listadoFrutasCodificadas = list( map( agregarID, frutas ) )
print('Listado de frutas después del proceso:')
[print(x) for x in listadoFrutasCodificadas]
   

#Requerimiento caso de estudio: obtener todas las transacciones realizadas en el primer trimestre del 2021 con cajeros modelo 101 y 2017.

#Modelos de interés del requerimiento
modelos = {101,2017}



#Predicados que componen el requerimiento
def enEnero2021(transaccion):
    return 
    




    












