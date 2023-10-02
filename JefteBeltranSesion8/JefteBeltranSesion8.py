# --------------------------------FUNCIONES EN PYTHON---------------------------------------------------

def my_function():
    print('Hola mundo desde una funcion')
    print('*************************')

my_function()
print('\n')

def saludar():
    print('Hola buenos dias!!')

print('Me gusta saludar', saludar())
print('\n')


def saludo(nombre):
    print(f'Hola buenos dias {nombre}')

saludo('Jefte')
print('\n')

def sumar(x, y):
    suma = x + y
    return suma
resultado = sumar(4, 5)
print('La suma es: ', resultado, '\n')


def print_name(name):
    print(name + 'es el nombre')
print_name('Jefte')
print('\n')


def myFunctio(nombre1, nombre2):
    print(nombre1 + ' ' + nombre2)

myFunctio('Jefte', 'Manuel')
print('\n')




# ARGUMENTOS DE PALABRA CLAVE
def myFunctio(nombre1, nombre2, nombre3):
    print(nombre1 + ' ' + nombre2 + ' ' + nombre3)

myFunctio(nombre1 = 'Jefte', nombre2 = 'Manuel', nombre3 = 'Yefte')
print('\n')


def saludar(nombre, mensaje):
    print(f'{mensaje}, {nombre}')
saludar(nombre = 'Jefte', mensaje = 'Hola')



#
def generar_informe(titulo, contenido, autor):
    informe = f' Titulo: {titulo} \nContenido: {contenido} \nAutor: {autor}'
    print(informe)

generar_informe(titulo='Informe Mensual', contenido='Ventas y Proyecciones', autor='Jefte')
print('\n')





#** kwargs SI NO SE SABE  CUANTOS ARGUMENTOS  DE PALABRAS CLAVE SE PASARAN
def my_function(**kid):
    print('El ultimo nombre es' + kid['mname'])

my_function(pnombre = 'Juan', mname = 'Maria', lname = 'Pablo')
print('\n')


# MONSTRAR INFORMACION
def mostrar_informacion(**kwargs):
    if 'nombre' in kwargs:
        print('Nombre:', kwargs['nombre'])
    if 'edad' in kwargs:
        print('Edad:', kwargs['edad'])
    if 'ubicacion' in kwargs:
        print('Ubicación:', kwargs['ubicacion'])

# Ejemplos de llamadas a la función
mostrar_informacion(nombre='Juan', edad=30, ubicacion='Ciudad XYZ')
mostrar_informacion(nombre='María', ubicacion='Ciudad ABC')
print('\n')


# CREAR PERFIL
def crear_perfil(**kwargs):
    perfil = {}
    for clave, valor in kwargs.items():
        perfil[clave] = valor
    return perfil

usuario = crear_perfil(nombre = 'Ana', edad = 28, ciudad = 'Barcelona')
print(usuario, '\n')



# RECURSIVIDAD

# factorial sin recursividad
def factorial_noRecursivo(n):
    result = 1
    for it in range(1, n + 1):
        result *= it
    return result
n = 10
print(f'El factoria de {n} es {factorial_noRecursivo(n)}\n')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1 )
numero = 3
resultado = factorial(numero)

print(f'El factorial de {numero} es {resultado}\n')


# SI DEFINIMOS DOS PARAMETROS, SIEMPRE DEBEMOS PASAR DOS ARGUMENTOS, SINO DARA ERROR


# EJEMPLO 1, FUNCION PARA CALCULAR AL AREA DE UN RECTANGULO
def area_rectangulo(base, altura):
    area = base * altura
    return area
print('El area de un rectangulo es: ', area_rectangulo(12, 15))
print('\n')




# EJEMPLO 2: FUNCION PARA IMPRIMIR UNA LISTA
def imprimir_lista(lista):
    for iterador in lista:
        print(iterador)

lst = [1, 2, 'hola']
imprimir_lista(lst)
print('\n')



# EJEMPLO 3: FUNCION PARA VERIFICAR SI UN NUMERO ES PAR

def es_par(numero):
    if numero % 2 == 0:
        return print('Es par')
    else:
        return print('No es par')

es_par(13)
print('\n')


# otra forma
def es_Par(number):
    if number % 2 == 0:
        return True
    else:
        return False
number = 5

if es_Par(number):
    print('Es par')
else:
    print('No es par')

print('\n')




# EJEMPLO 4: FUNCION QUE REGRESA UNA LISTA DE NUMEROS PARES
def lista_pares(n):
    lstPares = []
    for iterador in range(n + 1):
        if iterador % 2 == 0:
            lstPares.append(iterador)
    return lstPares

print(lista_pares(10))
print('\n')





# ARGUMENTOS ARBITRARIOS, SE PUEDEN PASAR VARIOS ARGUMENTOS, USANDO *args
def my_function(*nombre):
    print('El nombre es ' + nombre[1])

my_function('Juan', 'Mario', 'Pablo')
print('\n')


def imprimir_argumentos(*args):
    for arg in args:
        print(arg)

imprimir_argumentos(1, 2, 3, 'Hola', 'Mundo', ['a', 'b'])
print('\n')


def promedio_notas(*notas):
    totalNotas = 0
    for nota in notas:
        totalNotas += int(nota)
    promedio = totalNotas/len(notas)
    return promedio
notas = [6, 7, 8, 9, 10, 7, 9, 10]
promedioFinal = promedio_notas(*notas)

print(promedioFinal)
print('\n')


# CONCATENAR
def concatenar(*args):
    resultado = ' '.join(args)
    return resultado

frutas = 'guineo', 'naranja', 'limon'

mixFrutas = concatenar(*frutas)
print('Mix frutas: ', mixFrutas)
print('\n')


#
def media_aritmetica(*args):
    total = sum(args)
    cantidad = len(args)
    media = total/cantidad
    return media

notass = [8, 9 , 10, 12, 10, 5, 7, 9, 6]
preomdioFinal = media_aritmetica(*notass)
print('El promedio es: ', round(preomdioFinal, 1))
print('\n')



# MULTIPLICAR TODOS LOS NUMEROS DADOS   
def productoria(*args):
    producto = 1
    for it in args:
        producto *= it
    return producto
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

totalMultipliacion = productoria(*numeros)
print('El total es: ', totalMultipliacion, '\n')



#SUMA SIN RECURSIVIDAD
def suma_sin_recursividad(n):
    suma = 0
    for it in range(1, n + 1):
        suma += it
    return suma
n = 4
print(f'La suma es: {suma_sin_recursividad(n)} \n')


# SUMA CON RECURSIVIDAD
def suma_recursividad(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursividad(n - 1)
    
n = 4
print(f'La suma es: {suma_recursividad(n)} \n')


# FUNCIONES LAMBDA: ES UNA FUNCION ANONIMA

x = lambda a : a + 10
print(x(12))

#
f = lambda x : x ** 2 + 2 * x + 3
print(f(12))

x = lambda a, b, c: a + b + c
print(x(12, 4, 8), '\n')


#
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11), '\n')

# FILTRAR LISTAS
id_empleados = [341, 34, 55, 122, 110, 120, 78, 77]
pares = filter(lambda x : x % 2 == 0, id_empleados)
print(list(pares),'\n')


# OTRA FORMA
id_empleados = [341, 34, 55, 122, 110, 120, 78, 77]

def filtrado_par(*id_empleados):
    return filter(lambda x : x % 2 == 0, id_empleados)

pares = filtrado_par(*id_empleados)
print(list(pares), '\n')