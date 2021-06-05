#Requerimiento -> Determinar si un correo tiene le número de arrobas adecuado (1)
#Obtener el usuario y el dominio si es válido.
#Solicitar varios correos y almacenar en una lista de diccionarios aquellos que son válidos

#Solicitar correo al usuario
correo = input('Ingresar correo: ')
numArrobas = 0
# for caracter in correo:
#     if caracter == '@':
#         numArrobas += 1    
for i in range(len(correo)):
    if correo[i] == '@':
        numArrobas += 1
elementosCorreo = list()
diccionarioCorreo = dict()
if numArrobas == 1:
    print('Correo válido')
    elementosCorreo = correo.split('@')
    #Alternativa de actualización de diccionario
    # diccionarioCorreo['Nombre Usuario'] = elementosCorreo[0]
    # diccionarioCorreo['Dominio'] = elementosCorreo[1]       
    diccionarioCorreo =  {'Nombre Usuario':elementosCorreo[0],'Dominio':elementosCorreo[1]}
else:
    print('Correo inválido')

#Guardad la información en un diccionario mostrarla en pantalla
print('Accediendo a cada posición:')
print("Nombre de usuario: ", diccionarioCorreo['Nombre Usuario'])
print("Dominio: ",diccionarioCorreo['Dominio'])