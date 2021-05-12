#Objetivo -> Contar los múltiplos de 3 y múltiplos de 5
#en la entrada

#Algoritmo -> Diagrama de Flujo

#Traducción -> Python

#Interacción con el usuario
print("Ingrese tres números: ")
a = int(input())
b = int(input())
c = int(input())

#Lógica
contadorMul3 = 0
contadorMul5 = 0
#Primera entrada
if not( a % 5 > 0 ):
    #contadorMul5 = contadorMul5 + 1
    contadorMul5 += 1
if not( a % 3 > 0 ):
    #contadorMul5 = contadorMul5 + 1
    contadorMul3 += 1
#Segunda entrada
if not( b % 5 > 0 ):
    #contadorMul5 = contadorMul5 + 1
    contadorMul5 += 1
if not( b % 3 > 0 ):
    #contadorMul5 = contadorMul5 + 1
    contadorMul3 += 1
#Tercera entrada
if not( c % 5 > 0 ):
    #contadorMul5 = contadorMul5 + 1
    contadorMul5 += 1
if not( c % 3 > 0 ):
    #contadorMul5 = contadorMul5 + 1
    contadorMul3 += 1

#Interacción
#mensaje = "En el ingreso hay "+str(contadorMul3)+" múltiplo(s) de 3 y "+str(contadorMul5)+"múltiplo(s) de 5"
#mensaje = f"En el ingreso hay {contadorMul3} múltiplo(s) de 3 y {contadorMul5} múltiplo(s) de 5"
#print(mensaje)
print("En el ingreso hay ",contadorMul3," múltiplo(s) de 3 y ",contadorMul5,"múltiplo(s) de 5")

