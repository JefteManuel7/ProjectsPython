lst = []
nNumeros = int(input('Ingrese la cantidad de numeros que desea ingresar: '))

for iterador in range(nNumeros):
    num = int(input('Ingrese un numero: '))
    lst.append(num)
    print(lst)


for iterador in lst:
    if iterador % 2 == 0:
        print(iterador)
    else:
        pass
    
