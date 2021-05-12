def clasificarEntradas(a,b,c):

    def acumularMultiplo3(x,contadorMul3):
        if not( x % 3 > 0 ):    
            contadorMul3 += 1
        return contadorMul3

    def acumularMultiplo5(x,contadorMul5):
        if not( x % 5 > 0 ):    
            contadorMul5 += 1
        return contadorMul5

    contadorMul3 = contadorMul5 = 0
    #contadorMul3, contadorMul5 = 0,0
    contadorMul3 = acumularMultiplo3(a, contadorMul3)
    contadorMul5 = acumularMultiplo5(a, contadorMul5)
    contadorMul3 = acumularMultiplo3(b, contadorMul3)
    contadorMul5 = acumularMultiplo5(b, contadorMul5)
    contadorMul3 = acumularMultiplo3(c, contadorMul3)
    contadorMul5 = acumularMultiplo5(c, contadorMul5)
    return contadorMul3,contadorMul5