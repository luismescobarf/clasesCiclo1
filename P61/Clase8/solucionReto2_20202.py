#Objetivo -> Retornar diccionario con el id del préstamo y el campo booleano
#'aprobado' con el valor de verdad correspondiente.

#Algoritmo
#1) Procesar entradas (estandarización) para comparaciones posteriores.
#2) Implementar árbol de decisiones para aprobar o no el préstamo
#3) Retornar el diccionario solicitado.

#Copias (conservar la data original)
id_prestamo =  informacion['id_prestamo']
# casado = False
# if informacion['casado'] == 'Si':
#     casado = True
casado = informacion['casado'] == 'Si'




