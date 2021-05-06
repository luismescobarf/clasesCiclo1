def propuesta1CalculoIVA_4(producto1=0,producto2=0,producto3=0,producto4=0):
    #Lógica del proceso
    IVA = 0.19
    pagoAdicional = 0
    pagoAdicional = pagoAdicional + (producto1 * IVA)
    pagoAdicional = pagoAdicional + (producto2 * IVA)
    pagoAdicional = pagoAdicional + (producto3 * IVA)
    pagoAdicional = pagoAdicional + (producto4 * IVA)
    return pagoAdicional

def propuesta2CalculoIVA_4(producto1=0,producto2=0,producto3=0,producto4=0):
    #Lógica del proceso
    IVA = 0.19    
    pagoAdicional = (producto1+producto2+producto3+producto4)*IVA
    return pagoAdicional

def propuesta3CalculoIVA_4(producto1=0,producto2=0,producto3=0,producto4=0):
    #Lógica del proceso
    IVA = 0.19   
    return sum( (producto1,producto2,producto3,producto4) ) * IVA