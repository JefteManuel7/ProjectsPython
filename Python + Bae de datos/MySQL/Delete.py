import mysql.connector

def eliminar_estudiante(id_estudiante):
    try:
        connection = mysql.connector.connect(

            host = 'localhost',
            username = 'root',
            password = '123456',
            database = 'students'

        )
        print('La conexión a MySQL fue exitosa')
        cursor = connection.cursor()

        id_estudiante = int(input('Ingrese el id del estudiante a eliminar: '))

        select_query = 'SELECT id FROM estudiantes WHERE id = %s'
        cursor.execute(select_query, (id_estudiante,))
        resultado = cursor.fetchone()

        if resultado:
            delete_query = 'DELETE FROM estudiantes WHERE id = %s'
            cursor.execute(delete_query, (id_estudiante,))
            connection.commit()
            print(f'Eliminación exitosa del estudiante con el ID: {id_estudiante}\n')
        else:
            print(f'No se encontrón ningún estudiante con ID {id_estudiante}')

        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f'Error al conectar a MySQL: {e}')