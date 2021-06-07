#Filter -> Recibir una colección y una función y filtrar la colección

#Colección -> Héctor
salarios=[1100, 1100, 1500, 1200, 1200, 1700, 1250, 1250, 1900, 1100]

#Requerimiento para cada elemento
def bonificacion(salario):
    return salario*1.05

def bonificacionMenor(salario):
    return salario*1.03

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

#Requerimiento: Obtener solamente los salarios y además bonificados que hay que pagar con 
#bonificación del 3% (mayores a 1500)

#Filter -> Predicado y retorna la colección filtrada

#Predicado de salarios que reciben bonificación del 3%
def recibeBonificacionMenor(salario):
    return salario > 1500

#print("Salarios que reciben bonificación menor:", list(filter(recibeBonificacionMenor,salarios)))
#print("Salarios que reciben bonificación menor:", list(filter(lambda salario:salario>1500,salarios)))
#print("Número de Salarios que reciben bonificación menor:", len(list(filter(lambda salario:salario>1500,salarios))))

rqBonificadosMenor = list(map(bonificacionMenor,  list((filter( lambda salario:salario>1500,salarios )))))
print("Salarios bonificados (menor)",rqBonificadosMenor)
print("Cantidad Salarios bonificados (menor)",len(rqBonificadosMenor))
print("Total  Salarios Modificados",sum(rqBonificadosMenor))
print('----------------')
rqContrario = list(map(bonificacion,  list((filter( lambda salario:salario<=1500,salarios )))))
print("Salarios bonificados (mayor)",rqContrario)
print("Cantidad Salarios bonificados (mayor)",len(rqContrario))
print("Total  Salarios Modificados",sum(rqContrario))
