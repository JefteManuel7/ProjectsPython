#Ejercicio 5: Escribir un programa que, dado un conjunto de números, imprima el número más grande y el número más pequeño
nCantidad = int(input('Ingrese la cantidad de numeros que desea ingresar: '))
lst = []

for i in range(nCantidad):
    num = int(input('Ingrese un numero: '))
    lst.append(num)

for i in lst:
    numero_Grande = max(lst) 
    numero_Pequenio = min(lst)

print(f'El numero mas grande es: {numero_Grande}, y el numero mas pequeño es: {numero_Pequenio}')

