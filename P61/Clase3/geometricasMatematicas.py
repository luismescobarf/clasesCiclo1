def distEUC(valor_x1=0,valor_x2=0,valor_y1=0,valor_y2=0):
    resultado = ((valor_x1 - valor_x2) ** 2 + (valor_y2 - valor_y1) ** 2) ** (1/2)
    return resultado

def volumenCono(radio_2=0, alto_cono=0):
    pi = 3.1416
    resultado = (((pi * radio_2 ** 2) / 3) * alto_cono)
    return resultado

def aRectangulo(l=1,a=1):
    #print("El largo recibido es: ",l)
    #print("El ancho recibido es: ",a)
    resultadoArea = l * a
    return resultadoArea

def promedioNotas(nota_1=1.0,nota_2=1.0,nota_3=1.0,nota_4=1.0):
    return sum( (nota_1,nota_2,nota_3,nota_4) )/ len((nota_1,nota_2,nota_3,nota_4))