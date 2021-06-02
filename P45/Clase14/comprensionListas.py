#-> List Comprehension: Generar colecciones de forma resumida

#Requerimiento: solicitar un número y presentar todos los números
#impares hasta el número ingresado (incluído)

#Satisfacer de manera convencional el requerimiento:
# n = int(input('Ingrese un número: '))
# for i in range(1,n+1):
#     if i % 2 != 0:
#         print(i,end=' ')

# #Generar colecciones list comprehension
# n = int(input('Ingrese un número: '))
# #Generar todos los números hasta el valor n ingresado
# #list(range(n+1))#Solución con conversión de contenedores
# [print(i,end='-') for i in range(1,n+1) if i%2!=0]#Solución comprensión de listas

# #Generar un diccionario donde la llave sea un número y el valor sea ese mismo número
# #elevado al cuadrado hasta el valor ingresado (solamente los pares) -> una sola línea
# print({ i:i**2 for i in range(1,int(input('Ingrese un número: '))+1) if i%2==0  })

#Requerimiento: solicitar al usuario una serie de palabras (separadas por espacios)
#y mostrar aquellas que tengan únicamente vocales abiertas (a,e,o)

#Algoritmo:
# 1) Solicitar palabras al usuario
# 2) Separar las palabras por espacios
# 3) Para cada una de las palabras que tienen únicamente vocales abiertas
# 4)    Mostrar la palabra en pantalla

# #Solución línea a línea (Unidad1 - Unidad3)
# print('Ingrese las palabras a revisar separadas por espacios:')
# entradaUsuario = input('Entrada -> ')
# palabras = entradaUsuario.split(' ')
# conjuntoVocalesCerradas = set()
# conjuntoVocalesCerradas.add('i')
# conjuntoVocalesCerradas.add('u')
# for palabra in palabras:
#     tieneVocalesCerradas = False
#     for letra in palabra:
#         if letra in conjuntoVocalesCerradas:
#             tieneVocalesCerradas = True
#     if not tieneVocalesCerradas:
#         print(palabra)

#Solución comprensión de listas (Unidad4)
print('Ingrese las palabras a revisar separadas por espacios:')

#Predicado
def tieneVocalesCerradas(palabra):
    hipotesisTieneVocalesCerradas = False
    for letra in palabra:
        if letra in {'i','u'}:
            hipotesisTieneVocalesCerradas =  True
    return hipotesisTieneVocalesCerradas
        
#Comprensión de listas para el requerimiento
[print(palabra) for palabra in input('Entrada -> ').split(' ') if not tieneVocalesCerradas(palabra) ]
        
            


