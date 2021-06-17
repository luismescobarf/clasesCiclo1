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

    #Construyendo o componiendo nuestra interfaz
    btnListartareas = tk.Button(m,text='Listar Tareas',command = lambda : ic.mostrarTareas(tareas) )
    #Pack, Place, Grid (Chévere) -> Advertencia sólo se puede usar una!
    btnListartareas.pack()

    #Retornar la ventana construída
    return m