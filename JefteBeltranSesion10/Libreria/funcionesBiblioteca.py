# Modulo de funciones de la Biblioteca

"""
Las funciones a desarrollar son las siguientes:

Agregar libro
Mostrar libro
Buscar libro

"""

import datetime

#LISTA QUE CONTENDRA INFORMACION DE LOS LIBROS
libro = []

def agregar_libros(titulo, autor, fecha):
    libro.append({'Titulo':titulo, 'Autor':autor, 'Fecha':fecha})

def mostrar_libro():
    for libr in libro:
        print(f"Titulo: {libr['Titulo']}, Autor: {libr['Autor']}, Fecha de publicacion {libr['Fecha']}")


def buscar_libro(tituloLibro):
    encontrado = False
    for dato in libro:
        if tituloLibro.lower() in dato['Titulo'].lower():
            print(f"Titulo: {dato['Titulo']}, Autor: {dato['Autor']}, Fecha de publicacion {dato['Fecha']}")
            encontrado = True
            break
        if not encontrado:
            print('no existe libro')



def eliminar_libros(tituloLibro):
    encontrado = False
    for it in libro:
        if tituloLibro.lower() in it['Titulo'].lower():
            print('Eliminado')
            libro.remove(it)
            encontrado = True
            break
        if not encontrado:
            print('Libro no encontrado')

         



    