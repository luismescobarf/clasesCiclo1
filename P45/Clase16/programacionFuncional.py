#Híbrido Programación Funcional en Python:
#1) Minimizar las asignaciones a variables (cambios de estado de las variables)
#2) Tratamos a las funciones como variables: - Funciones de primera clase
#                                            - Funciones de orden superior
#3) Minimizar el acceso a estados globales

import random

#Calculadora estilo programación funcional
def operacion(signo):
    if signo == '+':
        def suma(a=0,b=0):
            return a + b
        return suma
    elif signo == '-':
        def resta(a=0,b=0):
            return a - b
        return resta
    elif signo == '*':
        def multiplicacion(a=0,b=0):
            return a * b
        return multiplicacion
    elif signo == '/':
        def division(a=0,b=1):
            return a // b
        return division
    else:
        def f(a=0,b=0):
            return (a,b)
        return f

def calculadora(signo, a, b):

    #Construir o solicitarle a otra función la construcción del proceso que debe hacer
    #funcionAplicar = operacion(signo)

    #Aplicar función que cunstruída en tiempo de ejecución
    #return funcionAplicar(a,b)

    #Forma resumida
    return operacion(signo)(a,b)

# #Utilizar función
# print(calculadora('+',7,8))
# print(calculadora('-',-12,8))
# print(calculadora('*',1555,4))
# print(calculadora('/',88,2))
# print(calculadora('akjsdlkajsdlk',7,8))
# #Utilizar función recogiendo información del teclado
# #print(calculadora(input('Signo->'),int(input('a = ')),int(input('b = '))))

#Construir nuestro propio map**
#Map -> recibo función y colección y retorno cada uno 
#de los elementos de la colección después de aplicarles la función. (retornamos colección)

#Requerimiento -> el docente quiere ayudar con 2 décimas de una actividad a los estudiantes 
# por las dificultades presentadas (sumar 2 décimas a cada elemento)

notas = [3.5, 3.0, 4.4, 3.2, 1.0, 3.8, 2.1, 3.7, 4.0]

# #Imperativa
# print('Notas antes de bonificación: ',notas)
# for i in range(len(notas)):
#     notas[i] = round(notas[i] + 0.2,2)
# print('Notas después de bonificación: ',notas)

#Declarativa
def mapBasico(funcion,coleccion):
    return [ funcion(elemento) for elemento in coleccion ]

def bonificacion(nota):
    return round(nota + 0.2, 2)

def bonificacionCondicionada(nota):
    # if nota<=3.5:
    #     return round(nota + 0.2, 2)
    # else:
    #     return nota
    return ( round(nota + 0.2, 2)  if nota<=3.5 else nota )

def penalidad(nota):
    return round(nota - 0.1, 2)

def bonificacionPorcentual(nota):
    return round(nota + nota * 0.15, 2)

#Solución al requerimiento de forma declarativa (map básico)
print('Notas antes de bonificación: ', notas)
# print('Notas después de bonificación: ', mapBasico(bonificacion,notas) )
# print('Notas después de penalidad: ', mapBasico(penalidad,notas) )
# print('Estado de notas ->',notas)

#5 + (8+12)<-
#Requerimiento bonificación basada en nota actual y luego penalidad a todo el grupo
#print("Requerimiento: ",mapBasico(penalidad, mapBasico(bonificacionPorcentual,notas) )  )

#Bonificación condicionada
print("Ayuda a los que tienen peor nota: ", mapBasico(bonificacionCondicionada,notas) )

#Ejemplo funciones lambda para la penalidad
print('Notas después de penalidad: ', mapBasico(penalidad,notas) )
print('Notas después de penalidad lambda: ', mapBasico( lambda x: round(x - 0.1, 2) , notas) )

#Requerimientos planteados:
#Fernando -> notas de estudiantes y sacar promedios
#Daniel ->  Recibir informacion de un usuario y crear el código 
#           compuesto por el nombre, apellido y identificacion

#Generar aleatoriamente los casos para los requerimientos planteados

#Generar notas de estudiantes aleatoriamente
def generarNotasGrupoAleatorias():
    notasPosibles = (0,1,2,3,4,5,3.3,3.8,4.2,2.4)
    cortesSemestre = 4
    numeroEstudiantes = 8
    grupoEstudiantes = list()
    for _ in range(numeroEstudiantes):
        grupoEstudiantes.append([notasPosibles[random.randint(0,len(notasPosibles)-1)] for _ in range(cortesSemestre)])
    return grupoEstudiantes

#Generar el caso
grupoEstudiantes = generarNotasGrupoAleatorias()
print('Notas Grupo: ')
[print(estudiante) for estudiante in grupoEstudiantes]
    

    




    







