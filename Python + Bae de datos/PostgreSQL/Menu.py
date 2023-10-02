import psycopg2

host = 'localhost'
database = 'students'
user = 'postgres'  # Quita la coma al final del valor del usuario
password = '$$Adm1n##'

try:
    connection = psycopg2.connect(

        host=host,
        database=database,
        user=user,  # Sin coma al final
        password=password
    )

    from Insertion import Ingresar_alumnos
    from Update import actualizar_alumno
    from Delete import eliminar_alumno

    exit = False

    while not exit:
        print('--------------Menú------------------')
        print('1-Ingresar alumnos')
        print('2-Actualizar alumnos')
        print('3-Eliminar alumnos')
        print('4-Salir\n')

        opcion = int(input('Ingrese la opción deseada: '))

        if opcion == 1:
            n_alumnos = int(input('Ingrese la cantidad de alumnos que desea ingresar: '))
            Ingresar_alumnos(n_alumnos)

        elif opcion == 2:
            id_estudiante = int(input('Ingrese el ID del estudiante: '))
            actualizar_alumno(id_estudiante)

        elif opcion == 3:
            id_estudiante = int(input('Ingrese el ID del estudiante a eliminar: '))
            eliminar_alumno(id_estudiante)

        elif opcion == 4:
            exit = True
            print('Gracias por usar el sistema, vuelva pronto!')

        else:
            print('Escoge una opción correcta')
            pass
        
except psycopg2.Error as e:
    print(f"Error al conectar a PostgreSQL: {e}")
