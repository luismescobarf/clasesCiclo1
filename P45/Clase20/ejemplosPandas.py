#Librerías
import numpy as np
import pandas as pd
import random

#Series -> Columnas
#Dataframes -> Hoja de Cálculo

#Construir series
serie = pd.Series([33,44,55],index=['Fila1','Fila2','Fila3'])
print(serie)
print('Valores de la serie (columna)')
print(serie.values)
print('Tipo de colección de los valores:',type(serie.values))
print('Índices de la serie (columna)')
print(serie.index)

#Partiendo de un diccionario
diccionario = {'Carlos':5.0,'Pedro':4.8,'Juan':5.0}
serieDiccionario = pd.Series(diccionario)
print('Serie a partir de diccionario')
print(serieDiccionario)
print('Indice',serieDiccionario.index)
print('Valores',serieDiccionario.values)

#Dataframe -> varias series
numEstudiantes = 10
nombres = [ 'Carlos','Pedro','Juan','Nathalia','Valentina','MariaCamila']
codigos = ['asjhd7','aksjd8','hh6','898s','uj77f','rtgerg','ref56','jyju8','asda2','5ggh']
estado = ['matriculado','suspendido','becado']
serie1 = pd.Series( [ random.choice(nombres) for _ in range(numEstudiantes) ] )
serie2 = pd.Series( [ random.randint(100,200) for _ in range(numEstudiantes) ] )
serie3 = pd.Series( [ random.choice(estado) for _ in range(numEstudiantes) ], index=['Hola',1,2,3,55,4,5,7,9,10] )
print(serie1)
print(serie2)
print(serie3)
diccionarioSeries = { 'Nombres':serie1, 'Puntaje1':serie2 }
df = pd.DataFrame(diccionarioSeries)
df['Estado'] = serie3
df['Codigo'] = pd.Series(codigos)
print('Nombres columnas')
print(df.columns)
df.columns.name = "Estudiantes"
df.index.name = "Autonumérico"
#df_original = df.copy()
# print('Original')
# print(df_original)
df.set_index('Codigo',inplace=True)
serie4 = pd.Series( [ random.randint(100,200) for _ in range(numEstudiantes) ], index = codigos )
df['Puntaje2'] = serie4
serie5 = pd.Series( [ random.randint(50,120) for _ in range(numEstudiantes) ], index = codigos )
df['Puntaje3'] = serie5
print(df)
print()




