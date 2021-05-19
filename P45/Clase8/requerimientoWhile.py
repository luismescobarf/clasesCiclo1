#Requerimiento: escribir un programa que le permita al usuario
#ingresar cuantos números quiera y al final reportar cuántos
#de esos números son múltiplos de 5 y cuántos son múltiplos de 3,
#recordar que hay números que pueden ser múltiplos de ambos

#Objetivo -> Reportar cantidad de múltiplos de 5 y múltiplos de 3
#entre los números ingresados

#Algoritmo (pseudocódigo)
# 1) Inicializar contadores
# 2) Mientras el usuario quiera ingresar números
# 2a) Capturar el número
# 2b) Revisar si es múltiplo de 3 y de 5 y actualizar contadores
# 3) Cuando el usuario reporte que no quiere ingresar más números,
#     informaro cuántos de los ingresados fueron múltiplos de 5
#     y cuántos fueron múltiplos de 3

#Múltiplo 5 -> 5 * cantidad; 25 -> 5 * 5

#Traducción a Python
contadorMultiplos3 = 0
contadorMultiplos5 = 0
quiereIngresarNumeros = True
while quiereIngresarNumeros:
    numero = int(input("Ingrese número: "))
    if numero % 3 == 0:
        contadorMultiplos3 += 1 
    if numero % 5 == 0:
        contadorMultiplos5 += 1
    # respuesta = input("Desea continuar? (s/n)")
    # if respuesta == 'n':
    #     quiereIngresarNumeros = False    
    quiereIngresarNumeros = input("Desea continuar? (s/n)") != 'n'
    
print(f"Múltiplos de 5: {contadorMultiplos5} y Múltiplos de 3: {contadorMultiplos3}")



