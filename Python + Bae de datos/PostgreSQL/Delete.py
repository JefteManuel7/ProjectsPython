import psycopg2

host = 'localhost'
database = 'students'
user = 'postgres'
password = '$$Adm1n##'


def eliminar_alumno(id_estudiante):
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
            delete_query = 'DELETE FROM estudiantes WHERE id = %s'
            cursor.execute(delete_query, (id_estudiante,))
            connection.commit()
            print(f'Eliminacion exitosa del estudiante con el ID: {id_estudiante}\n')

        else:
            print(f'Registro ID: {id_estudiante} no encontrado')

        cursor.close()
        connection.close()
    
    except psycopg2.Error as e:
        print(f'Error al conectar PostgreSQL: {e}')