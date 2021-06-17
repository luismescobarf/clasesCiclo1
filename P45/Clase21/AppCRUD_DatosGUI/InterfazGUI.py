#Librerías de la interfaz gráfica
import tkinter as tk
import InterfazConsola as ic

#Lógica para hacer consultas
import CRUD

#Construir ventana principal de la aplicación
def ventanaMenuPrincipal(tareas):

    #Creamos nuestra ventana principal (instanciar un objeto tipo aplicación Tk)
    m = tk.Tk()
    m.title("App CRUD Listado de Tareas")   
    #m.geometry("800x600")

    #Construyendo o componiendo nuestra interfaz
    btnListartareas = tk.Button(m,text='Listar Tareas',command = lambda : ic.mostrarTareas(tareas) )
    #Pack, Place, Grid (Chévere) -> Advertencia sólo se puede usar una!
    btnListartareas.pack()

    #Campo id
    etId = tk.Label(m,text='Id:')
    etId.pack()
    entradaId = tk.Entry(m)
    entradaId.pack()

    etDescripcion = tk.Label(m,text='Descripcion:')
    etDescripcion.pack()
    entradaDescripcion = tk.Entry(m)
    entradaDescripcion.pack()

    etEstado = tk.Label(m,text='Estado:')
    etEstado.pack()
    entradaEstado = tk.Entry(m)
    entradaEstado.pack()

    etTiempo = tk.Label(m,text='Tiempo:')
    etTiempo.pack()
    entradaTiempo = tk.Entry(m)
    entradaTiempo.pack()

    #Función que recoge la información de los campos del formulario
    def adicionarTareaGUI():

        id = entradaId.get()
        tarea = {
                'descripcion':entradaDescripcion.get(),
                'estado':entradaEstado.get(),
                'tiempo':int(entradaTiempo.get())
            }
        
        #Capa Lógica
        CRUD.Create(id,tarea,tareas)

    #Botón que realiza la acción Create
    btnAdicionarTarea = tk.Button(m,text='Adicionar Tarea',command = adicionarTareaGUI )
    #Pack, Place, Grid (Chévere) -> Advertencia sólo se puede usar una!
    btnAdicionarTarea.pack()

    #Función que guarda cambios en la capa de datos
    def salirGuardar():

        #Capa lógica
        if not(CRUD.Write(tareas)):#Si no hay error
            #Interacción (ayudados por consola)
            ic.mensaje('Cerrado y guardado con éxito!')
        else:
            #Interacción (ayudados por consola)
            ic.mensaje('Error guardando!!')

        #Interacción GUI
        m.destroy()

    #Botón que realiza la acción Create
    btnSalirGuardar = tk.Button(m,text='Salir y Guardar',command = salirGuardar )
    #Pack, Place, Grid (Chévere) -> Advertencia sólo se puede usar una!
    btnSalirGuardar.pack()             


    #Retornar la ventana construída
    return m