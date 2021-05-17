def consultarBD(id):

    #Base de Datos
    candidato1={
            "nombreCompleto":"Pedro Picapiedra",
            "documentoIdentidad":"1200AC",
            "experienciaJava":0.5,
            "experienciaPascal":0.5,
            "experienciaNet":9,
            "nivelEstudios":"Profesional",
            "aEgreso":0
    }
    candidato2={
            "nombreCompleto":"Tripulante MinTIC2022",
            "documentoIdentidad":"101010",
            "experienciaJava":1,
            "experienciaPascal":1,
            "experienciaNet":"3+",
            "nivelEstudios":0,
            "aEgreso":0
    }

    #Relación de tipos: int -> booleanos
    #                    0 -> False
    #                    Diferente de 0 -> True
    if id:
        return candidato1
    else:
        return candidato2

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
    #if promedioExperiencia>=2.5: #Requerimiento original
    #Fortalecimiento planteado por Edgar y Héctor
    if promedioExperiencia>=2.5 and experienciaJava >= 1.5 and experienciaPascal>= 1.5 and experienciaNet >= 1.5:
        return candidato["nombreCompleto"]+" aprobado a segunda ronda"
    #elif promedioExperiencia>=1.5 and promedioExperiencia<=2.5:
    elif promedioExperiencia>=1.5 and aEgreso>=2:        
        return candidato["nombreCompleto"]+" aprobado a segunda ronda"           
    else:
        return candidato["nombreCompleto"]+" No aprobado"

#Ejecución
candidato = consultarBD(0) #Consultar el candidato a la base de datos
print(evaluarCandidato(candidato))#Revisar y reportar
candidato = consultarBD(1) #Consultar el candidato a la base de datos
print(evaluarCandidato(candidato))#Revisar y reportar


