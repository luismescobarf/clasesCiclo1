#Solución reto 5
def analisisTRM(rutaArchivo):

    #Para subir a plataforma
    import pandas as pd

    #Revisar extensión
    if rutaArchivo[-3:].lower() != 'csv':
        return "Extensión inválida"

    #Si pasa la revisión de la extensión, procedemos a la carga (controlada)
    try:
        df = pd.read_csv(rutaArchivo, sep=',')
    except:
        return "Error al leer el archivo de datos"

    # print('Antes de convertir a tipo fecha')
    # print(df.head())

    #Conversión a tipo fecha
    df['Fecha'] = pd.to_datetime( df['Fecha'], dayfirst=True )
    # print('Después de convertir a tipo fecha')
    # print(df.head())
    df.set_index('Fecha',inplace=True)
    # print('Después de fecha como el índice')
    # print(df.head())

    #Calcular la variación
    variacion = list()
    for i in range(len(df['TRM'])-1):
        calculo = (abs(df['TRM'][i] - df['TRM'][i+1])/df['TRM'][i]) * 100
        variacion.append(calculo)
    variacion = pd.Series(variacion)
    promedioVariacion = variacion.mean()
    # df['VariacionTRM'] = variacion
    # print('Agregando la variación')
    # print(df)

    #Filtro -> Cuando se disparan (supera la media de la ventana de observación) 
    # los contagios, el valor del dolar
    promedioCasos = df['Casos'].mean()
    df = df[ df['Casos']>=promedioCasos ]

    # #Graficado opcional de los casos acumulados en cada mes después de la manipulación    
    # import matplotlib.pyplot as plt
    # dataCasosMes = df["Casos"].groupby(df.index.month).sum() 
    # dataCasosMes.plot(color="red")
    # plt.title("Total casos por mes")
    # plt.xlabel("Mes")
    # plt.ylabel("Número de casos")
    # plt.show()

    # #Graficado opcional del TRM medio de cada mes después de la manipulación
    # dataMediaPrecioMes = df['TRM'].groupby(df.index.month).mean() 
    # dataMediaPrecioMes.plot(color = "green")
    # plt.title("Valor dólar promedio")
    # plt.xlabel("Mes")
    # plt.ylabel("Valor")
    # plt.show()

    return { 'Promedio Variación':promedioVariacion, 'Registros Mayores':df}


    
#Sección principal
print(analisisTRM('BaseDeDatosReto5.csv'))
#print(analisisTRM('https://raw.githubusercontent.com/luismescobarf/clasesCiclo1/master/BaseDeDatosReto5.csv'))
    