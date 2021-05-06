def generadorRegiones(largo1,largo2,largo3,largo4,porcentajeAjuste):
    
    #1) Hallar el área de las cuatro piezas
    #2) Promediar las áreas obtenidas (AreaPromedio)
    #3) Calcular diferencia permitida 𝐷𝑖𝑓𝑒𝑟𝑒𝑛𝑐𝑖𝑎𝑃𝑒𝑟𝑚𝑖𝑡𝑖𝑑𝑎 = 𝑃𝑜𝑟𝑐𝑒𝑛𝑡𝑎𝑗𝑒𝐴𝑗𝑢𝑠𝑡𝑒 ∗ 𝐴𝑟𝑒𝑎𝑃𝑟𝑜𝑚𝑒𝑑𝑖𝑜
    #4) Encontrar la dferencia de cada pieza frente al área promedio de la pieza (valor absolulto)
    #5) Comparamos la diferencia de cada pieza con el área promedio y la diferencia permitida
    #   (condicional)
    #6) Cada pieza que cumpla, suma 1 en piezas aprobadas y se acumula el área.
    #7) Revisar cuántas piezas pasaron, si son 2 o más se estructura un mensaje
    #   y si son menos de dos se estructura otro mensaje
    #8) Se retorna el mensaje



#Llamados o casos de prueba
# generadorRegiones(3,3,3,3,0.2)
# generadorRegiones(3,1,2,2.5,0.5)
# generadorRegiones(3,1,2,2.5,0.8)
# generadorRegiones(3,1,0.5,3,0.8)
