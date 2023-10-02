#--------------------------------ESTRUCTURAS DE DESICION--------------------------------------

#----------------------EJERCICIO --->verificar si un numero es par---------------------------
numero = int(input("Ingrese el numero a verificar:  "))

if numero % 2 == 0:
    print(f'El numero es par: {numero}')


#----------------------EJERCICIO -->verificar contraseña-----------------------------------
password = input("Ingrese la contraseña: ")

if password == 'entrada123':
    print('Contraseña correcta')



#------------------------------------SENTENCIA ELIF-----------------------------------------------
x = 3
y = 7

if x > y:
    print(f'El numero mayor es x: {x}')
elif x == 7:
    print(f'Los numeros son iguales: {x}, {y}\n')
    
#------------------------------------SENTENCIA ELSE-----------------------------------------------
x = 3
y = 7

if x > y:
    print(f'El numero mayor es x: {x}')
elif x == 7:
    print(f'Los numeros son iguales: {x}, {y}')
else:
    print(f'El numero mayor es y: {y}\n')

#---------------------------EJERCICIO PRACTICO-----------------------------------------------
#Elaborar una solucion la cual, dado un valor, verifique si el numero es positivo
number = float(input("Ingrese un numero: "))

if number > 0:
    print(f'El numero es positivo: {number}')
elif number < 0:
    print(f'El numero es negativo: {number}')
elif number == 0:
    print(f'El numero es 0: {number}')
else:
    print("Ingrese un numero\n")


#-----------------------------------------SENTENCIA IF ACORTADA--------------------------------------
a = 9
b = 7
if a > b: print(f"El numero a es mayor: {a}")


#-------------------------------------------SENTENCIA IF ELSE ABREVIADA-------------------------------------
a = 9
b = 8

print(f'El numero a es mayor: {a}') if a > b else print(f'El numero b es mayor: {b}\n')



#-------------------------------VERIFICAR SI UN NUMERO ES PAR----------------------------------------
number = int(input('Ingrese un numero: '))

print(f'El numero es par: {number}') if number % 2 == 0 else print(f'El numero es impar: {number}\n')


#-------------------------------------EJERCICIO CALCULAR EL DESCUENTO DE UNA COMPRA------------------------------
# Si el precio es mayor que 100 recibe un descuento de 15%, sino de un 10%

valorCompra = float(input('Ingrese el monto de la compra: '))

if valorCompra > 100:
    descuento = 0.15
    precioFinal = valorCompra - valorCompra * descuento
    print(f'El precio final es de: {precioFinal}')
else:
    descuento = 0.10
    precioFinal = valorCompra - valorCompra * descuento
    print(f'El precio final es de: {precioFinal}\n')


#----------------------- REESCRITURA DEL CODIGO ANTERIOR-------------------------------------
descuento = 0.15 if valorCompra >= 100 else 0.10
precioFinal = valorCompra - valorCompra * descuento
print(f'El precion final es: {precioFinal}\n')



#-------------------------------CALCULO DEL SALARIO NETO DE UN EMPLEADO--------------------------------------------------
# $ 10, 000 -> 30% de impuesto
# $ 5, 000 -> 20% de impuesto
# $ menos de lo anterior 10%

salarioEmpleado = float(input('Ingrese el salario a evaluar: '))
impuestoSalario = 0.30 if salarioEmpleado > 10000 else 0.20 if salarioEmpleado > 5000 else 0.10

impuestoPagar = salarioEmpleado * impuestoSalario

salarioFinal = salarioEmpleado - impuestoPagar
print(f'El pago final es de: {salarioFinal}\n')


#----------------------------------OPERADOR LOGIO AND IF------------------------------
a = 330
b = 440
c = 10

if a > c and b > c:
    print(True, '\n')


#------------------------------------VERIFICACION DE EDAD Y ALTURA--------------------------
edad = 20
estatura = 165

if edad >= 18 and estatura >= 160:
    print('Eres apto para escalar la montaña')
else:
    print('No cumples con los requisitos\n')


#----------------------SERVICIO DE NEKFLI O DISNEI-----------------------------------
pago = True
membresia = True

acceso_a_contenido = membresia and pago

if acceso_a_contenido:
    print('Bienvenido a nuestros programas')
else:
    print('Pago o membresia invalida\n')



#-------------------------------------EJERCICIO CALCULO DE NOTAS--------------------------
nota = 10

if nota >= 0 and nota <= 10:
    print('Nota valida')
elif nota == 0:
    print('Nota es cero')
else:
    print('Nota es invalida, fuera de rango\n')



#-------------------------------EJERCICIO --> VERIFICAR  SI EL VALOR ES NUMERO PAR Y ENTERO POSITIVO
# IMPAR Y ENTERO POSITIVO
# VALOR ES CERO
# VALOR ES NEGATIVO

number = int(input('Ingrese un numero: '))

if number > 0 and number % 2 == 0:
    print('Es numero positivo par')
elif number > 0 and number % 2 != 0:
    print('Es numero impar y entero positivo')
elif number == 0:
    print('El numero es cero')
else:
    print('El numero es negativo')


#--------------------------------------OPERADOR LOGICO OR IF---------------------------------------------
#----------------------------EJERCICIO DE VERIFICAR AÑO BICIESTO-------------------------
year = int(input('Ingrese el año: '))
yearBiciesto = True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False
print(yearBiciesto, '\n')


#----------------------------EJERCICIO TRIANGULO CON OR---------------------------------
# EQUILTATERO -->tres lados iguales
# ISOSCELES --> dos lados iguales
# ESCALENO --> no tiene lados iguales


lado1 = 4
lado2 = 4
lado3 = 3

if lado1 == lado2 == lado3:
    print('El triangulo es equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('El triangulo es isosceles') 
else:
    print('El triangulo es escaleno\n')


#----------------------------EJERCICIOS CON IF ANIDADOS----------------------------------
a = -1

if a > 0:
    if a % 2 == 0:
        print(' Es par y positivo')
    else:
        print('Impar y positivo')
elif a == 0:
    print('El numero es cero')
else:
    print('Es negativo\n')


#------------------------------EJERCICIO DE VALIDACION DE UN TICKET-------------------------------
validacion_entrada = True
validacion_pelicula = True

if validacion_entrada and validacion_pelicula:
    print('Tienes derecho al descuento del parqueo')
elif validacion_entrada or validacion_pelicula:
    print('Tienes derecho a un descuento')
else:
    print('Te toca pagar las 4 horas del parqueo\n')

# usando pass
condicion_principal = True
condicion_alternativa = False

if condicion_principal:
    # Bloque de codigo principal
    pass
elif condicion_alternativa:
    # Bloque de codigo alternativo
    pass
else:
    # Bloque de codigo alternativo
    pass

#-----------------------------PRACTICA-------------------------------
EdadPorDefecto = int(input('Ingrese tu edad: '))
miEdad = int(input("cual es mi edad?: "))

if miEdad > EdadPorDefecto:
    print('Yo soy mayor que tu')
    edad = miEdad - EdadPorDefecto
    if edad == 1:
        print(f'La diferencia de año es: {edad}')
    elif edad > 1:
        print(f'La diferencia de años es: {edad}')

elif miEdad < EdadPorDefecto:
    print('Es mayor que yo')
elif miEdad == EdadPorDefecto:
    print('Tenemos la misma edad\n')



 #-----------------------------------------------EJERCICIOS PRACTICA--------------------------------------------------------


 #-----------------------------------------------EJERCICIO 1------------------------------------------
number = float(input('Ingrese un numero: '))

if number > 0:
    print('El numero es positivo')
elif number < 0:
    print('El numero es negativo')
else:
    print('El numero es cero \n')

#----------------------------------------------EJERCICIO 2------------------------------------------
number = int(input('Ingrese un numero entero: '))

if number % 2 ==0:
    if number % 3 == 0:
        print('El numero es par y es divisible por 3')
    else: 
        print('El numero es par, pero no es divisible por 3')
elif number % 2 != 0:
    if number % 3 == 0:
        print('El numero es impar y es divisble por 3')
    else:
        print('El numero es impar, pero no es divisible por 3 \n')


#----------------------------------------------EJERCICIO 3------------------------------------------
letter = input('Ingrese una letra: ')

if letter == 'a':
    print('La letra es una vocal')

elif letter == 'b':
    print('La letra es una vocal')

elif letter == 'i':
    print('La letra es una vocal')

elif letter == 'o':
    print('La letra es una vocal')

elif letter == 'u':
    print('La letra es una vocal')

else:
    print('La letra es consonante \n')




#----------------------------------------------EJERCICIO 4------------------------------------------

edadUsuario = int(input('Ingresa tu edad: '))

print('Eres lo suficientemente mayor para conducir' if edadUsuario >= 18 else f'Eres menor de edad. Te faltan {18 - edadUsuario} años para poder conducir. \n')


#----------------------------------------------EJERCICIO 5------------------------------------------


ageHuman = int(input('Ingresa tu edad: '))
myAge = 21

if myAge > ageHuman:
    ageResult = myAge - ageHuman
    print(f'Soy mayor que tu por: {ageResult} años')
elif ageHuman > myAge:
        ageResult = ageHuman - myAge  
        print(f'Tu eres mayor que yo por: {ageResult} años')
elif myAge == ageHuman:
      print(f'Tenemos la misma edad: {myAge}, {ageHuman}')





