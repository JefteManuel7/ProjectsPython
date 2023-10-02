lstPar = []
lstImpar = []

n = int(input('Ingrese la cantidad de numeros que va ingresar: '))

for iterador in range(n):
    number = int(input('Ingrese un numero: '))
    if number % 2  == 0:
        lstPar.append(number)
    else:
        lstImpar.append(number)

print()
print('Los numeros pares son los siguientes: ')
for i in range(len(lstPar)):
    print(lstPar[i])
    
print()
print('Los numeros impares son los siguientes: ')
for i in range(len(lstImpar)):
    print(lstImpar[i])