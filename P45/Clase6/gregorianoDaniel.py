""" Objetivo => Calcular si un año es biciesto o no, retornar el año y un mensaje si es o no bisiesto """

def CalcularAñoBisiesto(Año):
    AñoBisiesto = False

    if Año % 4 == 0:
        if Año % 100 == 0:
            if Año % 400 == 0:
                AñoBisiesto = True
        else:
            AñoBisiesto = True    

    if AñoBisiesto == True:
        return f"\n El año {Año} es bisiesto"
    else:
        return f"\n El año {Año} no es bisiesto"

#Año = int(input("Ingrese el año: "))
#print(CalcularAñoBisiesto(Año))

#Casos de Prueba
print("Casos BISIESTOS")
print(CalcularAñoBisiesto(2000))
print(CalcularAñoBisiesto(2400))
print(CalcularAñoBisiesto(2020))
print("Casos NO BISIESTOS")
print(CalcularAñoBisiesto(1800))
print(CalcularAñoBisiesto(1900))
print(CalcularAñoBisiesto(2100))
print(CalcularAñoBisiesto(2200))
print(CalcularAñoBisiesto(2300))
print(CalcularAñoBisiesto(2500))
print(CalcularAñoBisiesto(2021))
