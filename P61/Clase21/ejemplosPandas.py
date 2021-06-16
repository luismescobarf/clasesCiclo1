#Librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#Función para generar un código de estudiantes
def generarCodigo(numCaracteres):
    alfanumericos = "abcdefghijklmnopqrstuvwxyz1234567890"
    primerCaracter = 'CC'
    listaSeleccion = [ random.choice(alfanumericos) for _ in range(numCaracteres) ]
    listaSeleccion.insert(0,primerCaracter)
    return ''.join(listaSeleccion)

#print('Código generado',generarCodigo(5))

nombres = ["Homero", "Marge", "Bart", "Lisa", "Maggie", "Abraham", "Patty", "Selma"]
apellidos = ["Rodríguez", "Fernández", "Frasser", "Ruiz", "Rassa", "Novoa", "Restrepo", "Castro"]
estado = ['Matriculado','Expulsado','Suspendido','Becado']
carrera = ['Artes','Ingeniería','Medicina','Enfermería','Física','Abogado','Periodista']
condicion = ['condicional','especial']

#Construcción de series (columnas)
serie1 = pd.Series( [33,44,55] )
print(serie1)
print('Valores',serie1.values)
print('Índices',serie1.index)
print('----------------------------')
print('----------------------------')
listaEdades = [33,44,55,np.nan]
listaNombres = ['Ana','Juan','Luis','Pedro']
serie2 = pd.Series( listaEdades, index=listaNombres, name='Edades' )
#serie2.name = 'Edades'
serie2.index.name = 'Personas'
print(serie2)
print('Valores',serie2.values)
print('Índices',serie2.index)
print('---------------------------------------------')
print('---------------------------------------------')

#Construcción de dataframes (varias series varias columnas)
numEstudiantes = 10
colCodigos = pd.Series( [ generarCodigo(5) for _ in range(numEstudiantes) ] )
#print(colCodigos)
colNombres = pd.Series( [ random.choice(nombres) for _ in range(numEstudiantes) ] )
colApellidos = pd.Series( [ random.choice(apellidos) for _ in range(numEstudiantes) ] )
indicesMezclados = list(range(5,15))
# random.shuffle(indicesMezclados)
# print(indicesMezclados)
# colEstado = pd.Series( [ random.choice(estado) for _ in range(numEstudiantes) ], index=indicesMezclados )
# colEstado = pd.Series( [ random.choice(estado) for _ in range(numEstudiantes) ], index=[0,33,44,3] )
colEstado = pd.Series( [ random.choice(estado) for _ in range(numEstudiantes) ] )
colCarrera = pd.Series( [ random.choice(carrera) for _ in range(numEstudiantes) ] )
colCondicion = pd.Series( [ random.choice(condicion) for _ in range(numEstudiantes) ] )
colParcial1 = pd.Series( [ random.randint(0,5) for _ in range(numEstudiantes) ] )
colParcial2 = pd.Series( [ random.randint(0,5) for _ in range(numEstudiantes) ] )
colParcial3 = pd.Series( [ random.randint(0,2) for _ in range(numEstudiantes) ] )

#A partir de un diccionario
diccionarioColIniciales = { 'Codigo':colCodigos, 'Nombre':colNombres, 'Apellidos':colApellidos }
df = pd.DataFrame(diccionarioColIniciales)
df['Estado'] = colEstado
df['Carrera'] = colCarrera
df['Condicion'] = colCondicion
df['Parcial1'] = colParcial1
df['Parcial2'] = colParcial2
df['Parcial3'] = colParcial3
df.index.name = 'Autonumérico'
df.columns.name = 'Persona'
df.title = 'Grupo Estudiantes'
df.set_index('Codigo',inplace=True)
print(df)
print('---------------------------------------------')
print('---------------------------------------------')
#Requerimiento 1 el profesor quiere reajustar el tercer parcial (por exposiciones suma 20% de la nota actual)
df['Parcial3'] = df['Parcial3'] * 1.20
print(df)
print('---------------------------------------------')
print('---------------------------------------------')
#Calcular el promedio de los estudiantes después del reajuste
df['Promedio'] = (df['Parcial1']+df['Parcial2']+df['Parcial3'])/3
print(df)
print('---------------------------------------------')
print('---------------------------------------------')
#Nuevo dataframe con estudiantes que aprobaron
dfAprobados = df[ df['Promedio'] >= 3 ]
print(dfAprobados)
print('---------------------------------------------')
print('---------------------------------------------')
#Nota promedio de los estudiantes agrupados por estado
dfPromedioEstado = df.groupby('Estado')['Promedio'].mean()
dfPromedioEstado.plot(kind='barh')
print(dfPromedioEstado)
print('---------------------------------------------')
print('---------------------------------------------')
#Nota promedio de cada carrera clasificado por estado
dfClasificacionesProm = df.groupby(['Carrera','Estado'])['Promedio'].mean()
print(dfClasificacionesProm)
print('---------------------------------------------')
print('---------------------------------------------')
#Cantidad o proporciones de cada estado de estudiantes
dfProporcionEstados = df.groupby('Estado')[['Estado']].count()
print(dfProporcionEstados)
print('---------------------------------------------')
print('---------------------------------------------')
print(dfProporcionEstados.to_dict())#Tener disponible el resultado de la manipulación del dataframe
#Graficar proporciones de estado (torta)
dfProporcionEstados.plot(kind = 'pie', y='Estado')
plt.grid()
plt.show()










