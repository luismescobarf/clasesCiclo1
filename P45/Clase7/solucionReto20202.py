#Objetivo -> Determinar si se aprueba o se rechaza un crédito, retornando la resupuesta
#en un diccionario con una estructura específica.

#Algoritmo:
# 1) Estandarización de las variables
# 2) Reflejar árbol de decisiones de la entidad bancaria
# 3) Retornar el dictamen del árbol de decisiones

#Función para estandarizar si es alfanumérico el campo a numérico
def estandarizarAlfanumerico(valorAlfanumerico):
    #Revisión de tipos y parseo
    valorNumerico = float()
    if isinstance(valorAlfanumerico,str):
        valorNumerico = float(valorAlfanumerico[0])
    else:
        valorNumerico = valorAlfanumerico
    #Retorno
    return valorNumerico

#Estandarización
id_prestamo = informacion['id_prestamo']

#--------------------------
#Casado

# #Primera forma
# casado = bool()
# if informacion['casado'] == 'Si':
#     casado = True
# else:
#     casado = False

# #Segunda forma
# casado = False
# if informacion['casado'] == 'Si':
#     casado = True

#Tercera forma
casado = informacion['casado'] == 'Si'

#--------------------------
#Dependientes

#Primera forma
#dependientes = estandarizarAlfanumerico(informacion['dependientes'])

#Segunda forma
dependientes = informacion['dependientes'] if isinstance(informacion['dependientes'],int) else 3

#--------------------------
#Graduado

graduado = informacion['educacion'] == 'Graduado'


#--------------------------
#Independiente

independiente = informacion['independiente'] == 'Si'

#--------------------------
#Semiurbana

semiurbana = informacion['tipo_propiedad'] == 'Semi Urbana'

#Copias de los campos del diccionario

#Arbol de decisiones







