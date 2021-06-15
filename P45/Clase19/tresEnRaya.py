#Requerimiento general -> simulación de dos robots jugando tres en raya
#Requerimientos específicos -> Jugador O
#                           -> Jugador X
#                           -> Sistema que controla el tablero que modifican los jugadores (bots)

#Librerías de soporte
import numpy as np
import random

#Codificación
#Tablero -> matriz de numpy
#Jugador O -> 1
#Jugador X -> 10
#Posición libre del tablero -> 0
#Interfaz -> mostrar el tablero con X, O, _

#Interacción

def mostrarTablero(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == 1:
                print(" O ",end='')
            elif casilla == 10:
                print(" X ",end='')
            elif casilla == 0:
                print(" _ ",end='')
        print()#Separar las filas del tablero
    print()#Separar el tablero en pantalla            

#Lógica

def formatoCV(casillasVacias):
    listaFilas = list(casillasVacias[0])
    listaColumnas = list(casillasVacias[1])
    listaCV = list(zip(listaFilas,listaColumnas))
    return listaCV

def jugadorX(tablero):
    casillasVacias = np.where(tablero==0)
    listaCV = formatoCV(casillasVacias)
    casillaElegida = random.choice(listaCV)
    tablero[casillaElegida] = 10

def jugadorO(tablero):
    casillasVacias = np.where(tablero==0)
    listaCV = formatoCV(casillasVacias)
    casillaElegida = random.choice(listaCV)
    tablero[casillaElegida] = 1

def estadoTablero(tablero):

    #Gana el jugador O
    ganaFila = 3 in np.sum(tablero, axis = 1)
    ganaColumna = 3 in np.sum(tablero, axis = 0)
    ganaDiagonal = 3 == np.sum(tablero.diagonal())
    ganaDiagonalContraria = np.sum(np.fliplr(tablero).diagonal())
    if any( [ganaFila,ganaColumna,ganaDiagonal,ganaDiagonalContraria] ):
        return 1

    #Gana el jugador X
    ganaFila = 30 in np.sum(tablero, axis = 1)
    ganaColumna = 30 in np.sum(tablero, axis = 0)
    ganaDiagonal = 30 == np.sum(tablero.diagonal())
    ganaDiagonalContraria = np.sum(np.fliplr(tablero).diagonal())
    if any( [ganaFila,ganaColumna,ganaDiagonal,ganaDiagonalContraria] ):
        return 10

    #Empate
    empateIniciandoO = np.sum(tablero) == 45
    empateIniciandoX = np.sum(tablero) == 54
    if any([empateIniciandoO,empateIniciandoX]):
        return 0

    #No se cumple ninguna
    return -1


#Sección principal (sistema)
#---------------------------

#Inicializar el juego (tablero)
tablero = np.zeros((3,3))
mostrarTablero(tablero)

# #Forzar modificaciones para calibrar nuestros jugadores
# print('Modificaciones sobre el tablero')
# tablero[0,0] = 1
# tablero[1,1] = 1
# tablero[2,2] = 10
# tablero[0,2] = 10
# tablero[2,0] = 10
# mostrarTablero(tablero)

# #Jugadores percibiendo y afectando el tablero
# jugadorX(tablero)
# mostrarTablero(tablero)
# jugadorO(tablero)
# mostrarTablero(tablero)
# jugadorX(tablero)
# mostrarTablero(tablero)
# jugadorO(tablero)
# mostrarTablero(tablero)

#Sistema va a elegir el jugador que inicia
jugadorElegido = 1 if random.randint(0,1) else 10

#Sistema le da el turno al jugador seleccionado
if jugadorElegido == 1:
    jugadorO(tablero)
    jugadorElegido = 10
else:
    jugadorX(tablero)
    jugadorElegido = 1

mostrarTablero(tablero)

#Simulación
while True:

    #Revisar si el tablero aún tiene posiciones
    casillasVacias = np.where(tablero==0)
    if len(casillasVacias[0]) == 0:
        break

    #Sistema le da el turno al jugador seleccionado
    if jugadorElegido == 1:
        jugadorO(tablero)
        jugadorElegido = 10
    else:
        jugadorX(tablero)
        jugadorElegido = 1

    #Evolución del tablero con la intervención de los jugadores bots
    mostrarTablero(tablero)

    #Pausa en la salida
    input()



