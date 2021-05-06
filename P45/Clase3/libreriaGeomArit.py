def areaCirculo(radio):
    pi = 3.1416
    radioCuadrado  = radio**2
    area = pi * radioCuadrado
    return area

def distanciaEuclidiana(X1=0,Y1=0,X2=0,Y2=0):
    resultado = (((X2 - X1) ** 2) + ((Y2 - Y1) ** 2)) ** (1/2)
    return resultado

def areaTriangulo(base=0,altura=0):
    resultado = (base*altura)/2
    return resultado

def areaCuadrado(lado=0):
    resultado = lado**2
    return resultado

def promedio4(valor1=0,valor2=0,valor3=0,valor4=0):
    promedio = sum( (valor1,valor2,valor3,valor4) ) / len( (valor1,valor2,valor3,valor4) )
    promedio = round(promedio,2)
    return promedio

def suma3(a=0,b=0,c=0):

    print("Contenido de a:",a)
    print("Contenido de b:",b)
    print("Contenido de c:",c)

    sumatoria = a + b + c
    return sumatoria

def diferencia3(valor1=0,valor2=0,valor3=0):

    print("Valor1:",valor1)
    print("Valor2:",valor2)
    print("Valor3:",valor3)
    
    diferencia = valor1 - valor2 - valor3
    return diferencia
