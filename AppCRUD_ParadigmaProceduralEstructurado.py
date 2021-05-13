#Aplicación CRUD - Lista de Tareas Pendientes
#############################################

#Inicialización de tareas (desde el código)
tareas = {
    '01': { 
            'descripcion':'Ir a mercar',
            'estado' : 'pendiente',
            'tiempo' : 60            
           },
    '02': { 
            'descripcion':'Estudiar',
            'estado' : 'pendiente',
            'tiempo' : 180            
           }, 
    '03': { 
            'descripcion':'Hacer ejercicio',
            'estado' : 'pendiente',
            'tiempo' : 50            
           } 
}

#Funcionalidades (Procedimientos o rutinas -> backend)
#-----------------------------------------------------
def create(tareas, identificador, tareaNueva):    
    tareas[identificador] = tareaNueva   
    return tareas

def read(tareas):
    for identificador, tarea in tareas.items():
            print(identificador,' - ',end='')
            for nombre_atributo, atributo in tarea.items():
                print(atributo, ', ', end='')
            print()
            
def estaElemento(identificador, tareas):
    
    #Extraer de la base de datos (contenedor) los identificadores
    conjuntoIdentificadores = set(tareas.keys())
    
    #Revisar si se encuentra el elemento solicitado        
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False
    
def update(tareas,identificador):
	pass
    
    

#Interfaz - Menú (Interfaz - Mainloop)
#--------------------------------------

mainloop = True
while mainloop: 
    print(" ")
    print("-- Aplicación CRUD TareasPendientes ---")
    print("1. Adicionar Tarea")
    print("2. Consultar Tareas")
    print("3. Actualizar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    
    #Create
    if opcion == 1:
        print()
        print("->Adicionando Tarea")        
        
        identificador = str(input("Ingrese identificador de la Tarea: "))
        descripcion = str(input("Ingrese descripción de Tarea: "))
        estado = str(input("Ingrese el estado inicial de la Tarea: "))
        tiempo = int(input("Ingrese el tiempo de realización: "))       
        
        tareaNueva = {
                        'descripcion':descripcion,
                        'estado' : estado,
                        'tiempo' : tiempo       
                    }
        
        #Adicionar la tarea
        tareas = create(tareas, identificador, tareaNueva)        
        
    #Read
    elif opcion == 2:
        print()
        print("->Listado de Tareas")
        print()

        #Lectura de tareas
        read(tareas)               
        
    #Update
    elif opcion == 3:
        print()
        print("->Actualizar Tarea")
        print()
        
        #Solicitar al usuario el identificador
        identificador = str(input("Ingrese identificador de la Tarea para modificar: "))        
        
        #Revisar si se encuentra el elemento solicitado        
        if estaElemento(identificador, tareas):
            
            #Proceder a actualizar
            #---------------------        
            
            #Modificar los campos de interés
            nuevaDescripcion = str(input('Nueva descripción: '))
            if nuevaDescripcion:
                tareas[identificador]['descripcion'] = nuevaDescripcion
            nuevoEstado = str(input('Nuevo estado: '))
            if nuevoEstado:
                tareas[identificador]['estado'] = nuevoEstado
            nuevoTiempo = input('Nuevo tiempo: ')
            if nuevoTiempo:
                nuevoTiempo = int(nuevoTiempo)
                tareas[identificador]['tiempo'] = nuevoTiempo            
            
        else:
            print("No ha sido encontrada la Tarea!")     
           
    #Delete
    elif opcion == 4:
        print()
        print("->Eliminar Tarea")
        print()
        
        #Solicitar al usuario el identificador
        identificador = str(input("Ingrese identificador de la Tarea para eliminar: "))
        
        #Extraer de la base de datos (contenedor) los identificadores
        conjuntoIdentificadores = set(tareas.keys())
        
        #Revisar si se encuentra el elemento solicitado        
        if identificador in conjuntoIdentificadores:
            
            #Proceder a eliminar
            #-------------------           
            tareas.pop(identificador)    
            
        else:
            print("No ha sido encontrada la Tarea para eliminar!")
        
        
    elif opcion == 5:
        print("Ha salido exitosamente.")
        mainloop = False
    else:
        print("Valor inválido!")
        
        
    
    
    
    




