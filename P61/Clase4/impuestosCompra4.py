#Cómo veníamos trabajando:

#1) Se necesita una solución que calcule el IVA sobre una compra
#de hasta 4 productos. Retornar cuánto se debe pagar adicional.

#Objetivo Algoritmo -> Cálculo de impuesto IVA sobre los productos ingresado.

# Algoritmo (pseudocódigo)
# 1) Recoger valor compra del primer producto
# 2) Recoger valor compra del segundo producto 
# 3) Recoger valor compra del tercer producto 
# 4) Recoger valor compra del cuarto producto
# 5) Cargar valor del IVA
# 6) Inicializar acumulado de impuesto (pago adicional)
# 7) Acumular impuesto del primer producto
# 8) Acumular impuesto del segundo producto
# 9) Acumular impuesto del tercer producto
# 10) Acumular impuesto del cuarto producto
# 11) Reportar pago adicional (impuestos)

#Traducción o transcripción
#from logica import propuesta1CalculoIVA_4 as p1_iva
from logica import propuesta2CalculoIVA_4 as p2_iva
#from logica import propuesta3CalculoIVA_4 as p3_iva
from interfaz import *

# producto1 = 1200000
# producto2 = 1500000
# producto3 = 500000
# producto4 = 4000000

#Interacción con el usuario
# print("---------------------------------------------")
# print("Bienvenido aplicación cálculo de impuesto IVA")
# print("---------------------------------------------")
bienvenida()
# producto1 = int(input("Precio producto 1: "))
# producto2 = int(input("Precio producto 2: "))
# producto3 = int(input("Precio producto 3: "))
# producto4 = int(input("Precio producto 4: "))
producto1,producto2,producto3,producto4 = recoleccionInformacion()

# #Lógica del proceso
# IVA = 0.19
# pagoAdicional = 0
# pagoAdicional = pagoAdicional + (producto1 * IVA)
# pagoAdicional = pagoAdicional + (producto2 * IVA)
# pagoAdicional = pagoAdicional + (producto3 * IVA)
# pagoAdicional = pagoAdicional + (producto4 * IVA)
# #sum( (producto1,producto2,producto3,producto4) ) * IVA
#pagoAdicional = p1_iva(producto1,producto2,producto3,producto4)
pagoAdicional = p2_iva(producto1,producto2,producto3,producto4)

#Interacción con el usuario
#print("El pago adicional es: ",pagoAdicional)
print(reporte(pagoAdicional))
# print("---------------------------------------------")
# print("Fin de la aplicación. Hasta luego")
# print("---------------------------------------------")
despedida()