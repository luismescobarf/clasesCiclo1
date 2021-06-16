#Importar librerías de soporte
import random
import pprint as pp
import json

#Crear archivos de texto plano
numEstudiantes = 10
nombres = [ 'Carlos','Pedro','Juan','Nathalia','Valentina','MariaCamila']
codigos = ['asjhd7','aksjd8','hh6','898s','uj77f','rtgerg','ref56','jyju8','asda2','5ggh']
estado = ['matriculado','suspendido','becado','egresado','posgrado']

# manejadorArchvo = open('estudiantes.txt','w')

# #Generar un archivo con diez estudiantes generados aleatoriamente
# for i in range(numEstudiantes):
#     infoEstudiante = str()
#     infoEstudiante += codigos[i] + ' '
#     infoEstudiante += random.choice(nombres) + ' '
#     infoEstudiante += random.choice(estado) + '\n'
#     manejadorArchvo.write(infoEstudiante)

# manejadorArchvo.close()

try: 
    with open('estudiantes.txt','w') as manejadorArchvo:
        #Generar un archivo con diez estudiantes generados aleatoriamente
        for i in range(numEstudiantes):
            infoEstudiante = str()
            infoEstudiante += codigos[i] + ' '
            infoEstudiante += random.choice(nombres) + ' '
            infoEstudiante += random.choice(estado) + '\n'
            manejadorArchvo.write(infoEstudiante)
except:
    print('Fallo realizando la escritura')


#Leer archivos de texto plano y cargarlo en diccionario
diccionarioArchivo = dict()
try: 
    with open('estudiantes.txt') as manejadorArchvo:
        for linea in manejadorArchvo:            
            registro = linea.strip().split(' ')
            diccionarioArchivo[ registro[0] ] = { 'Nombre': registro[1], 'Estado': registro[2] }
except:
    print('Fallo realizando la lectura')
print('Contenido del diccionario:')
pp.pprint(diccionarioArchivo)

#Modificar
try:
    with open('estudiantes.txt','a') as manejadorArchivo:
        estudianteNuevo = '234rf John Casado\n'
        manejadorArchivo.write(estudianteNuevo)
except:
    print("Error modificando el archivo de estudiantes!")

#Generar archivo de json a partir de la información del archivo txt
with open('estudiantes.json','w') as manejadorArchivo:
    json.dump(diccionarioArchivo, manejadorArchivo)

#Leer del archivo json
diccionarioJson = dict()
with open('lectura.json') as manejadorArchivo:
    diccionarioJson = json.load(manejadorArchivo)
print()
print("Diccionario de JSON")
pp.pprint(diccionarioJson)


