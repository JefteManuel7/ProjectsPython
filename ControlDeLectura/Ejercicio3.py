#Escribir un programa que, dada una lista de números, imprima la lista de números sin duplicados.

lst = []
nCantidad = int(input('Ingrese la cantidad de numeros que desea añadir a la lista: '))

for _ in range(nCantidad):
    num = int(input('Ingrese un numero: '))
    lst.append(num)

numeros_Noduplicados = []
for iterador in lst:
    if lst.count(iterador) == 1:
        numeros_Noduplicados.append(iterador)

if len(numeros_Noduplicados) == 0:
    print('No hay números no duplicados en la lista.')
else:
    print('Números no duplicados:')
    for num in numeros_Noduplicados:
        print(num)