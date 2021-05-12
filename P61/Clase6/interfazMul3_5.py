def recoleccionEntradas():
    #Interacción con el usuario
    print("Ingrese tres números: ")
    a = input()
    if a == '':
        a = 1
    else:
        a = int(a)
    b = input()
    if b == '':
        b = 1
    else:
        b = int(b)
    c = input()
    if c == '':
        c = 1
    else:
        c = int(c)
    
    return a,b,c

def reporteMultiplos(contadorMul3,contadorMul5):
    mensaje = f"En el ingreso hay {contadorMul3} múltiplo(s) de 3 y {contadorMul5} múltiplo(s) de 5"
    print(mensaje)