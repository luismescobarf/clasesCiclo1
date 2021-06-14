#Requerimiento General -> Simular dos robots jugando tres en raya.

#Requerimientos Específicos  -> Sistema controlando el tablero y alternando turnos a los robots
#                            -> Robot O -> 1 (Hace su movimiento sobre una casilla vacía)
#                            -> Robot X -> 10 (Hace su movimiento sobre una casilla vacía)
#                            -> Tablero -> Posición vacía: rep lógica -> 0 rep consola -> _

#Librerías de soporte
import numpy as np
import random

#Funciones de lógica


def jugadorO(tablero):
    casillasVacias = np.where(tablero==0)
    print(casillasVacias)

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

#Forzar un movimiento (esquina superior izquierda jugador X)
tablero[0,0] = 10
print('Mostrar movimiento forzado')
mostrarTablero(tablero)

