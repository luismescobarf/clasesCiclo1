def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:
    
    #Algoritmo
    # 1) Identificar la peor nota
    # 2) Calculamos el promedio
    # 3) Convertimos el promedio a escala de 0 a 5
    # 4) Redondeamos el promedio obtenido
    # 5) Armamos el reporte

    peorNota = min( (nota1,nota2,nota3,nota4,nota5) )
    sumatoriaAjustada = sum( (nota1,nota2,nota3,nota4,nota5) ) - peorNota
    promedioAjustado = sumatoriaAjustada / 4
    promedioAjustadoEcala5 = promedioAjustado / 20
    primedioRedondeadoEscala5 = round(promedioAjustadoEcala5,2)
    
    return f"El promedio ajustado del estudiante {codigo} es: {primedioRedondeadoEscala5}"

print(nota_quices("AA0010276",40,50,39,76,96))




