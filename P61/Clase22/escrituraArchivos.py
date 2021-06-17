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


    