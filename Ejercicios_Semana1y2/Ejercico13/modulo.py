# Creamos el diccionario dónde vamos a guardar los datos por consola
projects = {'Nombre':'',
            'Encargado':'',
            'Fecha':'',
            'Descripcion': ''}

# Creamos la funcion de agregar proyectos al diccionario previamente creado
def agregar_proyectos(nombre, encargado, fecha, descrip):
    projects['Nombre'] = nombre
    projects['Encargado'] = encargado
    projects['Fecha'] = fecha
    projects['Descripcion'] = descrip

    print('\nLos datos fueron guardados exitosamente')
    for clave, valor in projects.items():
        print(f'{clave} : {valor}')

# Creamos la función para actualizar los datos guardados en el diccionario
def actualizar_projects(clave):
    if clave in projects:
        confirmacion = input('Desea realizar cambios en el proyecto?: (si/no) ')
        if confirmacion.lower() == 'si':
            nombre = input('Ingrese el nombre del projecto: ')
            encargado = input('Ingrese el nombre del encargado: ')
            fecha = input('Ingrese la fecha del proyecto: ')
            descrip = input('Ingrese la descripcion del proyecyto: \n')
            agregar_proyectos(nombre, encargado, fecha, descrip)

    print('Cambios realizados con exito: ')
    for clave, valor in projects.items():
        print(f'{clave} : {valor}')

# Por ultimo creamos la función para eliminar proyectos del diccionario/ para eliminar el diccionario
def eliminar_projects(clave):
    global projects
    if clave in projects:
        print('\nEscoga una opción', '\n',
              '1-Eliminar elementos del diccionario', '\n',
              '2-Eliminar el diccionario', '\n')
        
        opcion = int(input('Ingrese la opcion deseada: '))
        
        if opcion == 1:
            projects.clear()
            print(f'Cambios realizados con exito: {projects}')

        elif opcion == 2:
            del projects
            print('Cambios realizados con exito')










