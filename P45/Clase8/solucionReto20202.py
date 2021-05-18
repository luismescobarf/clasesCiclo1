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

# #Segunda forma (a)
# dependientes = int()
# if isinstance(informacion['dependientes'],int):
#     dependientes = informacion['dependientes']
# else:
#     dependientes = 3

# #Condicional en una sola línea Python (bonus)
# if condicion:
#     (h.v. -> retorno)
# else:
#     (h.f. -> retorno)
# (h.v.) if condicion else (h.f.)

#Segunda forma (b)
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

#Copias de los campos del diccionario que no necesitaban estandarización
i_d = informacion['ingreso_deudor']
i_c = informacion['ingreso_codeudor']
c_p = informacion['cantidad_prestamo']
p_p = informacion['plazo_prestamo']


#Arbol de decisiones







