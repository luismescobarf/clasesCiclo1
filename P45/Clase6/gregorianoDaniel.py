""" Objetivo => Calcular si un año es biciesto o no, retornar el año y un mensaje si es o no bisiesto """

def CalcularAñoBisiesto(Año):
    AñoBisiesto = False

    if Año % 4 == 0:
        if Año % 100 == 0:
            if Año % 400 == 0:
                AñoBisiesto = True

    if AñoBisiesto == True:
        return f"\n El año {Año} es bisiesto"
    else:
        return f"\n El año {Año} no es bisiesto"

Año = int(input("Ingrese el año: "))

print(CalcularAñoBisiesto(Año))