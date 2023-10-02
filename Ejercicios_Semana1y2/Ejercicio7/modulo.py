def tabla_multi(num):
    lst = []  # Mover la lista fuera del bucle para acumular los resultados
    for i in range(1, 11):
        resultado = num * i
        lst.append(resultado)
    print('La tabla de multiplicar de', num, 'es:')
    for resultado in lst:
        print(resultado)

