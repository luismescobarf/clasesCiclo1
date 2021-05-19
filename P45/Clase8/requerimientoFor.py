#Requerimiento: escribir una función que valide que un correo electrónico
#ingresado, solamente tenga una arroba, mostrar en pantalla la posición de las
#arrobas que estén sobrando


#Objetivo -> Número válido de arrobas den un correo (única arroba)

# #Algoritmo (Pseudocódigo)
# 1) Ingresa el correo electrónico
# 2) Inicializamos contador de arrobas
# 3) Recorremos todos los caracteres que constituyen el correo
# 3a) Si encontramos una arroba incrementamos el contador de arrobas
# 4) Revisar el número de arrobas y reportar si el correo es válido en este contexto.

#Traducción -> Python
email = input('Ingresar correo electrónico: ')
contadorArrobas = 0
# if email[0] == '@':
#     contadorArrobas += 1
# if email[1] == '@':
#     contadorArrobas += 1    
# if email[2] == '@':
#     contadorArrobas += 1
# .  
# .
# .

#Forma utilizando subíndice
# for i in range(len(email)):
#     if email[i] == '@':
#         contadorArrobas += 1
#         if contadorArrobas > 1:
#             print("Hay una arroba sobrante en la posición,",i)

# #Forma cargando en una variable cada elemento
# contadorPosicion = 0
# for caracter in email:
#     if caracter == '@':
#         contadorArrobas += 1
#         if contadorArrobas > 1:
#             print("Hay una arroba sobrante en la posición,",contadorPosicion)
#     contadorPosicion += 1

#Forma combinando las anteriores
for i,caracter in enumerate(email):
    if caracter == '@':
        contadorArrobas += 1
        if contadorArrobas > 1:
            print("Hay una arroba sobrante en la posición,",i)    

if contadorArrobas == 1:
    print("El correo tiene el número correcto de arrobas")
elif contadorArrobas == 0:
    print("El correo no tiene diferenciado el dominio: 0 arrobas encontradas")
elif contadorArrobas > 0:
    print(f"El correo tiene {contadorArrobas-1} de sobra")