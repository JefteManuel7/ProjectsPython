import modulo as m


salir = False
while not salir :
    print(30*'-')
    print('Menu')
    print(30*'-', '\n')
    print('1. Agregar producto', '\n',
        '2- Actualizar Producto', '\n',
        '3- Eliminar Producto', '\n',
        '4- Salir', '\n'
        )

    opcion = int(input('Ingrese la opción deseada: '))

    if opcion == 1:
        while True:
            nombre_producto = input('Ingrese el nombre del producto: ')
            precio = int(input('Ingrese el precio del producto: '))
            stock = int(input('Ingrese la cantidad existente del producto actualmente: '))
            m.agregar_producto(nombre_producto, precio, stock)
            print(m.agregar_producto, '\n')

            contin = input('Desea seguir ingresando productos? (si/no) ')
            if contin.lower() !=  'si':
                break
             
    elif opcion == 2:
        clave = input('Ingrese la clave que desea buscar: ')
        m.modificar_product(clave)

    elif opcion == 3:
        clave = input('Ingrese la clave a buscar: ')
        m.eliminar_producto(clave)

    
    elif opcion == 4:
        print('Gracias pr usar el sistema! Vuelva pronto')
        salir = True
    
    else:
        print('\n','Ingrese una opcion correcta')
        opcion = int(input('Ingrese la opción deseada: '))

