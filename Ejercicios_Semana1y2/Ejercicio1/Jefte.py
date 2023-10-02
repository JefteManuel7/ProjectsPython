import modulo as m
salir = False

while salir == False:

    print('Menu', '\n',
      '1. Resta', '\n',
      '2. Suma', '\n',
      '3. Multiplicacion', '\n',
      '4. Division', '\n', 
      '5. Salir', '\n'
      )
    opcion = int(input('Ingrese la opcion a escoger: '))

    if opcion == 1:
            num1 = int(input('Ingrese el primer numero: '))
            num2 = int(input('Inngrese el segundo numero: '))
            resultado = m.restar(num1, num2)
            print('El resultado es: ', resultado)
    elif opcion == 2:
            num1 = int(input('Ingrese el primer numero: '))
            num2 = int(input('Inngrese el segundo numero: '))
            resultado = m.sumar(num1, num2)
            print('El resultado es: ', resultado)
    elif opcion == 3:
            num1 = int(input('Ingrese el primer numero: '))
            num2 = int(input('Inngrese el segundo numero: '))
            resultado = m.multiplicar(num1, num2)
            print('El resultado es: ', resultado)
    elif opcion == 4:
            num1 = int(input('Ingrese el primer numero: '))
            num2 = int(input('Inngrese el segundo numero: '))
            resultado = m.dividir(num1, num2)
            print('El resultado es: ', resultado)
    elif opcion == 5:
            print("Saliendo del programa")
            break
            salir =True
  
    else:
            print("seleccione una opcion correcta")