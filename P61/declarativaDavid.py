def mEM(matriz,a):    
    return map(lambda x:map(lambda ij:a*ij,x),matriz)

def sumaFilas(x):    
    #Cada componente es un iterable
    return map(lambda y,z:y+z,x[0],x[1])

def sumaMatrices(matrizA,matrizB):
    contenedorMap = map(sumaFilas,zip(matrizA,matrizB))
    #Definir el tipo de colección de los iterables resultantes
    return list( map(lambda x:list(x), contenedorMap ) )   

#Matrices Ejemplo
matriz1=[[2,1,3],[1,-3,5]]
matriz2=[[0,2,-2],[1,2,5]]