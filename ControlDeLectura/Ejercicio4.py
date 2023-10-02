#Ejercicio 4: Escribir un programa que, dado un número, imprima todos los números primos menores que ese número.

num = int(input('Ingrese un numero: '))
lst = []

for i in range(num):
    resultado = num - i - 1
    lst.append(resultado)
    
print('Numeros menores que el numero dado son los siguientes: ')
for i in lst:
    print(i)