#-----------------------------------------------------------EJERCICIOS DE CONTROL DE LECTURA-------------------------------------------------------

#1
if 10:
    print('Número es igual a 10')

# SOLUCION ----> faltaban los dos puntos

#2
numero = 8
if numero < 10:
    print('Numero es menor que 10')


# Solucion ---> falta la variable y la palabra then esta


#3
numero = 8
if numero > 5:
    print('El número es mayor que 5')

# SOLUCION ----> no tenia la sangria correspondiente (tabulacion hacia la derecha)




# 4
numero = 3
if numero % 2 == 0:
    print('Numero par')
else:
    print('Numero no es par')

# SOLUCION ---->>> el codigo esta correcto, pero seria excelente complementarlo con mas codigo


# 6
valor = 'Python'

if valor == 'python':
    print('El valor es python')
else:
    print('El valor es python')

# SOLUCION ---> CAMBIAR EL != POR ==


# 7
edad = 18

if edad == 18:
    print('Tienes 18 años')

#SOLUCION ----> el error era que la condición de comparación era string '18', se debe cambiar a entero 


# 8
numero = 6
if numero > 5:
    print('El mayor que 5')

# SOLUCION ---> faltaba declarar la variable numero


# 9
valor = 'Hola'

if valor.startswith('H'):
    print(True)

# SOLUCION ---> faltaba el proceso de la estructura condicional si se cumplia la condición


# 10
numero = 10
if numero == 10:
    print('Numero es igual a 10')

# SOLUCION ---> se estaba usando el metodo de asignación = en vez de el de comparación == 




# 10
nota = 75
if nota >= 90:
    print('A')
elif nota >= 80:
    print('B')
elif nota >= 70:
    print('C')
else:
    print('D')


# SOLUCIN ---> la tercer condición estaba mal ya que era un if despues de un elif, es incorrecto, se debe cambiar a elif









#------------------------------------------------------LOS CICLOS-----------------------------------------------
flag = 0

while flag < 5:
    print(flag)
    flag += 1



#--------------------------------------------------- USANDO EL ELSE EN EL CICLO WHILE------------------------------------------

flag = 0

while flag < 5:
    print(flag)
    flag += 1
else:
    print(f'El valor de flag es: {flag}')





""" 
IMPLEMENTE UNA SOLUCION, LA CUAL ADIVINE UN NUMERO PREVIAMENTE DEFINIDO
#POR UN USUARIO Y QUE OTRO USUARIO LO DIGITE TRATANDO DE ADIVINAR EL DEFINIDO

Mensaje de inicio: Digita el numero para adivinar.
sino adivina el mensaje es: Intenta de nuevo
Si adivino: Felicidades adivinastes
"""

flag = 4
numero = int(input('Digita el numero para adivinar: '))

while numero !=  flag:
    numero = int(input('Intenta de nuevo: '))
else:
    print('Felicidades adivinastes')
    

# segunda solución
flag = 4
estado = False

while not estado:
    numero = int(input('Digital el numero para adivinar: '))

    if numero == flag:
        print('Felicidades adivinastes')
        estado = True
    else:
        print('Intente de nuevo')



#
i = 1
suma = 0
n = 1000

while i <= n:
    suma  += i
    i += 1
print(f'La suma de los numero es: {suma}')




# CALCULAR EL FACTORIAL DE UN NUMERO
n = int(input('Ingrese el numero a calcular: '))
factorial = 1
contador = 1


while contador <= n:
    factorial *= contador
    contador += 1
print(f'El factorial del numero {n} es {factorial}')



#-------------------------------------------- CICLO FOR-----------------------------------------------
frutas = ['mango', 'jocote', 'piña', 'guineo', 'sandia', 'melocoton']

for x in frutas:
    print(x)



cadena = 'Hola como estas? me llamo jefte'

for x in cadena:
    print(x)


# ---------------------------------------CICLOS FOR EN TUPLAS-------------------------------------------------------
tupla = ('a', 'b', 'c', 3, 4  )

for elementos in tupla:
    print(elementos)



# USANDO LA PALABRA CONTINUE
flag = 0
while flag < 10:
    if flag == 5:
        continue
    print('El valor despues de continue', flag)
    flag += 1
 
    

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('esta es otra opción')



# en diccionarios
informationPersonal = {
    'Nombre': 'Jefte',
    'Apellido': 'Montenegro',
    'Edad': '26',
    'Municipio': 'Ilopango'
}

#for info in informationPersonal:
#    print(info)


for info, valor in informationPersonal.items():
    print(info, valor)


# USANDO LA SENTENCIA BREAK PARA UN CICLO FOR
frutas = ['mango', 'jocote', 'papaya', 'sandia', 'melon']

for it in frutas:
    print(it)
    if it == 'jocote':
        break


# USANDO BREAK Y CONTINUE EN UN CICLO FOR
tuplaNumeros = (1, 2, 3, 4, 6, 7)

for num in tuplaNumeros:
    print(num)
    if num == 5:
        break
    else:
        continue


#-------------------------------------------FUNCION RANGE EN UN CICLO FOR-------------------------------------------------

for it in range(6):
    print(it)


# HACIENDO LISTA CON LA FUNCION RANGE (star, stop, step)
lista = list(range(0, 10, 2))
print(lista)




#-----------------------------USANDO ELSE EN EL CILO FOR---------------------------------------

for it in range(12):
    print(it)
else:
    print('Finalizamos el ciclo for')



#----------------------------------- BUCLES ANIDADOS-------------------------------------------
frutas = ['mango', 'melon', 'jicama', 'jocotes']
estado = ['bueno', 'maduro', 'picado', 'podrido']

for it in frutas:
    for jt in estado:
        print(f"Este {it} esta muy {jt}")


# TABLA DE MULTIPILCAR
numero = int(input('Ingrese el numero que sea ver: '))

for it in range(1, 11):
    resultado = numero * it
    print(f'{numero} x {it} = {resultado}')


# CONTADOR DE VOCALES
cadena = 'Hola soy Jefte Manuel, tengo 21 años'
contador = 0
for letra in cadena:
    if letra.lower()  in 'aeiouáéíóú':
        contador += 1

print('Numero de vocales: ', contador)