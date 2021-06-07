#Híbrido Programación Funcional en Python:
#1) Minimizar las asignaciones a variables (cambios de estado de las variables)
#2) Tratamos a las funciones como variables: - Funciones de primera clase
#                                            - Funciones de orden superior
#3) Minimizar el acceso a estados globales

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

#Utilizar función
print(calculadora('+',7,8))
print(calculadora('-',-12,8))
print(calculadora('*',1555,4))
print(calculadora('/',88,2))
print(calculadora('akjsdlkajsdlk',7,8))
#Utilizar función recogiendo información del teclado
print(calculadora(input('Signo->'),int(input('a = ')),int(input('b = '))))

#Construir nuestro propio map
#Map -> recibo función y colección y retorno cada uno de los elementos de la colección después de aplicarles la función



