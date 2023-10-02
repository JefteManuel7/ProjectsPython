
lst = []
n = int(input('Ingrese la cantidad de numeros que desea visualizar en formato fibonacci: '))

num1 = 0
num2 = 1
for _ in range(n):
    lst.append(num1)
    num1, num2 = num2, num1 + num2

print(lst)


  