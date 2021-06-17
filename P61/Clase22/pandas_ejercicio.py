#ejercicio 012
#crear lista de listas para llenar un data frame de pandas

import pandas as pd

#actores mas taquilleros en estados unidos.
#nombre, apellido, inicio, fin, recaudacion

actores= [
["Harrison", "Ford",	1967, "activo",	9817100],
["Samuel L", "Jackson",	1981, "activo",	8907900],
["Clark", "Gable",	1931, 1961,	8314646],
["John", "Wayne",	1930, 1976,	8253350],
["Tom", "Hanks",	1984, "activo",	7865200],
["James", "Stewart",	1935, 1978,	7312890],
["Bing", "Crosby",	1930, 1966,	7231310],
["Charlton", "Heston",	1950, 2001,	6834491],
["Anthony", "Daniels",	1977, "activo",	6759900],
["Robert", "Downey Jr",	1983, "activo",	6569600],
["Eddy", "Murphy",	1982, "activo",	6535400],
["Gary", "Cooper",	1926, 1961,	6487210],
["Cary", "Grant",	1932, 1966,	6460040],
["Tom", "Cruise",	1981, "activo",	6416600],
["Morgan", "Freeman",	1980, "activo",	6275200],
["Spencer", "Tracy",	1930, 1967,	6070250]
]

columnas = ["nombre", "apellido", "inicio", "fin", "recaudacion"] 
# definimos los nombres de las columnas
filas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] 
# definimos los nombres de las filas

df = pd.DataFrame(actores, columns=columnas, index=filas)

print(df)
