import modulo 


salir = False
lst = []

while salir == False:
    print('Menu', '\n',
                       '1. Registrar Alumno', '\n',
                       '2. Salir', '\n')
    opcion = int(input('Ingrese la opcion a escoger: '))
   
    if opcion == 1:
        nombre = input('Ingrese el nombre del estudiante: ')
        edad = int(input('Ingrese la edad del estudiante: '))
        modulo.RegistrarAlumno(nombre, edad)
        
        if edad >= 18:
            lst.append(nombre)
        
    elif opcion == 2:
        print('Saliendo del programa')
        break
        salir = True
    else:
        print('Ingrese la opcion correcta')

print('Estudiantes mayores de 18 años:')
for nombre in lst:
    print(nombre)
