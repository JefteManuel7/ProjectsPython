lstCompras = []

condicion = input('Desea crear una lista de productos? SI O NO: ')

if condicion == 'si':
    salir = False
    while salir !=  True:
        compra = input('Ingrese un producto: ')
        lstCompras.append(compra)
        exit = input('Desea seguir agregando productos?: ')
        if exit == 'si':
            continue
        else:
            salir = True

else:
    print('oK')
print('\n')
print('---------Lista de productos---------')
for i in range(len(lstCompras)):
    print('Producto', i + 1, ':', lstCompras[i])    