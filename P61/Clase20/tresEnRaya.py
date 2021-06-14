#Requerimiento General -> Simular dos robots jugando tres en raya.

#Requerimientos Específicos  -> Sistema controlando el tablero y alternando turnos a los robots
#                            -> Robot O -> 1 (Hace su movimiento sobre una casilla vacía)
#                            -> Robot X -> 10 (Hace su movimiento sobre una casilla vacía)
#                            -> Tablero -> Posición vacía: rep lógica -> 0 rep consola -> _

#Librerías de soporte
import numpy as np
import random

#Funciones de lógica

def formatoVacias(casillasVacias):
    filas = list(casillasVacias[0])
    columnas = list(casillasVacias[1])
    listaCV = list(zip(filas,columnas))
    return listaCV

#Agente o robot JugadorO
def jugadorO(tablero):
    #Identificar las vacías
    casillasVacias = np.where(tablero==0)
    listaCV = formatoVacias(casillasVacias)
    # #Salida de diagnóstico  
    # print(casillasVacias)
    # print(listaCV)
    #Seleccionar una casilla vacía para colocar su movimiento
    movimiento = random.choice(listaCV)
    #Aplicar el movimiento (mundo lógico)
    tablero[movimiento] = 1

#Agente o robot JugadorX
def jugadorX(tablero):
    #Identificar las vacías
    casillasVacias = np.where(tablero==0)
    listaCV = formatoVacias(casillasVacias)
    # #Salida de diagnóstico  
    # print(casillasVacias)
    # print(listaCV)
    #Seleccionar una casilla vacía para colocar su movimiento
    movimiento = random.choice(listaCV)
    #Aplicar el movimiento (mundo lógico)
    tablero[movimiento] = 10

#Estado del tablero
def estadoTablero(tablero):

    #Determinar si gana O
    ganoColumna = 3 in np.sum(tablero, axis=0)
    ganoFila = 3 in np.sum(tablero, axis=1)
    ganoDiagonal = 3 == np.sum(tablero.diagonal())
    ganoDiagonalContraria = 3 == np.sum( np.fliplr(tablero).diagonal() )
    if  any( [ganoColumna,ganoFila,ganoDiagonal,ganoDiagonalContraria] ) :
        return 1

    #Determinar si gana X
    ganoColumna = 30 in np.sum(tablero, axis=0)
    ganoFila = 30 in np.sum(tablero, axis=1)
    ganoDiagonal = 30 == np.sum(tablero.diagonal())
    ganoDiagonalContraria = 30 == np.sum( np.fliplr(tablero).diagonal() )
    if  any( [ganoColumna,ganoFila,ganoDiagonal,ganoDiagonalContraria] ) :
        return 10

    #Determinar si hay un empate
    empateIniciandoO = np.sum(tablero) == 45
    empateIniciandoX = np.sum(tablero) == 54
    if any( [empateIniciandoO,empateIniciandoX] ):
        return 0

    #Si no tomó ninguno de los caminos
    return -1 #Siga jugando   

#Funciones de interacción

#Mostrar en pantalla el tablero tres en raya
def mostrarTablero(tablero):
    for fila in tablero:
        for columna in fila:
            if columna == 1:
                print(' O ',end='')
            elif columna == 10:
                print(' X ',end='')
            elif columna == 0:
                print(' _ ',end='')
        print() 
    print()      

#Sección principal -> Sistema controlando el tablero y alternando turnos
#-----------------------------------------------------------------------
#Codificación del tablero
tablero = np.zeros((3,3))

# #Salidas de diagnóstico
# print('Versión lógica del tablero:',tablero)
# print('Versión para el usuario')
# mostrarTablero(tablero)

print('Inicio del juego')
mostrarTablero(tablero)

# #Forzar un movimiento (esquina superior izquierda jugador X)
# tablero[0,0] = 10
# tablero[1,1] = 10
# tablero[2,2] = 10
# print('Mostrar movimiento forzado')
# mostrarTablero(tablero)

# #Probando Robots o Agentes E-R JugadorO, JugadorX
# jugadorO(tablero)
# jugadorX(tablero)
# jugadorO(tablero)
# jugadorX(tablero)
# print('Mostrar movimientos reallizados por Jugadores')
# mostrarTablero(tablero)

#Seleccionar lógicamente el jugador
jugadorSeleccionado = 1 if random.randint(0,1) else 10

#Llamar el jugador correspondiente
if jugadorSeleccionado == 1:
    jugadorO(tablero)
    jugadorSeleccionado = 10
else:
    jugadorX(tablero)
    jugadorSeleccionado = 1

print('Mostrar jugador iniciando')
mostrarTablero(tablero)

#Simulación después del primer movimiento
while True:

    #Revisar estado del juego
    estado = estadoTablero(tablero)

    #Revisar cada caso
    if estado == 1:
        print('Ganó el Jugador O')
        break
    elif estado == 10:
        print('Ganó el Jugador X')
        break
    elif estado == 0:
        print('Empate!')
        break

    #Sistema revisa si hay casillas vacías para controlar continuación del juego
    casillasVacias = np.where(tablero==0)
    if len(casillasVacias[0]) == 0:
        break

    #Llamar el jugador que tiene el turno
    if jugadorSeleccionado == 1:
        jugadorO(tablero)
        jugadorSeleccionado = 10
    else:
        jugadorX(tablero)
        jugadorSeleccionado = 1

    #Mostrar tablero después de la jugada
    mostrarTablero(tablero)
    input()

    





