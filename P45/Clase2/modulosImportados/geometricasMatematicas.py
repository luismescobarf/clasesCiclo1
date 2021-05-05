def distEUC(valor_x1,valor_x2,valor_y1,valor_y2):
    resultado = ((valor_x1 - valor_x2) ** 2 + (valor_y2 - valor_y1) ** 2) ** (1/2)
    return resultado

def volumenCono(radio_2, alto_cono):
    pi = 3.1416
    resultado = (((pi * radio_2 ** 2) / 3) * alto_cono)
    return resultado

def promedioNotas(nota_1,nota_2,nota_3,nota_4):
    return sum( (nota_1,nota_2,nota_3,nota_4) )/ len((nota_1,nota_2,nota_3,nota_4))