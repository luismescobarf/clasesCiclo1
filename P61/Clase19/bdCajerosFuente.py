#Base de datos cajeros - Rutinas de generación de casos
#######################################################

#Librerías
import json
import random
import pprint as pp

#Función para seleccionar un elemento aleatorio de una lista
def aleatorioLista(lista):
    if lista != []:
        return lista[ random.randint(0, len(lista)-1)  ]

#Función para escribir el diccionario en un archivo JSON
def almacenarCasoPruebaJSON(diccionario, rutaArchivo='casoPruebaTransacciones.json'):
    #Descargar contenedor de datos del caso de prueba
    try:
        with open(rutaArchivo, 'w') as archivo_json:
            json.dump(diccionario, archivo_json)
    except:
        print("Error: No se pudo guardar la información del caso de prueba.")

#Función para generación de listado de fechas
def generadorFechas():
    añosConsiderados = (2020,2021)
    contenedorFechasDias = []
    for año in añosConsiderados:    
        for mes in range(1,13):
            for dia in range(1,29):
                #Limitar las transacciones hasta una fecha actual (final de mayo de 2021)
                if año == 2021 and mes >= 6:                
                    break
                elif año == 2020 and mes < 6:
                    continue
                else:
                    strDia = str(dia)
                    if dia < 10:
                        strDia = '0'+ str(dia)
                    strMes = str(mes)
                    if mes < 10:
                        strMes = '0'+ str(mes)  
                    strAño = str(año)
                    contenedorFechasDias.append(f"{strDia}-{strMes}-{strAño}")
    return contenedorFechasDias

#Salida de diagnóstico
# print("Fechas generadas")
# print(generadorFechas())
# input()

#Función para generación de ids de cajeros aleatorios
def generarIdCajeroAlteatorio(tamañoCodigo):
    letras = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnoprstuvwxyz"
    numeros = "1234567890"
    listaCaracteresCodigo = [str()]*tamañoCodigo
    for i in range(len(listaCaracteresCodigo)):#Realizar el proceso cinco veces        
        #Decidir si es número o letra
        if random.randint(0, 1):
            listaCaracteresCodigo[i] = letras[ random.randint(0, len(letras)-1)  ]#Letra
        else:
            listaCaracteresCodigo[i] = numeros[ random.randint(0, len(numeros)-1)  ]#Número en formato str

    #Decidir si es del banco principal o si es de un banco adquirido
    if random.randint(0, 1):
        listaCaracteresCodigo.append('BP') #Banco principal
    else:
        listaCaracteresCodigo.append('FI') #Firma bancaria integrada (comprada)

    #Convertir el listado a string
    idGenerado = "".join(listaCaracteresCodigo)
    
    #Retornar id tipo str
    return idGenerado

# #Salida de diagnóstico
# print("Id Generado: ",generarIdCajeroAlteatorio(5))
# print("Id Generado: ",generarIdCajeroAlteatorio(5))
# print("Id Generado: ",generarIdCajeroAlteatorio(5))
# print("Id Generado: ",generarIdCajeroAlteatorio(5))
# print("Id Generado: ",generarIdCajeroAlteatorio(5))

#Salida de diagnóstico aleatorio
#print(random.randint(3, 9))

#Parámetros y conjuntos para generación de instancias
tamañoCodigo = 5
maxNumeroCajeros = 1000
maxNumeroTransacciones = 100
contenedorZonas = [1,2,3,4,5,6,7]
contenedorModelosCajeros = [100,101,2017,2020]
contenedorEstados = ['Fuera de Servicio','Operando','Cerrado']          
#contenedorTiposMovimientos = ['retiro','consignacion','transferencia']
contenedorTiposMovimientos = ['retiro','transferencia']
contenedorMontos = [20000,50000,100000,200000,300000,500000,1000000]
contenedorTiposCuenta = ['ahorros','corriente','cuentaVirtual']
contenedorFechasDias = generadorFechas()

#Función para generar un número de transacciones variadas para un cajero
def generacionTransacciones(maxNumeroTransacciones):
    
    #Inicializar el contenedor con las transacciones
    listaTransaccionesGenerada = []

    #Obtener la cantidad aleatoria limitada
    numTransacciones = random.randint(1, maxNumeroTransacciones)

    #Generar y acumular el número de transacciones
    for _ in range(numTransacciones):
        transaccionAux = dict()
        transaccionAux['tipoMovimiento'] = aleatorioLista(contenedorTiposMovimientos)
        transaccionAux['monto'] = aleatorioLista(contenedorMontos)
        transaccionAux['tipoCuenta'] = aleatorioLista(contenedorTiposCuenta)
        transaccionAux['fechaMovimiento'] = aleatorioLista(contenedorFechasDias)
        listaTransaccionesGenerada.append(transaccionAux)

    # #Salida de diagnóstico
    # print("Transacciones antes de retornar")
    # print(listaTransaccionesGenerada)

    #Retornar las transacciones
    return listaTransaccionesGenerada

# #Salida de diagnóstico para transacciones
# [print(i+1," - ",x) for i,x in enumerate( generacionTransacciones(maxNumeroTransacciones) ) ]

#Función para generar un número de transacciones variadas para un cajero
def generacionInstancia(maxNumeroCajeros,maxNumeroTransacciones):
    
    #Generar número de cajeros de la instancia
    numCajerosCaso = random.randint(1, maxNumeroCajeros)

    #Generar códigos de los cajeros
    codigosCajeros = [generarIdCajeroAlteatorio(tamañoCodigo) for i in range(numCajerosCaso)]

    #Inicializar el diccionario de la instancia
    diccionarioInstancia = dict()
    for i in range(numCajerosCaso):        
        #Instanciar el cajero
        diccionarioInstancia[ codigosCajeros[i] ] = {
                'zona': aleatorioLista(contenedorZonas) ,
                'modeloCajero': aleatorioLista(contenedorModelosCajeros) ,
                'estado': aleatorioLista(contenedorEstados) ,
                'transacciones': generacionTransacciones(maxNumeroTransacciones)
        }
    
    #Retornar el caso de prueba
    return diccionarioInstancia

#Salidas de diagnóstico caso prueba
"""print("----->>>>Caso de prueba generado:")
print("----->>>>Caso de prueba generado:")
print("----->>>>Caso de prueba generado:")
caso = generacionInstancia(maxNumeroCajeros,maxNumeroTransacciones)
pp.pprint(caso)
print("----->>>>Fin del caso de prueba generado<<<<<<<<<")
print("----->>>>Fin del caso de prueba generado<<<<<<<<<")
print("----->>>>Fin del caso de prueba generado<<<<<<<<<")
almacenarCasoPruebaJSON(caso,'casoEjemplo2.json')"""

#Generación de los casos de prueba por lote
# numeroCasosPrueba = 1
# for i in range(numeroCasosPrueba):
#     caso = generacionInstancia(maxNumeroCajeros,maxNumeroTransacciones)
#     print('Caso',i+2,'---------------------------------------------')
#     print()
#     print()
#     #pp.pprint(caso)
#     print()
#     print()
#     print('---------------------------------------------')
#     almacenarCasoPruebaJSON(caso,'./ficheroCasosJSON/caso'+str(i+2)+'.json')
#     input()

#Generar un solo caso
caso = generacionInstancia(maxNumeroCajeros,maxNumeroTransacciones)
almacenarCasoPruebaJSON(caso)

#Ejemplo de estructura (algunas imprecisiones)
bdCajerosInstitucion = {
    'F45789': {
        'zona':1,
        'modeloCajero':12,
        'estado':'Fuera de Servicio',
        'transacciones': [
            {'tipoMovimiento':'retiro', 'monto':20000, 'tipoCuenta':'ahorros', 'fechaMovimiento':'12-10-2020'},
            {'tipoMovimiento':'retiro', 'monto':20000, 'tipoCuenta':'ahorros', 'fechaMovimiento':'12-10-2020'}
        ]        
    },
    'F45789': {
        'zona':1,
        'modeloCajero':12,
        'estado':'Fuera de Servicio',
        'transacciones': [
            {'tipoMovimiento':'retiro', 'monto':20000, 'tipoCuenta':'ahorros', 'fechaMovimiento':'12-10-2020'},
            {'tipoMovimiento':'retiro', 'monto':20000, 'tipoCuenta':'ahorros', 'fechaMovimiento':'12-10-2020'}
        ]        
    }
}