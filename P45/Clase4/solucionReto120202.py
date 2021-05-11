def nota_quices(codigo,nota1,nota2,nota3,nota4,nota5):
    
    #Objetivo -> Promedio en escala diferente, desechando
    #la peor nota

    #Algoritmo
    #1) Desechar la peor nota (detectar la peor nota)
    #2) Hallar el promedio ajustado
    #3) Conversión de la escala
    #4) Redondeo a dos cifras decimales

    #Traducción
    peorNota = min( (nota1,nota2,nota3,nota4,nota5) )
    sumatoriaNotas = sum( (nota1,nota2,nota3,nota4,nota5) )
    promedioAjustado = (sumatoriaNotas - peorNota) / 4
    resultadoConversion = promedioAjustado * 5 / 100
    resultadoConversion = round(resultadoConversion,2)
    return f"El promedio ajustado del estudiante {codigo} es: {resultadoConversion}"

print(nota_quices("AA0010276",40,50,39,76,96))


