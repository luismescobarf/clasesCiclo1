#Librerías
import json

#Capa lógica

#Create -> Adicionar tarea
def Create(id,tarea,tareas):
    tareas[id] = tarea

#Read
def Read():
    
    # #Inicialización de los datos, lectura (sin capa de datos)
    # tareas = { '00':{
    #                     'descripcion':'Mercar',
    #                     'estado':'Pendiente',
    #                     'tiempo':30
    #                 },
    #             '01':{
    #                 'descripcion':'Estudiar TKINTER',
    #                 'estado':'En proceso',
    #                 'tiempo':190
    #             },
    #             '02':{
    #                 'descripcion':'Entrenar',
    #                 'estado':'Cancelado',
    #                 'tiempo':45
    #             }
    # }

    #Obtener el diccionario de tareas del archivo/base de datos
    tareas = dict()

    try:        
        with open('tareas.json') as manejadorArchivo:
            tareas = json.load(manejadorArchivo)
    except:
        print('Error de carga de tareas!!!')

    return tareas

#Escritura en la base de datos (archivo json)
def Write(tareas):
    try:        
        with open('tareas.json','w') as manejadorArchivo:
            json.dump(tareas,manejadorArchivo)
        
        return 0#Escritura exitosa

    except:
        return 1 #Error de escritura
