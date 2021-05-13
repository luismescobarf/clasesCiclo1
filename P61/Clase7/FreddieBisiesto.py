#año = int(input("Introduzca un año:"))

def bisiesto(año):
    a4=año % 4
    a100=año % 100
    a400=año % 400

    ##print (a4,a100,a400)
    if año < 1582:
        print (" No dentro del período del calendario gregoriano")
    elif a4==0:
        print ("residuo %4",año%4)
        print(año, " es Año Bisiesto")
        #Agregar revisiones adicionales
        #Agregar revisiones adicionales
        #Agregar revisiones adicionales
    elif a100==0:
        print ("residuo %100",año%100)
        print(año, " es Año Bisiesto")
    elif a400==0:
        print ("residuo %400",año%400)
        print(año, " es Año Comun")
    else:
        print(año, " es Año Comun")

print("Casos Bisiestos")
print("----------------")
bisiesto(2000)
bisiesto(2400)
bisiesto(2020)
bisiesto(2024)
print("Casos No Bisiestos")
print("----------------")
bisiesto(1800)
bisiesto(1900)
bisiesto(2100)
bisiesto(2200)
bisiesto(2300)
bisiesto(2500)