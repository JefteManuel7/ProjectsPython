# --------EJERCICIO 1----------------
nombreUsuario = input("Ingrese su nombre completo: ")


def saludos(nombreUsuario):
    print('!Hola!' + nombreUsuario + ' Bienvenido a nuestro programa.')
saludos(nombreUsuario)

#-------------EJERCICIO 2----------------------------   
b = float(input("Ingrese la base: "))
h = float(input("Ingrese la altura del triangulo: "))
a = b * h / 2

print(f"El area del triangulo es: {round(a, 2)}")


#------------------EJERCICIO 3------------------------
nombreUsuarios = input("Ingrese su nombre: ")
edadUsuario = int(input("Ingrese su edad: "))
ciudadResidencia = input("Ingrese la ciudad de residencia: ")

print(f"El nombre de usuario es: {nombreUsuarios} y el tipo de variable es: {type(nombreUsuarios)}\n"
      f"La edad del usuario es: {edadUsuario} y el tipo de variable es: {type(edadUsuario)} \n"
      f"La ciudad de residencia es: {ciudadResidencia} y el tipo de variable es: {type(ciudadResidencia)}\n")

#------------trabajo en clase--------------------
x = 1
y = 1.35465
z = 2j

print(type(x), type(y), type(z))



z = 35E3
y = 12e4
z = 1.2e4
print(x, y, z)

x = 3 + 5j
y = -5j
z = -3 + 0j
print(type(x), type(y), type(z),'\n')


#-------------------EJERCICIO-------------------------
print(type(3))
print(type(3.14))
print(type( 1 + 8j))
print(type('Hello Word!'))
print(type([1, 2, 3]))
print(type({1: "one", 2: "two", 3: "three"}))
print(type({1, 2, 3}))
print(type((1, 2, 3)), '\n')

# int: para un contador de un bucle
totalContador = 0

for i in range(1, 5):
    totalContador = totalContador + i
    print('Valor de i: ', i)
    print('Valor del contador: ', totalContador)
print('El tipo de la variable contador es: ', type(totalContador), 'y su valor es: ', {totalContador}, '\n')



notas = [7.0, 6.0, 9, 10.0, 8.4, 5.7, 9.4, 9.7]
promedio = sum(notas)/len(notas)
print('El promedio de notas: ', promedio, '\n')



# ------------------validar usuario-------------------------------
usuarioRegistrado = True

if usuarioRegistrado:
    print('Bienvenido al curso')
else:
    print('Usuario no esta en el curso')

print()

#Listas tipo string
nombre = ['Jefte', 'Manuel', 'Beltran', 'Pineda']
print(f'Lista de Nombres: {nombre}\n')

# tuple: Dias de la semana y otra con valores
diasSemana = ('L', 'M', 'W', 'J', 'V')

print(diasSemana)
print(type(diasSemana), '\n')

#------------------DICCIONARIOS----------------------
dicContacts = {
    'Chrstian': 898556,
    'Dennis': 454547578,
    'Jefte': 5444545,
    'Alexa': 544545
}

print(f'El diccionario contiene: {dicContacts} y el tipo es: {type(dicContacts)}\n')

# ----------------CONVERTIR DATOS---------------------
x = 1
y = 2.8
z = 3j

convertX = float(x)
converty = complex(y)
#convertX = int(z) #no se puede convertir

# Cadena str a entero
cadena = '475875'
type(cadena)


cadena = '[1, 2, 3, 4, 5]'
lista = eval(cadena)
print(type(lista))
print(lista)


#Acortas cadenas
a = 'Hola mundo: Hello Word'
b = 'No se me ocurre nada'
print(len(a), len(b))

print(a[2:21])
print(b[4:5])



#-----------------------------------------------EJERCICIOS--------------------------------------------------

#--------------------------------------EJERCICIO1--------------------------
mensaje = 'Bienvenidos a Python'
print(mensaje)

#---------------------------------EJERCICIO 2-----------------------------------+
poema = """
sdfkjdkfjdfkjsd
sdkjsdksjds
skdjsdjskdjs
wdkjsd
"""
print(poema)



#---------------------------------EJERCICIO 3---------------------------------------

cadena ='Bienvenidos a Python'
print(len(cadena))
subcadena = cadena[14:]
print(subcadena)

#_-----------------------------------EJERCICIO 4---------------------------------
cadena = 'abcdefghilj'
subcadena = cadena[2:6]
print(subcadena)



#-------------------------------------- EJERCICIO 5-----------------------------------------

cadena = 'Python es genial'
variable = cadena[9:]
print(variable)

a = ' Hello word'
print(a.strip())
print(a.upper(), a.lower())

#reemplazar letras en cadena
a = 'Hello Word'
print(a.replace("H", "J"))
print(a.replace("llo", "llou"))

# diviir cadenas
a = ' Hello word'
print(a.split(","))
print(a.split("o"))

a = 'Hello'
b = 'Work'
print(a + ' ' + b)

# -------------------------aplicando el metodo format----------------------------
edad = 34
cadena = 'Mi nombre es Texto, y tengo {}'
print(cadena.format(edad))



superMercado = 'La despensa de don jefte'
cantidadGranos = 3
precioLibra = 1.40
total = precioLibra * cantidadGranos
ordenSuper = 'Fui a {} y compre {} libras de frijoles a un precio de {} dolares cada libra y gaste un total de: {} dolares' 
print(ordenSuper.format(superMercado, cantidadGranos, precioLibra, total))



superMercado = 'La despensa de don jefte'
cantidadGranos = 3
precioLibra = 1.40
total = precioLibra * cantidadGranos
ordenSuper = 'Fui a {0} y compre {1} libras de frijoles a un precio de {2} dolares cada libra y gaste un total de: {3} dolares' 
print(ordenSuper.format(superMercado, cantidadGranos, precioLibra, total))



# ---------CARACTERES DE SALIDA-----------------
superMercado = 'La despensa de don \'Jefte\''
print(superMercado)






#----------------------------------------------------EJERCICIOS PRACTICOS-----------------------------------------------------
#---------------------------EJERCICIO 1------------------------------------

cadena = """Programación es arte y ciencia, un lenguaje que crea la realidad, 
una forma de dar vida a la inteligencia, y al mundo digital una identidad
"""
print(cadena.split())



#-------------------------------EJERCICIO 2------------------------------------

# -------------------------------EJERCICIO 2-------------------------------------
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(f"Las primeras 10 letras del abecedario: {abecedario[:10]}\n")
print(f"Las ultimas 10 letras del abecedario: {abecedario[-10:]}\n")
print(f"El abecedario al reves: {abecedario[::-1]}\n")
