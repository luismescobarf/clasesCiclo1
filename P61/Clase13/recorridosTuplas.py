nombre = "Tripulante"
apellido = "Rodríguez"
rh = '+'
tipoSangre = 'O' 
edad = 58
certificaciones = ['JavaSE','Python','JavaScript','Vue.js']
tupla = ( nombre,apellido,rh,tipoSangre,edad,certificaciones)
print(tupla)
print(type(tupla))

for elemento in tupla:
    print(elemento)