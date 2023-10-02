# LAS EXCEPCIONES EN PYTHON
def division_segura(numerador, denominador):
    
    try:
        resultado = numerador / denominador
        return resultado
    except ZeroDivisionError:
        print('Error: No se puede dividir entre cero')

    except ValueError:
        print('Error: Ha ocurrido algún problema')

x = int(input('Ingrese el numerador: '))
y = int(input('Ingrese el denominador: '))
print(division_segura(x, y))



#--------------------------------------------------------------------
def convert_2_int(cadena):
    try:
        entero = int(cadena)
        return entero
    except ValueError:
        print('Error: La cadena no es valida')

cadena = '1256567'
intCad = convert_2_int(cadena)
print(type(intCad))




#-----------------------------------------------------------------

entrada = input('Ingrese un numero: ')

try:
    numero = int(entrada)
    print(numero)

except ValueError:
    print('Error en la entrada, es numero no valido')

else:
    print('La conversion fue exitosa')



# FINALLY EN LAS EXCEPCIONES
try:
    numerador = float(input('Ingrese el numerador: '))
    denominador = float(input('Ingrese el denominador: '))

    result = numerador / denominador
except ZeroDivisionError:
    print('Error: No se puede dividir entre cero')

else:
    print('El resultado es: ', result)


finally:
    print('El codigo ha sido ejecutado con exito')




# LEVANTAR UNA EXCEPCION CON RAISE
x = -1
if x < 0:
    raise Exception('NO, numeros negativos')




string = 'Hello'
if not type(string) is int:
    raise TypeError('Solo necesitamos enteros')




####
try :
    numerador   = float(input('Ingrese el Numerador: '))
    denominador = float(input('Ingrese el denominador: '))
    
    if denominador == 0:
        raise ZeroDivisionError('No se puede dividir por cero')
    
    resultado = numerador / denominador

except ZeroDivisionError:
    print('Error: No se puede dividir entre cero')

else: 
    print('El resultado es: ', resultado)
    
finally:
    print('El codigo ha sido ejecutado con éxito')




#

class MenorDeEdadError(Exception):
    pass

try:
    edad = int(input('Digite la edad: '))
    if edad < 18:
        raise MenorDeEdadError('Error: Debes ser mayor de edad.')
        
except MenorDeEdadError as e:
        print('Error', e)
else:
    print('Eres mayor de edad!')
    
finally:
    print('al fin se terminó')