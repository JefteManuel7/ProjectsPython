
# -------------------------------------------MODULOS BUILT IN PYTHON----------------------------------------------------------
import math
raiz = math.sqrt(4)
print('La raiz cuadra es: ', raiz, '\n')

print(math.pi, '\n')

print(math.log10(20), '\n')


# OTRA FORMA DE LLAMAR A LOS MODULOS
from math import pi, e, sqrt, pow


from statistics import* 
# media
ages = [30, 50, 60, 20, 10, 40]
print(mean(ages), '\n')

#
print(stdev(ages), '\n')


# RAMDOM
from random import random, randint
print(random())
print(randint(1, 9), '\n')


#-----------------------------------------
import Librarys.MyModule as MyModule
print(MyModule.sumar(4, 5), '\n')


#-----------------------------------------
print('El resultado es: ', MyModule.restar(5, 9), '\n')


# PODEMOS USAR ALIAS
import Librarys.areas as ar
print('El resultado es: ', ar.area_rectangulo(12, 5))



import Librarys.MixModulo as mx
archivo = "Power.csv"
cargar_datos = mx.cargar_datos(archivo)
print(cargar_datos.head(), '\n')


lst = [1, 2, 3, 4, 5]
prom = mx.calcular_promedio(lst)
print('El promedio es: ', prom, '\n')