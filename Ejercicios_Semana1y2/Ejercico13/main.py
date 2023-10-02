# Importamos el modulo dónde guardamos nuestras funciones
import modulo as m

# Creamos un bucle para que nos muestre el menu de opciones constantaemente, y salir si el usuario lo requiere
salir = False
while not salir:
    print('\n', 10*'-', 'Menu', 10*'-',
          '\n1-Agregar Proyecto \n',
          '2-Actualizar Proyecto \n',
          '3-Eliminar Proyecto \n',
          '4-Salir \n')
    opcion = int(input('Ingrese la opción deseada: '))

    if opcion == 1:
        while True: 
            nombre = input('Ingrese el nombre del projecto: ')
            encargado = input('Ingrese el nombre del encargado: ')
            fecha = input('Ingrese la fecha del proyecto: ')
            descrip = input('Ingrese la descripcion del proyecyto: ')
            m.agregar_proyectos(nombre, encargado, fecha, descrip)

            contin = input('\nDesea seguir ingresando productos? (si/no) \n')
            if contin.lower() !=  'si':
                break
    
    elif opcion == 2:
        clave = input('Ingrese la clave para actualizar: ')
        m.actualizar_projects(clave)

    elif opcion == 3:
        clave = input('Ingrese la clave para eliminar: ')
        m.eliminar_projects(clave)


    elif opcion == 4:
        print('Gracias pr usar el sistema! Vuelva pronto')
        salir = True

    else:
        print('\n','Ingrese una opcion correcta')
        opcion = int(input('Ingrese la opción deseada: '))
