nNumeros = int(input('Ingrese una cantidad de numeros para la lista: '))
lst = []
for _ in range(nNumeros):
    num = int(input('Ingrese un numero: '))
    lst.append(num)
print(lst)
resultado = 0
for numero in lst:
    resultado += numero

print('El resultado de la suma de los numeros en la lista es: ', resultado)