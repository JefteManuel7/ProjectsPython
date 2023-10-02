import psycopg2

host = 'localhost'
database = 'students'
user = 'postgres'
password = '$$Adm1n##'

def actualizar_alumno(id_estudiante):
    try:
        connection = psycopg2.connect(
            host = host, 
            database = database, 
            user = user,
            password = password
        )

        cursor = connection.cursor()

        select_query = 'SELECT id FROM estudiantes WHERE id = %s'
        cursor.execute(select_query, (id_estudiante,))
        resultado = cursor.fetchone()

        if resultado:
            nuevo_nombre = input('Ingrese el nombre del estudiante: ')
            nuevo_apellido = input('Ingrese el apellido del estudiane: ')
            nueva_edad = int(input('Ingrese la edad del estudiante: '))

            update_query = 'UPDATE estudiantes SET nombre = %s, apellido = %s, edad = %s WHERE id = %s'
            cursor.execute(update_query, (nuevo_nombre, nuevo_apellido, nueva_edad, id_estudiante))
            connection.commit()
            print('Actualización exitosa\n')

        else:
            print(f'Registro con ID: {id_estudiante} no encontrado')

        cursor.close()
        connection.close()
    except psycopg2.Error as e:
        print(f'Error al conectar con PostgreSQL: {e}')