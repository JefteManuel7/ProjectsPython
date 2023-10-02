
# ARCHIVOS EN PYTHON
f = open('Sesion12/lorem.txt')
txt = f.read()
print(txt)
print(type(txt))
f.close()



# los abrimos de nuevo
f = open('Sesion12/lorem.txt')
print(f.read(10))
print(f.read(15))
print(f.read(30))
f.close()

# Lo abrimos de nuevo
f = open('Sesion12/lorem.txt')
line = f.readline()
print(type(line))
print(line)

# Puede ir leyendo linea por linea
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()



#
f = open('Sesion12/lorem.txt')
lines = f.readlines()
print(lines)
f.close()

#
f = open('Sesion12/lorem.txt')
lines = f.read().splitlines()
print(lines)
f.close()

#
file = 'Sesion12/lorem.txt'

with open(file) as f:
    lines = f.read().splitlines()
    print(lines)


# 
file = 'Sesion12/lorem.txt'

# Edtiamos o agregamos informacion
with open(file, 'a') as f:
    f.write('\n Este texto debe ir al final de todo')

# Elimina y agrega la parte que se especifica
with open(file, 'w') as f:
    f.write('\n Este texto debe ir al final de todo')


# da error si ya existe
# creamos un archivo
file2 = 'Sesion12/myfile.txt'
with open(file2, 'x'):
    pass


#

with open('Sesion12/prueba.txt', 'a') as f:
    f.write('texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto')


# Vamos a eliminar un archivo
import os
os.remove('Sesion12/prueba.txt')


# Compruebe si el archivo existe
if os.path.exists('Sesion12/prueba.txt'):
    os.remove('Sesion12/prueba.txt')
else:
    print('El archivo no existe')






try:
    if os.path.exists('Sesion12/prueba.txt'):
        os.remove('Sesion12/prueba.txt')
        print('Archivo eliminado')

    else:
        raise FileNotFoundError('No existe el archivo')
    
except FileNotFoundError as err:
    print(err)

finally:
    print('Fin del programa')



    
# ELIMINAR CARPETAS
os.rmdir('Sesion12/Nueva carpeta')


# crear carpeta
os.mkdir('Sesion12/Prueba')



#--------------------------------------------
datos_dct = {
    'nombre': 'John dane',
    'pais': 'Australia',
    'ciudad': 'Sidney',
    'habilidades': ['Javascrip', 'React', 'Python']
}

datos_jason =  """{
    "nombre": "John dane",
    "pais": "Australia",
    "ciudad": "Sidney",
    "habilidades": ["Javascrip", "React", "Python"]
}"""

print(type(datos_dct), type(datos_jason))

import json
# JSON cambiando json a diccionario
datos_dct = json.loads(datos_jason)

print(datos_dct)




import csv
"""
with open('Sesion12/auto-mpg.csv') as f:
    csv_reader = csv.reader(f, delimiter = " ,")
    line_count = 0
    for fila in csv_reader:
        if line_count == 0:
            print(f'El nombre de la columna es: {" ,".join(csv[fila])}')
            line_count += 1
        else:
            print(f'{fila[0]}')
"""


##
import pandas as pd

data = pd.read_csv('Sesion12/auto-mpg.csv')
print(data)
print(data['horsepower'].mean())
print(data['horsepower'].sum())



"""
import  matplotlib.pyplot as plt
plt.hist(data)
"""


# creando un archivo serializado
import pickle
datos_dict = {'nombre': 'Doe', 'edad': 30}

with open('Sesion12/archivo.pk1', 'wb') as file:
    pickle.dump(datos_dict, file)



with open('archivo.pk1', 'rb') as file:
    datos_info = pickle.load(file)
    print('Los datos: ', datos_info)
    

import csv



alumnos = [
    {'Nombre': 'Doe', 'Nota': 6.0},
    {'Nombre': 'Snow', 'Nota': 9.0},
    {'Nombre': 'Harry', 'Nota': 1.0},

]

with open('Sesion12/registro_alumnos.csv', 'w', newline = '') as file:
    campos = ['Nombre', 'Nota']
    escribir = csv.DictWriter(file, fieldnames = campos)
    escribir.writeheader()
    for alumno in alumnos:
        escribir.writerow(alumno)

with open('Sesion12/registro_alumnos.csv', 'r') as file:
    leer = csv.DictReader(file)
    print('Esto es un registro de alumnos')
    for alumno in leer:
        print(f'El alumno es:  {alumno["Nombre"]} con nota de {alumno["Nota"]}')