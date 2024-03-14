bandas =[]

opcion = 100
while(opcion != 5):
    opcion = int(input('Digita una opcion: '))
    print('***********FESTIVAL ALTAVOZ************')
    print('***************************************')
    print('1. Registrar banda')
    print('2. Ver cartel del festival')
    print('3. Buscar banda')
    print('4. Modificar banda')
    print('5. Finalizar')
    opcion=int(input('Digita una opcion: '))
    if opcion ==1:
        banda = {}
        #Se llena el objeto o diccionario de la banda [] = lista o arreglo= mucchos datos del mismo tipo // Diccionario es un conjunto de diferentes datos
        banda['id'] = int(input('Digite el id: '))
        banda['nombre'] = input('Nombre: ')
        banda['genero'] = input('Genero: ')
        banda['clasificacion'] = input('Clasificacion: ')
        banda['costo'] = int(input('Digite el costo: '))
        banda['tiempo'] = int(input('Tiempo en tarima'))

        #Como agrego un diccionario a una lista?
        bandas.append(banda)           
        
    elif opcion==2:
        #Recorriendo una lista para imprimir sus elementos
        for bandaAuxiliar in bandas:
            print(f"{bandaAuxiliar['id']} -- {bandaAuxiliar['nombre']}")        
    elif opcion==3:
        #busca un elemento dentro de una lista
        bandaBuscada = input('Digiota la banda que quieres buscar: ')
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"] == bandaBuscada:
                print('Aca esta  mi banda panita')
                break
            else:
                print('La banda no esta registrada')                   
        
    elif opcion==4:
        #Tarea: modificar un elemento de la lista.
        pass
    elif opcion==5:
        pass
    else:
        print('Digita una opcion valida')

    