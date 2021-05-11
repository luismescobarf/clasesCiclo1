def Saludar():
    print("----------------------------------")
    print("Bienvenidos al torneo de futbol de Bogota")
    print("----------------------------------")
    Equipo = input("Ingrese el nombre del equipo: ")
    return Equipo

def PedirDatos():
    Nombre1 = input("Ingrese el nombre del integrante del equipo #1: ")
    Edad1 = int(input("Ingrese la edad del integrante del equipo #1: "))
    Nombre2 = input("Ingrese el nombre del integrante del equipo #2: ")
    Edad2 = int(input("Ingrese la edad del integrante del equipo #2: "))
    Nombre3 = input("Ingrese el nombre del integrante del equipo #3: ")
    Edad3 = int(input("Ingrese la edad del integrante del equipo #3: "))
    Nombre4 = input("Ingrese el nombre del integrante del equipo #4: ")
    Edad4 = int(input("Ingrese la edad del integrante del equipo #4: "))
    
    return Nombre1,Edad1,Nombre2,Edad2,Nombre3,Edad3,Nombre4,Edad4

def PersonasMayores(Edad1, Edad2, Edad3, Edad4):
    PersonasMayoresDeEdad = 0
    PromedioEdad = 0
    if Edad1 >= 18:
        PersonasMayoresDeEdad += 1
        PromedioEdad += Edad1
    if Edad2 >= 18:
        PersonasMayoresDeEdad += 1
        PromedioEdad += Edad2
    if Edad3 >= 18:
        PersonasMayoresDeEdad += 1
        PromedioEdad += Edad3
    if Edad4 >= 18:
        PersonasMayoresDeEdad += 1
        PromedioEdad += Edad4
    return PersonasMayoresDeEdad, PromedioEdad

def Resultado(PersonasMayoresDeEdad,Nombre1,Edad1,Nombre2,Edad2, Nombre3, Edad3, Nombre4,Edad4, PromedioEdad, Equipo):
    if PersonasMayoresDeEdad >= 2:
        print(f"*************Felicitaciones Equipo {Equipo} Participacion Aprobada********************")
        print("Informacion del equipo")
        print(f"Nombre: {Nombre1} Edad: {Edad1}")
        print(f"Nombre: {Nombre2} Edad: {Edad2}")
        print(f"Nombre: {Nombre3} Edad: {Edad3}")
        print(f"Nombre: {Nombre4} Edad: {Edad4}")        
        PromedioEdad = PromedioEdad / PersonasMayoresDeEdad
        print(f"Promedio de edad de los acudientes: {PromedioEdad}")
    else:
        print("*************Participacion No Aprobada********************")

#Sección Principal
Equipo = Saludar()
Nombre1,Edad1,Nombre2,Edad2, Nombre3, Edad3, Nombre4,Edad4 = PedirDatos()
PersonasMayoresDeEdad, PromedioEdad = PersonasMayores(Edad1, Edad2, Edad3, Edad4)
Resultado(PersonasMayoresDeEdad,Nombre1,Edad1,Nombre2,Edad2, Nombre3, Edad3, Nombre4,Edad4, PromedioEdad, Equipo)

