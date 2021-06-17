import json

#->Tomar un diccionario y guardarlo en un archivo csv

#Módulo o librería para valores por defecto
import parametrosDefault as paramD

#Segunda forma (con validaciones)
diccionarioEstudiantes = paramD.estudiantesDefecto

#Intentar hacer la conexión
try:
    #Conexión
    with open('estudiantesP61.csv','w') as manejadorArchivo:

        #Carrito escribiendo en el archivo el encabezado
        encabezado = 'Codigo,'
        encabezado += 'Nombre,'
        encabezado += 'Ciudad,'
        encabezado += 'Indicador' + '\n'
        manejadorArchivo.write(encabezado)        
        for codigo,info in diccionarioEstudiantes.items():            
            fila = codigo +',' 
            fila += info['Nombre'] + ','
            fila += info['Ciudad'] + ','
            fila += str(info['Indicador']) + '\n'
            manejadorArchivo.write(fila)                    
except:
    print("Error de escritura!!")

#Cargar el diccionario proveniente del json
diccionarioDesdeJSON = dict()
try:
    with open('estudiantesP61.json') as manejadorArchivo:
        diccionarioDesdeJSON = json.load(manejadorArchivo)
        print('Carga de JSON exitosa')
except:
    print('Error Cargando JSON!!!')

print('Proveniente de archivo JSON')
print(diccionarioDesdeJSON)

#Tomar el diccionario de estudiantes y guardarlo en un json
try:
    with open('estudiantesP61.json','w') as manejadorArchivo:
        json.dump(diccionarioEstudiantes,manejadorArchivo)
        print('Creación de JSON exitosa')
except:
    print('Error de la escritura del archivo JSON')


    