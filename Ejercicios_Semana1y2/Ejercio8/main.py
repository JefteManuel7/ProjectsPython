import modulo as m

print('Nota: su contraseña debe tener una longitud de 8 caracteres')
print('Debe contener al menos una letra y un numero para ser correcta')
passw = input('Ingrese su contraseña: ')
m.validacion(passw)