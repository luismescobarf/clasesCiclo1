#Objetivo: calcular precio de compra
#aplicando descuento cuando
#los productos ingresados superan 3000 u.m.

#Algoritmo -> Digrama de flujo

#Traducción al lenguaje -> Python!!!
a = int(input('Ingrese el primer producto: '))
b = int(input('Ingrese el segundo producto: '))
c = a + b
if c > 3000:
    c = c * 0.90
print("La compra después del descuento es",c)

