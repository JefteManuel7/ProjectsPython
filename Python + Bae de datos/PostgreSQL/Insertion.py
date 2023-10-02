import psycopg2


# Parametros de conexión a la base datos PostgreSQL
host = 'localhost'  
database = 'students'
user = 'postgres'
password = '$$Adm1n##'

def Ingresar_alumnos(n_alumnos):
    try:
        connection = psycopg2.connect(

            host = host,
            database = database,
            user = user,
            password = password

        )

        cursor = connection.cursor()

        for i in range(n_alumnos):
            nombre = input('Ingrese el nombre del alumno: ')
            apellido = input('Ingrese el apellido del alumno: ')
            edad = int(input('Ingrese la edad del alumno: '))
            numero_identificacion = int(input('Ingrese el numero de identificación: '))

            insert_query = 'INSERT INTO estudiantes(nombre, apellido, edad, numero_identificacion) values(%s, %s, %s, %s)'

            cursor.execute(insert_query, (nombre, apellido, edad, numero_identificacion))

        connection.commit()
        cursor.close()
        connection.close()

        print('Inserción Exitosa!\n')

    

    except psycopg2.Error as e:
        print(f'Error al conectar a PostgreSQL: {e}')
