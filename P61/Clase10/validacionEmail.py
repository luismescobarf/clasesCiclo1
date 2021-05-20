#Requerimiento: El usuario ingresa un correo electrónico
#se necesita una primera función (esto es solamente una
#etapa de la validación) que revise que el número de arrobas
#sea válildo (estrictamente igual a 1). Y si es válido en
#términos de arrobas revisar que los caracteres previos sean
#alfanuméricos (válidos) -> José Luis Rassa
#->Tarea: Requerimiento adicional -> mostrar en pantalla las posiciones
#donde se encuentran los caracteres inválidos

#Objetivo -> reportar si es válido o no el número de arrobas
#del correo

#Algoritmo
#1) Capturar el correo electrónico que solicita el usuario
#2) Recorrer los caracteres del correo capturado
#2a) Si el caracter es igual a arroba, acumular en el contador
#de arrobas
#3) Revisar el contador de arrobas, si es igual a 1 reportar validez
#3a) Si es diferente de uno reportar invalidez del correo

#Traducción
email = input('Ingrese un correo electrónico: ')
cont = 0
for caracter in email:
    if caracter == '@':
        cont += 1
if cont == 1:
    #Variación del requerimiento
    #->Intensificar validación:revisar el nombre del corre (previo al domino)
    
    #nombreCorreo = email.split('@')[0].lower()
    parcicionCorreo = email.split('@')#Generar lista de dos cadenas
    nombreCorreo = parcicionCorreo[0]#Tomar la primera cadena de la lista
    nombreCorreo = nombreCorreo.lower()#Pasar la cadena a minúsculas

    cadenaCaracteresInvalidos = 'ñ\\ áéíóú*,#$%='
    conteoInvalidos = 0
    for caracter in cadenaCaracteresInvalidos:
        if caracter in nombreCorreo:
            conteoInvalidos += 1
    if conteoInvalidos:
        print(f"{email} es un correo inválido! El nombre contiene caracteres especiales.")
    else:
        print(f"{email} es un correo válido")
else:
    print(f"{email} es un correo inválido!")