#Map -> Recibir una colección y una función y aplicar la función a la colección
#Desarrollar un Map sencillo

#Colección -> Héctor
salarios=[1100, 1100, 1500, 1200, 1200, 1700, 1250, 1250, 1900, 1100]

#Requerimiento -> se recibe una colección de salarios y se le va a aplicar a cada uno un bono del 5%

# #Procedural estructurada
# print("Salarios antes del bono: ",salarios)
# for i in range(len(salarios)):
#     salarios[i] = salarios[i] + salarios[i]*0.05
# print("Salarios con bonificación: ",salarios)

#Híbrido funcional -> map

#Requerimiento para cada elemento
def bonificacion(salario):
    return salario*1.05

#Requerimiento Freddie: si el salario es superior a 1500 solo el 3% 
def bonificacionCondicionada(salario):
    # if salario > 1500:
    #     return salario*1.03
    # else:
    #     return salario*1.05
    return (salario*1.03 if salario > 1500 else salario*1.05)    

def aportesIndependiente(salario):
    return round(salario/1.048,2)

def aportesEmpleado(salario):
    return round(salario*(1-0.12),2)

def aumentoFinAño(salario):
    return salario * 1.02

def bonificacionVentasAnuales(salario):
    return salario + 200

#Map casero
def mapCasero(funcionAplicar,coleccion):
    return [ funcionAplicar(elemento) for elemento in coleccion ]

#Responder al requerimiento con el map casero

# #Bonificación Héctor
# salarios = mapCasero(bonificacion,salarios)
# print('Salarios con la bonificación->',salarios)

# #Bonificación Freddie
# print(salarios)
# print('Bonificación sin condición:', mapCasero(bonificacion,salarios))
# salarios = mapCasero(bonificacionCondicionada,salarios)
# print('Salarios con la bonificación->',salarios)

#Freddie: Requerimiento aplicar aumento de fin de año y luego aplicar bonificación de ventas a los empleados
#7 + (12 + 8)<-
salarioFinAño = mapCasero(bonificacionVentasAnuales, mapCasero(aumentoFinAño,salarios))
print(salarios)
print(salarioFinAño)

# print("Salarios con bonificación (hechos con map): ", mapCasero(bonificacion,salarios))
# print("Aportes independiente (hechos con map): ", mapCasero(aportesIndependiente,salarios))
# print("Aportes empleado (hechos con map): ", mapCasero(aportesEmpleado,salarios))
# print("Salarios->",salarios)

#Map de Python
print('Map de Python', list(map(bonificacion,salarios)) )
#Funciones lambda -> funciones en una sola línea, envolver expresiones de parámetros y cómputs en una función
bonificacionSingleLine = lambda salario:salario*1.05
print('Uso de la función una línea',bonificacionSingleLine(1500))
print('Uso de la función una línea',bonificacion(1500))

salarios = list(map(lambda salario:salario*1.05,salarios))
print('Requerimiento con map y función anónima: ', salarios )

