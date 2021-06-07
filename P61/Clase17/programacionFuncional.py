#Funcional híbrido (Python): 1) Minimizar las asignaciones (cambios de estado de variables)
#Scala, Clojure, Haskell, Scheme -> Asignaciones (Puentes)
#2) Funciones como variables:   - Funciones de primera clase
#                               - Funciones de orden superior
#3) Evita acceso a estados globales

#Calculadora -> Recibe un caracter con el operador, construye 
#funciones y aplica a los argumentos la función construída

def operacion(signo):
    if signo == '+':
        #Función de primera clase
        def suma(a=0,b=0): #if a==None: a=0
            return a+b
        #envolturaFuncion = suma
        return suma #Wrapper
    elif signo == '-':        
        def resta(a=0,b=0):
            return a-b        
        return resta #Wrapper
    elif signo == '*':        
        def multiplicacion(a=0,b=0):
            return a*b        
        return multiplicacion #Wrapper
    elif signo == '/':        
        def division(a=0,b=1):
            return a//b        
        return division #Wrapper
    else:
        def funcionGenerica(a=0,b=0):
            return (a,b)
        return funcionGenerica

#Recibe operandos, solicita la construcción de la operación y aplica esa operación
def calculadora(signo, a, b):
    #Solicitar construcción de la función que va a aplicar (otra función)
    funcionParaAplicar = operacion(signo)
    #Tomar la función construída y aplicarla a los operandos y retornar el resultado
    return funcionParaAplicar(a,b)    
    """
    #Forma compacta
    return operacion(signo)(a,b)
    """    

#Sección principal
#-----------------
print(calculadora('+',4,5))
print(calculadora('-',-34,5))
print(calculadora('/',12,4))
print(calculadora('*',45,5))
print(calculadora('?',45,5))

