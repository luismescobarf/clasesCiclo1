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