#Objetivo -> Retornar diccionario con el id del préstamo y el campo booleano
#'aprobado' con el valor de verdad correspondiente.

#Algoritmo
#1) Procesar entradas (estandarización) para comparaciones posteriores.
#2) Implementar árbol de decisiones para aprobar o no el préstamo
#3) Retornar el diccionario solicitado.

def prestamo(informacion):

    #Copias (conservar la data original)
    id_prestamo = informacion['id_prestamo']

    #--------------------------------------------------------
    #Estandarización de variables para el árbol de decisiones

    # casado = False
    # if informacion['casado'] == 'Si':
    #     casado = True
    casado = informacion['casado'] == 'Si'

    #Primera forma de estandarizar dependientes
    # dependientes = int()
    # if isinstance( informacion['dependientes'],str ):
    #     #Estandarización de la primera posición de la cadena
    #     dependientes = int(informacion['dependientes'][0])
    # else:
    #     #Realizamos la copia del campo
    #     dependientes = informacion['dependientes']

    #Segunda forma
    # dependientes = int()
    # if isinstance( informacion['dependientes'],int):
    #     dependientes = informacion['dependientes']
    # else:
    #     dependientes = 3

    #Segunda forma (b)
    # if condicion:
    #     (p. verdadera)
    # else:
    #     (p. falsa)
    # (p. verdadera ) if condicion else (p. falsa)
    dependientes = informacion['dependientes'] if isinstance( informacion['dependientes'],int ) else 3

    graduado = informacion['dependientes'] == 'Graduado'

    independiente = informacion['independiente'] == 'Si'

    semiurbana = informacion['tipo_propiedad'] == 'Semi Urbana'

    #----------------------------
    #Copias de los demás campos

    i_d = informacion['ingreso_deudor']
    i_c = informacion['ingreso_codeudor']
    c_p = informacion['cantidad_prestamo']
    p_p = informacion['plazo_prestamo']
    h_c = informacion['historia_credito']

    #Árbol de decisiones del préstamo
    decision = bool()
    if h_c:
        #Cuando el solicitante cuenta con historia crediticia
        if i_c > 0 and i_d / 9 > c_p:
            decision = True#Aprobado
        else:
            #Si no hay suficientes ingresos simultáneos entre cod. deu. se revisa entorno
            if dependientes > 2 and independiente:
                #Respaldar un entorno cargado con el codeudor
                decision =  i_c / 12 > c_p
            else:
                #Revisar tope, entorno favorable
                decision = c_p < 200
    else:
        #No cuenta con historia creditica, proceder a revisar variables (entorno, ingresos, etc)
        if independiente:
            if not(casado and dependientes > 1):
                if i_d / 10 > c_p or i_c / 10 > c_p:
                    #Revisar top, entorno inestable de trabajo
                    decision = c_p < 180
                else:
                    decision = False#Rechazo, ninguno cumple ingresos de respaldo
            else:
                decision = False#Rechazo
        else:
            if not(semiurbana) and dependientes < 2:
                if graduado:
                    decision = i_d / 11 > c_p and i_c / 11 > c_p
                else:
                    decision = False#Rechazo
            else:
                decision = False#Rechazo
    
    #Construir diccionario que relaciona el id del préstamo con la decisión
    diccionarioDecision = {'id_prestamo':id_prestamo,'aprobado':decision}
    
    #Retorno del diccionario como se solicita en el requerimiento
    return diccionarioDecision

#Recordar Ley de DeMorgan para negación de compuertas lógicas
#condición1 Y condición2 (simultaneidad para que sea verdadero)
#negación (condición1 Y condición2) -> negación condición1 O negación condición2 (si sucede uno de ellos es suficiente para que sea cierto)


#Sección principal
#-----------------
import BD_Prestamos as bd

print(prestamo(bd.caso1))
print(prestamo(bd.caso2))
print(prestamo(bd.caso3))