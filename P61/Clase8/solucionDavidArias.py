def evaluarCandidato(candidato):
    experienciaJava=float()
    if isinstance(candidato["experienciaJava"],str): #verifica si la variable es de x tipo, devuelve booleano
        print("La primera posición es: ",candidato["experienciaJava"][0])
        experienciaJava=float(candidato["experienciaJava"][0])
    else:
        experienciaJava=candidato["experienciaJava"]
    experienciaPascal=float()
    if isinstance(candidato["experienciaPascal"],str): #verifica si la variable es de x tipo, devuelve booleano
        print("La primera posición es: ",candidato["experienciaPascal"][0])
        experienciaPascal=float(candidato["experienciaPascal"][0])
    else:
        experienciaPascal=candidato["experienciaPascal"]
    experienciaNet=float()
    if isinstance(candidato["experienciaNet"],str): #verifica si la variable es de x tipo, devuelve booleano
        print("La primera posición es: ",candidato["experienciaNet"][0])
        experienciaNet=float(candidato["experienciaNet"][0])
    else:
        experienciaNet=candidato["experienciaNet"]
    aEgreso=float()
    if isinstance(candidato["aEgreso"],str): #verifica si la variable es de x tipo, devuelve booleano
        print("La primera posición es: ",candidato["aEgreso"][0])
        aEgreso=float(candidato["aEgreso"][0])
    else:
        aEgreso=candidato["aEgreso"]
    promedioExperiencia=(experienciaJava+experienciaPascal+experienciaNet)/3
    if promedioExperiencia>2.5:
        return candidato["nombreCompleto"]+" aprobado a segunda ronda"
    elif promedioExperiencia>=1.5 and promedioExperiencia<=2.5:
        if aEgreso>2:
            return candidato["nombreCompleto"]+" aprobado a segunda ronda"
        else:
            return candidato["nombreCompleto"]+" No aprobado"
    else:
        return candidato["nombreCompleto"]+" No aprobado"
