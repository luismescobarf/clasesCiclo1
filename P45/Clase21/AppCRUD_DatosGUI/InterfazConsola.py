#Lógica para hacer consultas
import CRUD

#Interacción
def menuPrincipal():
    print("Elija una opción")
    print("1. Adicionar Tarea")
    print("2. Mostrar Tareas")
    print("3. Salir")
    opcion = int(input('Ingresar opción'))
    return opcion

def formularioCrearTarea():
    id =  input('Ingresar id:')
    descripcion =  input('Ingresar descripcion:')
    estado =  input('Ingresar estado:')
    tiempo =  int(input('Ingresar tiempo:'))
    tarea = {
                'descripcion':descripcion,
                'estado':estado,
                'tiempo':tiempo
            }
    return id,tarea

def mostrarTareas(tareas):    
    print('Listado de tareas')
    for id,tarea in tareas.items():            
        print(f"{id} - {tarea['descripcion']}, {tarea['estado']}, {tarea['tiempo']} ")

def mensaje(info):
    print()
    print(info)
    print()
    