# -------------------------OPERADORES ARTIMETICOS---------------------------
a = 12
b = 14

#---------------------------------OPERADOR SUMA----------------------------------
c = a + b
print(f'La suma de los dos numeros es: {c}')

#----------------------------------OPERADOR RESTA-----------------------------
c = a - b
print(f'La resta de los dos numeros es: {c}')

#--------------------------------MULTIPLICACION------------------------------
c = a * b
print(f'La multiplicacion de los dos numeros es: {c}')

#-----------------------------------DIVISION--------------------------------
c = a/b
print(f'La division de los dos numeros es: {c}')

#----------------------------------DIVISION ENTERA-----------------------------
c = a // b
print(f'La division entera de los dos numeros es: {c}')

#------------------------------MODULO---------------------------------
c = a % b
print(f'El modulo de los dos numeros es: {c}')

#--------------------------------POTENCIACION----------------------------------
c = a ** b
print(f'La potenciacion de los dos numeros es: {c}\n')

#-------------------------PRACTICA----------------------
print((4 + 6)* 2)

print(10**2 /5)

print((15-3)* 4/2)

print((27 % 5) + 10)

print(19 // 3 - 2)

print(((5 +2 )*3) **2 /(10%3))


x = 4
print((2 * x) + (3 * x) - (5 / x))

import math
a = 6
b = 4
c = -8
discriminante = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(discriminante)) / (2 * a)
x2 = (-b - math.sqrt(discriminante)) / (2 * a)

print(x1, x2, '\n')



#--------------------------OPERADORES DE ASIGNACION----------------------------------
x = 5
print(x)
x += 5
print(x)
x -= 5
print(x)
x *= 12
print(x)
x /= 4
print(4)
x **= 5
print(x)
x %= 4
print(x)


#--------------------------------------AND--------------------------------------------
x = 10 
y = 17
z = 40

# COMPARANDO CON EL OPERADOR AND
if x < y and y < z:
    print("true")
else:
    print("false")


#----------------------------------------OPERADOR OR------------------------------------------
x = 10 
y = 17
z = 40

print(x < y)
print(y > z)
print(x < y or y > z)

print()

#---------------------------------------OPERADOR NOT--------------------------------------------
x = 10 
y = 17
z = 40

print(not x < y)
print(not y > z)
print(not(x < y or y > z))



#-----------------------------OPERADOR IS NOT
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)
print(x is z)

print('\n')
print(x is not y)
print(x is not z)

#-----------------------------OPERADOR IN----------------------------------
print('\n')
lista = [1, 2, 3, 4]
print(3 in lista)
print(7 in lista)


#--------------------------------------------EJERCICIOS PRACTICOS----------------------------------------

#------------------------EJERCICICIO 1------------------------------------------------
productoPrecioOriginal = float(input("Ingrese el precio original del productor: "))
descuento = int(input("Ingrese el descuento del producto: "))
porcentajeDescuento = (descuento* 100) / 100

precioFinal = productoPrecioOriginal -  porcentajeDescuento 
print(f'El precio original del producto era: {productoPrecioOriginal}\ny su descuento era: {descuento}\n'
      f'Y el precio final es de: {precioFinal}')
#--------------------------------EJERCICIO 2---------------------------------------------------------
pesoUsuario = float(input("Ingrese su peso en kilogramos: "))
alturaUsuario = float(input("Ingrese su altura: "))

imcUsuario = pesoUsuario / alturaUsuario**2
print(f"El peso de usuario es: {pesoUsuario}\n"
      f"SU altura es: {alturaUsuario}\n"
      f"Su IMC es: {imcUsuario}")

#--------------------------------EJERCICIO 3---------------------------------------------------------
horaIngresada = int(input("Ingrese las horas a calcular: "))
minutosIngresado = int(input("Ingrese los minutos a calcuar: \n"))

opcion = int(input("Menu de conversion: \n"
      "1- Horas a segundos \n"
      "2- Minutos a segundos\n"
      "3-Ambos\n"))
resultado = 0
if (opcion == 1):
    resultado = horaIngresada * 3600
    print(f"El resultado es: {resultado}")
elif(opcion == 2):
    resultado = minutosIngresado * 60
    print(f"El resultado de la conversion es: {resultado}")
elif(opcion == 3):
    resultado = (horaIngresada * 3600, minutosIngresado * 60)
    print(f"El resultado es: {resultado[0]} segundos para las horas y {resultado[1]} segundos para los minutos.")

#--------------------------------EJERCICIO 4---------------------------------------------------------
montoComida = float(input("Ingrese el monto de la comida: "))
porcenPropina = float(input("Ingrese el porcentaje de propina a depositar: "))

totalPagar = montoComida + (montoComida * (porcenPropina / 100))
print(f"El total de consumo es: {montoComida} \n"
      f"El porcentaje de propina es: {porcenPropina}\n"
      f"El total a pagar es: {totalPagar}\n")


#--------------------------------EJERCICIO 5---------------------------------------------------------
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
print("La temperatura en grados Fahrenheit es: ", temperatura_fahrenheit)


#--------------------------------EJERCICIO 6---------------------------------------------------------
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

resultado = (num1//num2, num1%num2)
print(f"El cociente de la division es: {resultado[0]} y el resto de la division es: {resultado[1]}")




#-------------------------------------EJERCICIOS DE APLICACIÓN DE CONOCIMIENTOS-----------------------------------------------------------
a = 15
b = 26
c = 12

variable1 = a + b * c
variable2 = (a + b) * c
variable3 = (a / b) * c
variable4 = a / (b * c)
variable5 = (a ** b)     + c
variable6 = a ** (b + c)

print(f"El resultado de la variable 1 es: {variable1}\n"
      f"El resultado de la variable 2 es: {variable2}\n"
      f"El resultado de la variable 3 es: {variable3}\n"
      f"El resultado de la variable 4 es: {variable4}\n"
      f"El resultado de la variable 5 es: {variable5}\n"
      f"El resultado de la variable 6 es: {variable6}\n")