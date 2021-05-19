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

def prestamo(informacion):

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
    h_c = informacion['historia_credito']

    #Suponemos que es falso hasta que se demuestre lo contrario en el árbol de decisiones
    decision = False

    #Arbol de decisiones
    if h_c:
        #Cuando el cliente tiene historial crediticio
        if i_c > 0 and i_d/9 > c_p:
            #Cumple ingresos del codeudor ingresos del solicitante
            decision = True
        else:
            if dependientes > 2 and independiente:
                decision = i_c / 12 > c_p
            else:
                decision = c_p < 200
    else:
        #Cuando el cliente no tiene historial crediticio
        if independiente:
            #Cuando es trabajador independiente
            if not(casado and dependientes > 1):
                if i_d / 10 > c_p or i_c / 10 > c_p:
                    decision = c_p < 180
                else:
                    decision = False
            else:
                decision = False
        else:
            #Cuando es trabajador dependiente
            if not(semiurbana) and dependientes < 2:
                if graduado:
                    decision = i_d / 11 > c_p and i_c / 11 > c_p
                else:
                    decision = False
            else:
                decision = False

    #Diccionario con la decisión del préstamo
    diccionarioDecision = {
                            'id_prestamo':id_prestamo,
                            'aprobado': decision
                            }

    return diccionarioDecision

#Sección principal -> Pruebas
#############################

#Casos de prueba
diccionario1=dict(id_prestamo='RETOS2_001',
    casado='No',
    dependientes=1,
    educacion='Graduado',
    independiente='Si',
    ingreso_deudor=4692,
    ingreso_codeudor=0,
    cantidad_prestamo=106,
    plazo_prestamo=360,
    historia_credito=1,
    tipo_propiedad='Rural')

diccionario2=dict(id_prestamo='RETOS2_002',
    casado='No',
    dependientes='3+',
    educacion='No Graduado',
    independiente='No',
    ingreso_deudor=1830,
    ingreso_codeudor=0,
    cantidad_prestamo=100,
    plazo_prestamo=360,
    historia_credito=0,
    tipo_propiedad='Urbano')

diccionario3=dict(id_prestamo='RETOS2_003',
    casado='No',
    dependientes='0',
    educacion='No Graduado',
    independiente='No',
    ingreso_deudor=3748,
    ingreso_codeudor=1668,
    cantidad_prestamo=110,
    plazo_prestamo=360,
    historia_credito=1,
    tipo_propiedad='Semiurbano')

#Correr las pruebas
print(prestamo(diccionario1))
print(prestamo(diccionario2))
print(prestamo(diccionario3))














