import numpy as np

#np.sum(matrizAleatoria, axis=1)

def displayInicialTriqui():
    for i in range(0,3):
        for j in range(0,3):
            print("|_",end="")
        print("|")

def displayTriqui(matriz):
    for i in range(0,3):
        for j in range(0,3):
            if matriz[i,j]==1:
                print("|X", end="")
            else:
                if matriz[i,j]==10:
                    print("|O",end="")
                else:
                    print("|_",end="")
        print("|")
        
def estadoDelJuego(matriz)->int:
    #devuelve 1 si gana la X
    if 3 in np.sum(matriz, axis=0) or 3 in np.sum(matriz, axis=1) or np.sum(np.diagonal(matriz))==3 or np.sum(np.diagonal(np.fliplr(matriz)))==3:
        salida = 1
    else:
        #devuelve 2 si gana la Y
        if 30 in np.sum(matriz, axis=0) or 30 in np.sum(matriz, axis=1) or np.sum(np.diagonal(matriz))==30 or np.sum(np.diagonal(np.fliplr(matriz)))==30:
            salida = 2
        else:
            #devuelve 3 si no hay ganador
            if np.sum(matriz)==45 or np.sum(matriz)==54:
                salida = 3
            else:
                #devuelve 4 si aun hay juego
                salida = 4
    return salida

def jugarTriqui():
    #seleccionar aleatoriamente un jugador
    turno=False
    if np.random.rand()<0.5:
        turno=True
    #inicializar las variables del juego
    displayInicialTriqui()
    matriz = np.zeros((3,3))   # Crear una matriz de todos los ceros
    estado=4
    while(estado==4):
        #atrapar el movimiento de los jugadores
        tupla= tuple(input("Ingrese la casilla a jugar, ej: la casilla superior derecha es 1,3: "))
        #convertir la notacion de los jugadores a los indices de la matriz
        x=int(tupla[0])-1
        y=int(tupla[2])-1
        #validar movimiento dentro del tablero
        if x>=0 and x<= 2 and y>=0 and y<=2:
            #validar movimiento no antes hecho
            if matriz[x,y]==0:
                if turno:
                    matriz[x,y]=1
                else:
                    matriz[x,y]=10
                #llamar la funcion del estado del juego
                estado = estadoDelJuego(matriz)
                #llamar el visualizador
                displayTriqui(matriz)
                #cambiar de turno
                turno=not(turno)
            else:
                print("Recuerde jugar en casillas vacias!")
        else:
            print("Recuerda que el tablero es de 3 por 3!  ej: la casilla inferior izquierda es 3,1")
    # Publicar el resultado del juego
    if estado == 1 :
        print("El jugador X ha ganado!")
    else:
        if estado == 2 :
            print("El jugador O ha ganado!")
        else:
            print("No hubo ganadores!")


jugarTriqui()