#Entender el flujo de caracteres de los archivos
flujoCaracteres = """Saludos Tripulantes,
Este es un mensaje desde coordinación, queremos felicitarlos.
Esperamos que continúen así de juiciosos para el Ciclo 2.
Atentamente,
Equipo UTP-MisiónTIC2022
"""
# print('Tipo de la colección de líneas que se obtiene del flujo:')
# print(type(flujoCaracteres.splitlines()))

# #Recorrer el flujo de caracteres y mostrarlo en pantalla
# i = 0
# for linea in flujoCaracteres.splitlines():
#     print('Línea',i+1)
#     print(linea)
#     print()
#     #Mostrar cada palabra de la línea
#     print('Palabras de la línea')
#     for palabra in linea.split(' '):
#         #print(palabra,end='-')
#         print(palabra)
#     i += 1

#Primer manejo de archivos

# #Conexión
# manejadorArchivo = open('estudiantesP61.txt')

# diccionarioEstudiantes = dict()
# for i,linea in enumerate(manejadorArchivo):
#     print('Linea',i+1)
#     print(linea)
#     #Coleccionar
#     listaPalabras = linea.strip().split(' ')
#     diccionarioEstudiantes[listaPalabras[0]] = {    
#                                                     'Nombre':listaPalabras[1],
#                                                     'Ciudad':listaPalabras[2],
#                                                     'Indicador':float(listaPalabras[3]),
#                                                  }

# #Colección cargada desde un archivo
# import pprint as pp
# pp.pprint(diccionarioEstudiantes)

# #Desconexión
# manejadorArchivo.close()

#Módulo o librería para valores por defecto
import parametrosDefault as paramD

#Segunda forma (con validaciones)
diccionarioEstudiantes = dict()

#Intentar hacer la conexión
try:
    #Conexión
    with open('estudiantesP61.txt') as manejadorArchivo:
        
        for i,linea in enumerate(manejadorArchivo):
            print('Linea',i+1)
            print(linea)
            #Coleccionar
            listaPalabras = linea.strip().split(' ')
            diccionarioEstudiantes[listaPalabras[0]] = {    
                                                            'Nombre':listaPalabras[1],
                                                            'Ciudad':listaPalabras[2],
                                                            'Indicador':float(listaPalabras[3]),
                                                        }
except ValueError:
    print('Falló la conversión!!')
except:
    print("Error cargando los estudiantes del archivo!!")
    print('Cargando valores por defecto...')
    diccionarioEstudiantes = paramD.estudiantesDefecto

#Acá ya está desconectado
print('Listo!')

#Colección cargada desde un archivo
import pprint as pp
pp.pprint(diccionarioEstudiantes)

    






    