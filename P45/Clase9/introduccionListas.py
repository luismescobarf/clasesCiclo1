#Listas -> Primer contenedor general
#Mutable -> cada casilla la podemos modificar
#CRUD -> Create, Read, Update, Delete
#En cada casilla podemos guardar información de cualquier tipo
#Cada posición tiene un índice (autonumérico)

#Ejemplo lista
lista = [12,56,7.9,'Hola Mundo']

#Requerimiento -> El usuario va a especificar el número
#de ingresos que va a realizar. Se va a identificar de
#esas entradas cuántos y cuáles de ellos son números pares
#y cuáles son impares. Además necesitamos saber a cuál de las
#entradas corresponde

#Objetivo -> Informar cuántos y cuales son pares e impares
#de las entradas recibidas, y en qué momento de la secuencia
#fueron ingresados

#Algoritmo
#1) Solicitar al usuario el número de entradas que va a realizar
#2) Por cada una de las entradas revisar si es número par
#3) Si es primo coleccionarlo
#3b) De lo contrario continuar solicitando las entradas  

#Trducción
n = int(input('Cuántos números va a ingresar?'))
coleccionNumerosPares = []
coleccionNumerosImpares = []
for i in range(n):
    num = int(input('Ingrese Número: ')) 
    if num % 2 == 0:
        #coleccionNumerosPares.append(num)
        coleccionNumerosPares.append([num,i])        
    else:
        #coleccionNumerosImpares.append(num)
        coleccionNumerosImpares.append([num,i])        

soloNumerosPares = []
for numero in coleccionNumerosPares:
    soloNumerosPares.append(numero[0])

soloNumerosImpares = []
for numero in coleccionNumerosImpares:
    soloNumerosImpares.append(numero[0])

print(f"Número Pares Ingresados : {len(coleccionNumerosPares)} Colección: {soloNumerosPares}")
print(f"Número Impares Ingresados : {len(coleccionNumerosImpares)} Colección: {soloNumerosImpares}")


#pares = [2,4]
#pares = [ [2,6], [4,7] ]








