def precioFinalVenta(producto1,producto2,producto3,producto4):
    #Lógica
    IVA = 0.19
    acumuladorImpuestos = 0
    #acumuladorImpuestos = acumuladorImpuestos + (producto1 * IVA)
    acumuladorImpuestos += producto1 * IVA
    acumuladorImpuestos += producto2 * IVA
    acumuladorImpuestos += producto3 * IVA
    acumuladorImpuestos += producto4 * IVA
    #precioTotalProductos = producto1 + producto2 + producto3 + producto4
    precioTotalProductos = sum((producto1,producto2,producto3,producto4))
    precioRealCompra = precioTotalProductos + acumuladorImpuestos
    return precioRealCompra

def precioFinalVenta2(producto1,producto2,producto3,producto4):
    return sum((producto1,producto2,producto3,producto4)) * 1.19