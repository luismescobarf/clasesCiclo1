#Función respondiendo al requerimiento
def indicadoresPetroleo(rutaArchivo):

    #Pandas para anlítica (descriptiva)
    import pandas as pd

    #Analizar la extensión del archivo
    if rutaArchivo[-3:].lower() != 'csv':
        return "Extensión inválida"
    
    #Si cumple la extensión del archivo cargar el archivo en un dataframe para trabajar
    #-> Hablar con capa externa a la aplicación donde estamos
    try:
        df = pd.read_csv(rutaArchivo,sep=',')        
    except:
        return "Error al leer el archivo de datos"

    # #Salida de diagnóstico
    # print('Contenido del dataframe cargado')
    # print(df)
    
    # print('Nombres de las columnas')
    # print(df.columns)

    df["Fecha"] = pd.to_datetime(df["Fecha"],dayfirst=True)    
    print(df)

    df.set_index("Fecha",inplace=True)
    print(df)

    #Calcular la variación
    variacion = list()
    for i in range(len(df['Ecopetrol'])-1):
        calculo = (abs(df['Ecopetrol'][i] - df['Ecopetrol'][i+1])/df['Ecopetrol'][i]) * 100
        variacion.append(calculo)

    # #Observación de la variación (No hace parte del requerimiento, recordar índices)
    # df['Variacion'] = pd.Series(variacion)
    # print(df)

    #Conversión buscando aprovechar funciones de pandas
    variacion = pd.Series(variacion)
    promedioVariacion = variacion.mean()

    #Promedio de casos de COVID
    promedioCasos = df["Casos"].mean()
    df = df[ df["Casos"] <= promedioCasos ]
    #print(df)

    #Graficado opcional de los casos acumulados en cada mes después de la manipulación    
    import matplotlib.pyplot as plt
    dataCasosMes = df["Casos"].groupby(df.index.month).sum() 
    #dataCasosMes.plot(kind='barh', color="red")
    dataCasosMes.plot(color="red")
    plt.title("Total casos por mes")
    plt.xlabel("Mes")
    plt.ylabel("Número de casos")    
    plt.show()
    
    #Graficado opcional del valor medio de la acción de Ecopetrol de cada mes después de la manipulación   
    dataMediaPrecioMes = df['Ecopetrol'].groupby(df.index.month).mean() 
    #dataMediaPrecioMes.plot(kind='barh', color = "green")
    dataMediaPrecioMes.plot(color = "green")
    plt.title("Valor Ecopetrol promedio")
    plt.xlabel("Mes")
    plt.ylabel("Valor")
    plt.show()


    #Retorno del requerimiento
    return {'Promedio Variación':promedioVariacion,'Registros Menores':df}


#Sección principal
print(indicadoresPetroleo('BaseDeDatosReto5.csv'))


    

    