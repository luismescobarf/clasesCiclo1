#Objetivo -> Precio final de venta de productos cargados
#sin IVA

#Algoritmo:
# 1) Cargar el precio sin IVA de cada producto.
# 2) Cargar el valor del IVA (porcentaje, float)
# 3) Inicializamos un acumulador para el impuesto de cada 
# producto
# 4) Calcular el IVA del primer producto y sumarlo al 
# acumulador
# 5) Calcular el IVA del segundo producto y sumarlo al 
# acumulador
# 6) Calcular el IVA del tercer producto y sumarlo al 
# acumulador
# 7) Calcular el IVA del cuarto producto y sumarlo al 
# acumulador
# 8) Calculamos el valor total de los productos
# 9) Sumamos al valor total de los productos el acumulado
# de impuestos.

#Traducción LP -> Python
producto1 = 1200000
producto2 = 1500000
producto3 = 350000
producto4 = 4000000
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
print("Precio final de compra:",precioRealCompra)





