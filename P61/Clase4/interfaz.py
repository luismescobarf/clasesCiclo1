def bienvenida():
    print("---------------------------------------------")
    print("Bienvenido aplicación cálculo de impuesto IVA")
    print("---------------------------------------------")

def recoleccionInformacion():
    producto1 = int(input("Precio producto 1: "))
    producto2 = int(input("Precio producto 2: "))
    producto3 = int(input("Precio producto 3: "))
    producto4 = int(input("Precio producto 4: "))
    return producto1, producto2, producto3, producto4

def reporte(pagoAdicional):
    #return "El pago adicional es: " + str(pagoAdicional)
    return f"El pago adicional es: {pagoAdicional}"

def despedida():
    print("---------------------------------------------")
    print("Fin de la aplicación. Hasta luego")
    print("---------------------------------------------")

    