#Ejemplos listas compuestas
bdFrutas = [
    ['Pera',1200,'Importada',56],
    ['Manzana',780,57],
    ['Borojó',800,57], 
    ['Uva',4000,'Importada',51],       
    ['Mango',1100,57],
    ['Banano',2000,'Importado',59],
    [2000,'Feijoa',57],
    [57,'Mandarina',600],
    ['Kiwi']  
]

#Recorrer la base de datos subíndices
# for i in range(len(bdFrutas)):
#     print(f"{i+1}) Nombre Fruta: {bdFrutas[i][0]} Precio = {bdFrutas[i][1]}")

for i in range(len(bdFrutas)):
    cadenaSalidaFruta = str()
    cadenaSalidaFruta += f"Fruta {i+1}) "

    for j in range(len(bdFrutas[i])):        
        cadenaSalidaFruta += f"Atributo{j+1}: {bdFrutas[i][j]}, "

    print(cadenaSalidaFruta)
    
        




