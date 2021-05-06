def areaCirculo(radio):
    pi = 3.1416
    radioCuadrado  = radio**2
    area = pi * radioCuadrado
    return area

def distanciaEuclidiana(X1,Y1,X2,Y2):
    resultado = (((X2 - X1) ** 2) + ((Y2 - Y1) ** 2)) ** (1/2)
    return resultado

def areaTriangulo(base,altura):
    resultado = (base*altura)/2
    return resultado

def areaCuadrado(lado):
    resultado = lado**2
    return resultado

def promedio4(valor1,valor2,valor3,valor4):
    promedio = sum( (valor1,valor2,valor3,valor4) ) / len( (valor1,valor2,valor3,valor4) )
    promedio = round(promedio,2)
    return promedio

def suma3(a,b,c):

    print("Contenido de a:",a)
    print("Contenido de b:",b)
    print("Contenido de c:",c)

    sumatoria = a + b + c
    return sumatoria

def diferencia3(valor1,valor2,valor3):

    print("Valor1:",valor1)
    print("Valor2:",valor2)
    print("Valor3:",valor3)
    
    diferencia = valor1 - valor2 - valor3
    return diferencia
