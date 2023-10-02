"""
Este sistema se ha desarrollado para automatizar los procesos en una
biblioteca ; contiene las funciones basicas para llevar el control del
usuario

"""
import Libreria.funcionesBiblioteca as fb

print('\n----------Bienvenido al Sistema de Biblioteca----------- \n')

while True:
    print('Digite la opcion a utlizar:', '\n'
        '0-salir del sistema', '\n',
        '1-Agregar libros', '\n',
        '2-Mostrar Libros en biblioteca', '\n',
        '3-Buscar libro', '\n',
        '4-Eliminar Libro', '\n')
    
    opcion = int(input('Ingrese el numero de la opcion: '))
    if opcion == 0:
        print('Gracias por usar el sistema: \n')
        break
    elif opcion ==1:
        titulo = input('Ingrese el titulo del libro: ')
        autor = input('Ingrese el autor del libro: ')
        fecha = input('Ingrese la fecha de la publicacion: AAA-MM-DD ')
        fb.agregar_libros(titulo, autor, fecha)
        print('\n')

    elif opcion == 2:
        print('El libro a mostrar es: \n')
        fb.mostrar_libro()
        print('\n')

    elif opcion == 3:
        busqueda = input('Digite el nombre del titulo: \n')
        fb.buscar_libro(busqueda)
        print('\n')

    elif opcion == 4:
        busqueda = input('Digite el nombre del titulo: \n')
        fb.buscar_libro(busqueda)
        fb.eliminar_libros(busqueda)


    else:
        print('opcion invalida \n')








