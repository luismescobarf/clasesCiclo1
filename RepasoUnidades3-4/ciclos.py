#R:Imprimir los primeros 20 números
# https://github.com/luismescobarf/clasesCiclo1/tree/master/RepasoUnidades3-4

#While -> Se recomienda cuando necesitamos mayor generalidad
# x = 1
# while(x<=20):
#     print(x,end='-')
#     x += 1

# #Para (for) -> Colecciones (con certexa conozco el número de veces que debo hacer algo)
# for x in range(20):#Hasta dónde vamos a iterar y empieza en 0
#     print(x+1,end='-')

# for x in range(1,21):#Dónde inicia y dónde termina (estrictamente menor)
#     print(x,end='-')

#Muestre de 2 en 2
# for x in range(1,21,2):#Dónde inicia y dónde termina variar avance
#     print(x,end='-')

for _ in range(5):
    print('Hola Tripulantes')

#Ciclo -> por lo menos una vez y detenerse bajo un criterio
trabajando = True
while(trabajando):
    print('Realizando cómputo 1')
    print('Realizando cómputo 2')
    if( input('Desea salir (s)').lower() == 's'  ):
        trabajando = False

 
