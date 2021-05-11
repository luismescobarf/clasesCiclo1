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

from logica import precioFinalVenta as pfv
from logica import precioFinalVenta2 as pfv2
from interfaz import bienvenida as bv
from interfaz import recogerPrecio4Productos as r4p
from interfaz import reporte as rp
from interfaz import finalizacionExitosa as fe

#Traducción LP -> Python
# producto1 = 1200000
# producto2 = 1500000
# producto3 = 350000
# producto4 = 4000000

#Interacción
# print("-------------------------------------------")
# print("Bienvenido: Aplicación Cálculo de Impuestos")
# print("-------------------------------------------")
bv()
# producto1 = float(input('Ingrese el valor del primer producto: '))
# producto2 = float(input('Ingrese el valor del segundo producto: '))
# producto3 = float(input('Ingrese el valor del tercer producto: '))
# producto4 = float(input('Ingrese el valor del cuarto producto: '))
producto1,producto2,producto3,producto4 = r4p()

#Lógica
#precioRealCompra = pfv(producto1,producto2,producto3,producto4)
precioRealCompra = pfv2(producto1,producto2,producto3,producto4)

#Interacción
#print("Precio final de compra:",precioRealCompra)
print(rp(precioRealCompra))
# print("-------------------------------------------")
# print("Finalización Exitosa")
# print("-------------------------------------------")
fe()
 



