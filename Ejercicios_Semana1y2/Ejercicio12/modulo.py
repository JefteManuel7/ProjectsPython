
# Creamos el diccionario
dictionary = {'Nombre': '',
              'Precio': 0,
              'Stock': 0}

# Creamos la función para agregar productos a un diccionario
def agregar_producto(nombre_producto, precio, stock):
    dictionary['Nombre'] = nombre_producto
    dictionary['Precio'] = precio
    dictionary['Stock'] = stock

    print("Productos guardados:")
    for clave, valor in dictionary.items():
        print(f'{clave} : {valor}')


# Función para modificar los valores de un diccionario   
def modificar_product(clave):
    if clave in dictionary:
        producto = input('Desea realizar cambios en producto? (si/no) ')
        if producto.lower() == 'si':
            nombre_producto = input('Ingrese el nombre del producto: ')
            dictionary['Nombre'] = nombre_producto
            print(f'Cambios realizados con exito: {dictionary["Nombre"]}')


        precio = input('Desea realizar cambios en producto? (si/no) ')
        if precio.lower() == 'si':
            precio_valor = int(input('Ingrese el precio del producto: '))
            dictionary['Precio'] = precio_valor
            print(f'Cambios realizados con exito: {dictionary["Precio"]}')


        stock = input('Desea realizar cambios en stock? (si/no) ')
        if stock.lower() == 'si':
            stock_cantidad = int(input('Ingrese la cantidad de producto existente: '))
            dictionary['Stock'] = stock_cantidad
            print(f'Cambios realizados con exito: {dictionary["Stock"]}')

        for clave, valor in dictionary.items():
            print(f'{clave}: {valor}')


            
def eliminar_producto(clave):
    global dictionary
    if clave in dictionary:
        print('\nEscoga una opción', '\n',
              '1-Eliminar elementos del diccionario', '\n',
              '2-Eliminar el diccionario', '\n')
        
        opcion = int(input('Ingrese la opcion deseada: '))
        if opcion == 1:
            dictionary.clear()
            print(f'Los elementos han sido eliminados con exito: {dictionary}\n')
        elif opcion == 2:
            del dictionary
            print('Los cambios se han realizado correctamente', '\n')
        else:
            print('El diccionario no se ha eliminado', '\n')

