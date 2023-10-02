import Modulo as m

numTemp = int(input('ingrese la cantidad de temperaturas: '))
lst = []

for iterador in range(numTemp):
    temperatura = int(input('Ingrese una temperatura: '))
    lst.append(temperatura)
    print(lst)

print('\n')
print('------------MENU------------', '\n',
      '1. Convertir de Fahrenheit a Celsius', '\n',
      '2. Convertir de Celsius a Fahrenheit', '\n',
      '3. Salir', '\n')

opcion = int(input('Ingrese la opcion deseada: '))

while opcion != 3:
    lstResult = []

    if opcion == 1:
        for i in range(len(lst)):
            temp_celsius = m.convertCels(lst[i])
            lstResult.append(temp_celsius)
        print('Conversión de Fahrenheit a Celsius fue exitosa: ', lstResult, '\n')

    elif opcion == 2:
        for i in range(len(lst)):
            temp_fahrenheit = m.convertFahrent(lst[i])
            lstResult.append(temp_fahrenheit)
        print('Convertir de Celsius a Fahrenheit fue exitosa: ', lstResult, '\n')

    else:
        print('Seleccione una opcion correcta.')

    print('------------MENU------------', '\n',
          '1. Convertir de Fahrenheit a Celsius', '\n',
          '2. Convertir de Celsius a Fahrenheit', '\n',
          '3. Salir', '\n')
    
    opcion = int(input('Ingrese la opcion deseada: '))

print('Gracias!')
