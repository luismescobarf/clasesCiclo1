#Se requiere una función que reciba 3 números
#que son diferentes, y determine cuál es el mayor de ellos.
#Observación -> Los números no están ordenados

#Objetivo -> Reportar el mayor número

#Representación -> Diagrama de flujo

#Traducción -> Python
print("Ingrese 3 números diferentes")
a = int(input())
b = int(input())
c = int(input())
if a>b:
    if a>c:
        print(a,"es el mayor número")
    else:
        print(c,"es el mayor número")
else:
    if b>c:
        print(b,"es el mayor número")
    else:
        print(c,"es el mayor número")


