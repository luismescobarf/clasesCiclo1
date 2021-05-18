#Objetivo -> Aprobar o rechazar hv de desarrolladores con unos
#lineamientos específicos.

#Algoritmo
# 1) Estandarizar la información -> Valores tipo string que son cantidades
# 2) Revisar si cumple el promedio alto de años de experiencia
# 2a) Si no lo cumple, revisar si cumple con lo mínimo (ambas -> conjunción):
#         - Promedio mínimo de experiencia
#         - Escolaridad y tiempo de egreso
# 3) Dependiendo de las revisiones, reportar si se aprueba o se rechaza

#Traducción -> Python
candidato1 = {
                "Nombre Completo":"Juan Pérez",
                "Documento Identidad":"10456789",
                "ExpJava":1.5,
                "ExpPascal":'3+',
                "ExpNET":0,
                "Nivel Estudios":0,
                "Años Egreso":0
            }

candidato2 = {
                "Nombre Completo":"Estudiante MisiónTIC2022",
                "Documento Identidad":"A203440",
                "ExpJava":'3+',
                "ExpPascal":0,
                "ExpNET":'3+',
                "Nivel Estudios":"Profesional",
                "Años Egreso":"2+"
            }

#Función para estandarizar si es alfanumérico el campo a numérico
def estandarizarAlfanumerico(valorAlfanumerico):
    #Revisión de tipos y parseo
    valorNumerico = float()
    if isinstance(valorAlfanumerico,str):
        valorNumerico = float(valorAlfanumerico[0])
    else:
        valorNumerico = valorAlfanumerico
    #Retorno
    return valorNumerico

#Modularización requerimiento
def probarCandidato(candidato):
    
    expJava = estandarizarAlfanumerico(candidato["ExpJava"])
    expPascal = estandarizarAlfanumerico(candidato["ExpPascal"])
    expNET = estandarizarAlfanumerico(candidato["ExpNET"])
    aEgreso = estandarizarAlfanumerico(candidato["Años Egreso"])
    
    experienciaPromedio = sum( (expJava,expPascal,expNET) )/3

    if experienciaPromedio >= 2.5:
        #print("El candidato ",candidato2["Nombre Completo"]," ha sido aprobado")
        print(f"El candidato {candidato['Nombre Completo']} ha sido aprobado")
    elif experienciaPromedio >= 1.5 and aEgreso >= 2:
        print(f"El candidato {candidato['Nombre Completo']} ha sido aprobado")
    else:
        print(f"El candidato {candidato['Nombre Completo']} ha sido rechazado!")


#Estandarización
# expJava = float()
# if isinstance(candidato2["ExpJava"],str):
#     expJava = float(candidato2["ExpJava"][0])
# else:
#     expJava = candidato2["ExpJava"]
# expJava = estandarizarAlfanumerico(candidato2["ExpJava"])
# expPascal = estandarizarAlfanumerico(candidato2["ExpPascal"])
# expNET = estandarizarAlfanumerico(candidato2["ExpNET"])
# aEgreso = estandarizarAlfanumerico(candidato2["Años Egreso"])

# print("Resultados de estandarización")
# print(expJava)
# print(expPascal)
# print(expNET)
# print(aEgreso)

#experienciaPromedio = sum( (expJava,expPascal,expNET) )/3

# if experienciaPromedio >= 2.5:
#     #print("El candidato ",candidato2["Nombre Completo"]," ha sido aprobado")
#     print(f"El candidato {candidato2['Nombre Completo']} ha sido aprobado")
# else:
#     if experienciaPromedio >= 1.5 and aEgreso >= 2:
#         print(f"El candidato {candidato2['Nombre Completo']} ha sido aprobado")
#     else:
#         print(f"El candidato {candidato2['Nombre Completo']} ha sido rechazado!")

# if experienciaPromedio >= 2.5:
#     #print("El candidato ",candidato2["Nombre Completo"]," ha sido aprobado")
#     print(f"El candidato {candidato2['Nombre Completo']} ha sido aprobado")
# elif experienciaPromedio >= 1.5 and aEgreso >= 2:
#     print(f"El candidato {candidato2['Nombre Completo']} ha sido aprobado")
# else:
#     print(f"El candidato {candidato2['Nombre Completo']} ha sido rechazado!")

probarCandidato(candidato1)
probarCandidato(candidato2)











