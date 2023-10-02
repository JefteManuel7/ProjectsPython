#Importamos la libreria para realizar la conexión a la base de datos en MySQL
import mysql.connector

#Creamos una excepción para la conexión con la base de datos
def insertar_estudiantes(n_alumnos):
    try:
        #Realizamos la conexión a la base de datos
        connection = mysql.connector.connect(

            host = 'localhost',
            user = 'root',
            password = '123456',
            database = 'students'
        )

        #Creamos un objeto para hacer manipulaciones de datos
        cursor = connection.cursor()



        
        for iterador in range(n_alumnos):
            nombre = input('Ingrese el nombre del alumno: ')
            apellido = input('Ingrese el apellido del alumno: ')
            edad = int(input('Ingrese la edad del alumno: '))
            numero_identificacion = int(input('Ingrese el número de indentifiacion del alumno: '))
            
            insert_query = 'INSERT INTO estudiantes (nombre, apellido, edad, numero_identificacion) VALUES (%s, %s, %s, %s)'

            cursor.execute(insert_query, (nombre, apellido, edad, numero_identificacion))

        
        
        connection.commit()
        cursor.close()
        connection.close()

        print('Insercion exitosa\n')
    except mysql.connector.Error as e:
     print(f'Error al conextar MySql: {e}')