#2021-05-12, 
#misionTIC2022, UTP grupo 61. Hector Alejandro Ruiz, clase 6.

#Recibir tres números enteros diferentes y determinar
#con condicionales cuál es el mayor.

def buscar_mayor(a, b, c):

	if a > b and a > c:
		mayor = a

	elif b > a and b > c:
		mayor = b

	else:
		mayor = c

	return mayor

#print("El mayor es: ",buscar_mayor(31, 29, 44))


"""
informar si un año fue bisiesto.
Nota: el calendario gregoriano entró en vigencia en 1582.
"""
def bisiesto(anho):
	valor = False
	mensaje = ""
	if anho % 4 != 0:
		valor = False
	else:
		if anho % 400 == 0:
			valor = True
		else:
			if anho % 100 == 0:
				valor = False
			else:
				valor = True

	if valor == True:
		mensaje = "{} bisiesto".format(anho)
	else:
		mensaje = "{} no bisiesto".format(anho)


	return mensaje

print("Casos Bisiestos")
print(bisiesto(2000))
print(bisiesto(2400))
print(bisiesto(2020))
print(bisiesto(2024))
print("Casos No Bisiestos")
print(bisiesto(1800))
print(bisiesto(1900))
print(bisiesto(2100))
print(bisiesto(2200))
print(bisiesto(2300))
print(bisiesto(2500))


