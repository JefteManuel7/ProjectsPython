    
#print(3+3)  

#Ejercicio 1
resultado = max(5, 10, 3, 8)
print(resultado)

#Ejercicio 2
resultado = round(3.14159, 2)
print(resultado)

#Ejercicio 3
resultado = min(5, 10, 3, 8)
print(resultado)

#Uso de la Función print() ->imprime mensaje en consola
print('Hola Mundo')

nombre = 'Jefte'
edad = 23

print('Mi nombre es: ' , nombre, 'y mi edad es: ', edad)


#Función Len()
#Len() ->nos muestra la longitud de una cadena de caracteres
mensaje = 'Buenas tardes, este es un Hola Mundo'
longitud = len(mensaje)
print('La longitud del mensaje es: ', longitud)

# 1-Practica
#1.1 Definir una variable 'nombre' que guarde el nombre de ustedes, 'edad' que almacena la edad de ustedes
nombre = 'Jefte'
edad = 21

#1.2 Imprimir 
print('Mi nombre es: ', nombre, ' y mi edad es: ', edad)

#1.3 encontrar la longitud de la variable nombre
print(len(nombre))

#Función type()
mensaje = 'Hola mundo'
print('El tipo de valor de la variable es: ', type(mensaje))

#Tipod de datos float, str, int
cadena = '123'
print('El tipo de dato de la variable es: ', type(cadena))

cadena = int(cadena)
print('El tipo de dato de la variable es: ', type(cadena))

print(cadena + cadena)


valor = 14
print('El valor de la variable es: ', type(valor))
valor = float(valor)
print('El tipo de dato de la variable es: ', type(valor))



#COMENTARIOS
#COMENTARIOS POR LINEA
""" COMENTARIOS MULTILINEA
Este es un comentario multilinea , que acabo yo de escribir
para explicar un proceso
"""

def saludos(nombre):
    """
    """
    print('Hola!' + nombre + '!')
saludos('Jose')



y = 'John'
x = 5

print(x*y)
"""
-----------EJEMPLOS DE CAMECASE----------
miVariableEjemplo
nombreUsuario
calcularImpuesto


-------------EJEMPLOS DE PASCAL CASE--------
MiVariableEjemplo
NombreUsuario
CrearUsuario



----------EJEMPLOS SNAKE CASE-------------
numero_de_telefono
cantidad_de_productos
mi_variable_ejemplo


---------EJEMPLOS DE LOWER CASE--------
mivariableejemplo
minombre
cantidadalumnos

-------EJEMPLOS UPPER CASE-------------
NOMBRE_ALUMNO
CANTIDAD_SALARIO
MIVARIABLEEJEMPLO
"""

x = 2
y = 'naranja'
z = 14.6

print(x)
print(y)
print(z)

x, y , z = 2, 'sandia', 23.7
print(x,'\n', y,'\n', z,'\n')


x =  y =  z = 'Esto es una cadena'
print(x, y, z)


x = 'Python  is awesome: Python es asombroso!'
print(x)

#Concatenacion
x = 'Python is awesome!'
y = ':'
z = 'Python es asombroso!'
print(x, y, z)
print( x + y + z)

""""
a, b, c = 1, 2, 3
print(a, b, c)
print(a + b + c) #al ser de tipo int, se suma, y no se produce la concatenacion
print(f'La suma es: ' {a + b + c}+  ';' + 'La multiplicacion es: ' + {a * b * c})
"""

# Imprimir variables en una linea
nombre = 'Jefte Beltran'
edad = 21
print(f"Mi nombre es: {nombre} y tengo: {edad}")

print()

valorHora = 17.5
totalHoras = 8
nombreTrabajador = 'Jefte'
print(f'El nombre del empleado es: {nombreTrabajador}\n y El valor de la hora es:  {valorHora}\n y el total de horas es: {totalHoras}\n y su salario total es: {valorHora * totalHoras}')

#Concatenacion con el operador % 
nombre = 'Alice'
edad = 30
peso = 120
print('Mi nombre es %s y tengo %d años %d.\n\n'%(nombre, edad, peso))


#Tabulación en la impresión
print('Nombre: \n\t José\n Edad: \n\t 37')

print('Hola')
print('Mundo')

print()

print('Hola', end = '')
print('Mundo')
print('\n')
#
colores = ['verde', 'amarillo', 'rojo']
print(colores, sep = ',')
print('\n')
print(*colores, sep = ',')
print('\n')
print(*colores)
print('\n')


#Posiciones en una lista
print(colores[0])
print('\n')
print(colores[1])
print('\n')
print(colores[2])
print('\n')
print(colores[-1])

print()

#Aplicando las propiedades de mayusculas y minisculas
mensaje = "hoLA muNdo"
mensajeMayuscula = mensaje.upper()
mensajeMiniscula = mensaje.lower()
print(mensajeMayuscula,'\n', mensajeMiniscula)


#----------------------------EJERCICIO PRACTICO-------------------------
nombre = 'Jefte Manuel'
print(f'\nEl tipo de dato que contiene la variable es: {type(nombre)} \ny el contenido de la variable es: {nombre}')

apellidos = 'Beltran'
print(f'\nEl tipo de dato que contiene la variable es: {type(apellidos)} \ny el contenido de la variable es: {apellidos}')


apellidos_dos = 'Pineda'
print(f'\nEl tipo de dato que contiene la variable es: {type(apellidos_dos)} \ny el contenido de la variable es: {apellidos_dos}')


edad = 21
print(f'\n El tipo que contiene la variable es: {type(edad)} \ny el contenido de la variale es: {edad}')

nacionalidad = 'Salvadoreña'
print(f'\nEl tipo de dato que contiene la variable es: {type(nacionalidad)} \ny el contenido de la variable es: {nacionalidad}')

sexo = 'Masculino'
print(f'\nEl tipo de dato que contiene la variable es: {sexo} \ny el contenido de la variable es: {sexo}')


print(f'\nMi nombre es: {nombre} \ny mis apellidos son: {apellidos} {apellidos_dos}\nMi edad es: {edad}'
      f'\ny mi nacionalidad es: {nacionalidad} \ny mi sexo es: {sexo}')
