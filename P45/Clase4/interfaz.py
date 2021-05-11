def bienvenida():
    print("-------------------------------------------")
    print("Bienvenido: Aplicación Cálculo de Impuestos")
    print("-------------------------------------------")

def recogerPrecio4Productos():
    producto1 = float(input('Ingrese el valor del primer producto: '))
    producto2 = float(input('Ingrese el valor del segundo producto: '))
    producto3 = float(input('Ingrese el valor del tercer producto: '))
    producto4 = float(input('Ingrese el valor del cuarto producto: '))
    return producto1,producto2,producto3,producto4

def reporte(precioRealCompra):
    #return "Precio final de compra:"+str(precioRealCompra)
    return f"Precio final de compra: {precioRealCompra}"

def finalizacionExitosa():
    print("-------------------------------------------")
    print("Finalización Exitosa")
    print("-------------------------------------------")