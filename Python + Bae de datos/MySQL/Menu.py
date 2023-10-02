import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='students'
)

from Delete import eliminar_estudiante
from Insertion import insertar_estudiantes
from Update import actualizar_estudiante

exit = False 

while not exit: 
    
    print('------------Menu----------')
    print('1-Ingresar alumnos')
    print('2-Actualizar información de alumnos')
    print('3-Eliminar información de alumno')
    print('4-Salir del sistema\n')
    
    opcion = int(input('Ingrese la opción deseada: '))

    if opcion == 1:
        n_alumnos = int(input('Cuantos alumnos desea registrar?: '))
        insertar_estudiantes(n_alumnos) 

    elif opcion == 2:
        id_estudiante = int(input('Ingrese el ID del estudiante a actualizar: '))
        actualizar_estudiante(id_estudiante)  

    elif opcion == 3:
        id_estudiante = int(input('Ingrese el ID del estudiante a eliminar: '))
        eliminar_estudiante(id_estudiante)

    elif opcion == 4:
        exit = True

    else:
        print('Opción no válida. Por favor, ingrese una opción válida.')
