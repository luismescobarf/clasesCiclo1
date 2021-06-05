parrafo = """
Esta es una prueba
de contenido probando probando
hola
otro otro otro otro
de contenido probando probando"""

for linea in parrafo.split('\n'):
    print(linea)

coordenadas = """A 8 8
B 5 7
C 10 10"""

listadoCoordenadas = []
for coordenada in coordenadas.split('\n'):
    print(coordenada,type(coordenada))
    componentes = coordenada.split(' ')
    listadoCoordenadas.append([str(componentes[0]), int(componentes[1]), int(componentes[2])])

print("Resultado procesamiento de las coordenadas: ")
print(listadoCoordenadas)

    


