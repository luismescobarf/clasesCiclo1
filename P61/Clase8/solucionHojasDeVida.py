def consultarBD(id):

    #Base de Datos
    candidato1 = {
                "nombreCompleto":"Pedro Picapiedra",
                "documentoIdentidad":"1200AC",
                "añosExperienciaJava":"3+",
                "añosExperienciaPascal":1,
                "añosExperienciaNET":1.5,
                "nivelEstudios":"Profesional",
                "añosEgreso":"2+"
    }
    candidato2 = {
                    "nombreCompleto":"Tripulante MinTIC2022",
                    "documentoIdentidad":"101010",
                    "añosExperienciaJava":1,
                    "añosExperienciaPascal":1,
                    "añosExperienciaNET":"3+",
                    "nivelEstudios":0,
                    "añosEgreso":0
    }

    #Relación de tipos: int -> booleanos
    #                    0 -> False
    #                    Diferente de 0 -> True
    if id:
        return candidato1
    else:
        return candidato2

#Algoritmo hojas de vida desarrolladores
# 1) Obtener la información de la base de datos 
# (llega un diccionario)
# 2) Las variables (campos del diccionario) con las cuales
# se va a trabajar, hacerles una estandarización a los tipos.
# 3) Aprobar aquellos que tengan más de 2.5 años de experiencia
#     Si los años de experiencia son menores a 2.5 y mayor
#     mayor o igual a 1.5
#         Revisamos los años de egresado
#             Si cumple con los años de egresado aprobado
# 4) Retornar el aprobado (mensaje o un boolean)

#Traducción a Python:
candidato = consultarBD(1)
nom = candidato["nombreCompleto"]
print(nom)

#Ejemplo de estandarización de los años de xp
#Si es tipo string extraer la primera posición y convertirla
#a numérico
añosExperienciaJava = float()
if isinstance(candidato["añosExperienciaJava"],str):
    print("La primera posición es: ",candidato["añosExperienciaJava"][0])
    añosExperienciaJava = float(candidato["añosExperienciaJava"][0])
else:
    añosExperienciaJava = candidato["añosExperienciaJava"]

