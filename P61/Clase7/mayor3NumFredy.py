"""
Recibir tres números enteros diferentes y determinar
con condicionales cuál es el mayor.
"""

#Algoritmo --> flujograma

print("Ingrese tres números enteros diferentes")

Num1 = input()
Num2 = input()
Num3 = input()

print("Revisión de tipos ingresados")
print(type(Num1))
print(type(Num2))
print(type(Num3))

if Num1 > Num2:
    if Num1 > Num3:
        msj = f"El número mayor es: {Num1}"
    else:
        msj = f"El número mayor es: {Num3}"
else:
    if Num2 > Num3:
        msj = f"El número mayor es: {Num2}"
    else:
        msj = f"El número mayor es: {Num3}"

print(msj)