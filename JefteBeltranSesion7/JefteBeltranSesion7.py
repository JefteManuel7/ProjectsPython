# Listas
thisList = ['apple', 'banan', 'watermelon', 'cherry']
print(len(thisList))
print(thisList, '\n')


vegetalesLst = ['Tomate', 'Papa', 'Coliflor', 'Zanahoria', 'Cebolla']
print(len(vegetalesLst))
print(vegetalesLst[1], '\n')


paises = [
    'El Salvador', 'Guatemala', 'Costa Rica', 'Panama', 'Honduras',
    'Nicaragua', 'Belice'
]
print(len(paises))
print(paises, '\n')


listas = [3, 4, 5, 6, 7, 8, 8, 9, 9]
print(listas)
print(len(listas), '\n')

# AGREAGANDO DATOS A UNA LISTA CON EL METODO APPEND()-------------------------------------------------------------------------
thisList = ['apple', 'banan', 'watermelon', 'cherry']
thisList.append('Orange')
thisList.append('Piña')
thisList.append('Melon')
print(thisList)


emptyList = []
print(emptyList)
emptyList.append('vacio1')
print(emptyList)
emptyList.append('ya no esta vacia')
print(emptyList, '\n')


# PODEMOS AGREGAR DATOS DIFERENTES EN UNA LISTA
list4 = [1, 2, 3, 4, 'Hola', True]
print(list4)
print(type(list4[0]))
print(type(list4[1]))
print(type(list4[2]))
print(type(list4[3]))
print(type(list4[4]))
print(type(list4[5]), '\n')




list5 = [
    'Juan', 350, True, {'Pais': 'El Salvador', 'Ciudad': 'San Salvador'},
    [1, 2, 3, 4]
]
print(list5, '\n')

print(len(list5))
print(list5[4])
print(type(list5[4]), '\n')

print(list5[3])
print(type(list5[3]), '\n')


list5.append(23)
list5.append('Hola Mundo')
list5.append(False)

print(list5, '\n')


# CREANDO UNA LISTA A PARTIR DE OTRA
lstNew = [list5[0], list5[1], list5[2], list5[5]]
indiceFinal = len(lstNew)-1
print(indiceFinal)

print(lstNew[3], '\n')



# ACCESANDO A UNA LISTA, CON INDICE NEGATIVO
frutas = ['Papaya', 'Jocote', 'Pina', 'Melon', 'Sandia']
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])
print(frutas[-4], '\n')


# DESEMPACANDO ELEMENTOS DE UNA LISTA
frutas = ['Papaya', 'Jocote', 'Pina', 'Melon', 'Sandia']

fruta1, fruta2, *sobran = frutas

print(fruta1)
print(fruta2)
print(sobran)

#

numTest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

n1, n2, *nvarios, nPenultimo, nUltimo = numTest
print(n1)
print(n2)
print(nvarios)
print(nPenultimo)
print(nUltimo, '\n')

#
numTest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
nInicio, *nCentrales, nUltimo = numTest
print(nInicio)  
print(nCentrales)
print(nUltimo, '\n')


# TRABAJANDO CON LA LISTA NUMEROS

numTest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
nInicio, *nCentrales, nUltimo = numTest
print(nInicio)  

nCentral = []

# CONVIRTIENDO LOS DATOS A ENTEROS, YA QUE ERAN STRINGS
for num in nCentrales:
    nCentral.append(num)
print(nCentral)
print(nCentrales,'\n')

print(nUltimo, '\n')



# TRABJANDO CON LA LISTA FRUTAS
frutas = ['papaya', 'jocote', 'pina', 'melon', 'sandia']
print(len(frutas))
print(frutas[::2])
print(frutas[::-1]) #invirtiendo la cadena

todoFrutas = frutas[0:5]
print(todoFrutas, '\n')

pruebaFrutas = frutas[0:]
print(pruebaFrutas, '\n')

slice1 = frutas[1:3]
print(slice1)
slice2 = frutas[2:4]
print(slice2)

# OTRO EJERCICIO CON UNA LISTA DE FRUTAS
frutas = ['papaya', 'jocote', 'pina', 'guineo', 'melon', 'sandia']
print(frutas[3])

# EDITANDO EL VALOR DE GUIENO
frutas[3] = 'fresas'
print(frutas[3], '\n')



# AGREGAR ELEMENTOS A UNA LISTA EN CUALQUIER POSICION
frutas = ["manzana", "plátano", "naranja", "uva", "sandía",
           "pera", "kiwi","fresa", "piña", "mango", "melón", 
           "frambuesa", "cereza", "papaya","limón", "granada", 
           "mandarina", "coco", "ciruela", "melocotón", 'naranja'
            ]

print('melon' in frutas) #BUSCANDO ELEMENTOS EN UNA LISTA
print('papaya' in frutas)

for fruta in frutas:
    if fruta == 'papaya':
        print('Si hay')
    else:
        print('No hay')



# USANDO LA FUNCION INSERT, EL CUAL INSERTA ELEMENTOS EN UNA LISTA EN DETERMINADO LUGAR
frutas = ["manzana", "plátano", "naranja", "uva", "sandía", "pera", "kiwi", 
          "fresa", "piña", "mango", "melón", "frambuesa", "cereza", "papaya", 
          "limón", "granada", "mandarina", "coco", "ciruela", "melocotón"]

frutas.insert(3, 'jocote')
print('jocote' in frutas)
print(frutas, '\n')

frutas.insert(6, 'guineo')
print(frutas, '\n')

# ELIMINAR ELEMENTOS DE UNA LISTA CON EL METODO REMOVE()
frutas.remove('guineo')
print('guineo' in frutas)
print(frutas)



frutas = ["manzana", "plátano", "naranja", "uva", "sandía",
           "pera", "kiwi", "fresa", "piña", "mango", "melón", 
           "frambuesa", "cereza", "papaya", "limón", "granada", 
           "mandarina", "coco", "ciruela", "melocotón"]


# ELIMINAR ELEMENTOS DE UNA LISTA CON EL METODO POP() USANDO UN INDICE ESPECIFICO(UBICACION EN LA LISTA)
#frutas.pop() # si se deja en blanco, automaticamente elimina el ultimo elemento
print(len(frutas))
frutas.pop(19)
print('melocoton' in frutas)



frutas = ["manzana", "plátano", "naranja", "uva", "sandía", 
          "pera", "kiwi", "fresa", "piña", "mango", "melón", 
          "frambuesa", "cereza", "papaya", "limón", "granada", 
          "mandarina", "coco", "ciruela", "melocotón"]


# USANDO EL METODO DELETE PARA ELIMINAR DATOS DE UNA LISTA, SE USA PARA ELIMINAR DATOS, GRUPOS ESPECIFICOS
# SI NO INDICAMOS UN INDICE, ELIMINAR LA LISTA ENTERA
# del list[index]
# del list
# del list[a:b]

del frutas[0]
print('manzana' in frutas)


del frutas[4:9] #eliminando el grupo
print(frutas)

del frutas
print(frutas, '\n')


# LIMPIAR ITEMS DE LISTAS, USANDO EL METODO CLEAR(), EL CUAL LIMPIA ELEMENTOS DE UNA LISTA
"""
SINTAXIS:
list.clear()

"""

paisesCentroamerica = ['El Salvador', 'Costa Rica', 'Honduras', 'Panama', 'Guatemala']
paisesCentroamerica.clear() #elimina los datos, pero no a la lista
print(paisesCentroamerica, '\n')




# COMO COPIAR UNA LISTA
"""
SINTAXIS:
listNew = list.copy()
"""
paises_norteamerica = [
    "Estados Unidos",
    "Canadá",
    "México"
]
newPaises = paises_norteamerica.copy()
print(newPaises, '\n')





# UNIR LISTAS
paises_norteamerica = [
    "Estados Unidos",
    "Canadá",
    "México"
]

paises_centroamerica = [
    "Belice",
    "Costa Rica",
    "El Salvador",
    "Guatemala",
    "Honduras",
    "Nicaragua",
    "Panamá"
]

casiAmerica = paises_norteamerica + paises_centroamerica
print(casiAmerica, '\n')




# UTILIZANDO EL METODO EXTEND(), PARA UNIR LISTAS
"""
list1.extend(list2)

"""
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = ['a', 'b', 'c']
lista1.extend(lista2)
print(lista1, '\n')


#CONTANDO ELEMENTOS DE UNA LISTA
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = ['a', 'b', 'c']
lista1.extend(lista2)
lista1.append(1)
print(lista1, '\n')
lista1.count(1)

# BUSCAR ELEMENTOS EN UNA LISTA
lista1 = [1, 2, 3, 4, 5, 6]
print(lista1.index(3), '\n')

# EL METODO REVERSE, INVIERTE LAS LISTAS
lista1.reverse()
print(lista1)


# ORDENAR ELEMENTOS DE UNA LISTA, CON EL METODO SORT()
frutas2 = ['banana', 'mango', 'limon', 'sandia']
frutas2.sort()
print(frutas2)


# METODO SORTED(), NO ALTERA LA LISTA
edades = [22, 19, 25, 24, 25, 24]
print(sorted(edades, reverse = True), '\n')



# EMPEZAMOS A TRABAJAR CON UNA TUPLA---------------------------------------------------------------------------------------
thisTuple = ('banana', 'sandia', 'limon')
print(thisTuple)

emptyTuple = ()
print(emptyTuple)



#
frutastTupla = ("manzana", "plátano", "naranja", "uva", "sandía", "pera", "kiwi", "fresa", "piña", "mango")
print(frutastTupla)

print(frutastTupla[0])
print(frutastTupla[-1])
print(frutastTupla[-6])

frutastTupla[0] = 'mango' #no se puede modificar
print('\n')


# HACIENDOO SLICING EN TUPLAS
frutasTupla = ("manzana", "plátano", "naranja", "uva", "sandía", "pera", "kiwi", "fresa", "piña", "mango")

tpl1 = frutasTupla[0:4]
print(tpl1)
tpl2 = frutasTupla[2:8]
print(tpl2, '\n')


#CONVERTIR TUPLA A LISTAS
lst2tp1 = list(tpl2)
print(type(lst2tp1))
print(lst2tp1)
lst2tp1.append('coco')
tpl3 = tuple(lst2tp1)
print(tpl3, '\n')



# BUSQUEDAS EN TUPLAS
frutas = ('mango', 'fresa', 'sandia')
print('fresa' in frutas)


# SE PUEDEN UNIR TUPLAS
tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = ('a', 'b', 'c')
tupleResult = tuple1 + tuple2
print(tupleResult)

# BORRAR TUPLAS
del tupleResult
print(tupleResult, '\n') # dara error, ya que la eliminar






# CONJUNTOS DE DATOS: SET
thisSet = {'apple', 'banana', 'cherry'}
print(thisSet)
#son inmutables, no puede contener valores duplicados y no estan ordenados

setT1 = {1, 2, 3, 4, 5, 6, 1, 3,4, 5} #no toma valores duplicados
print(setT1, '\n')

# PARA ACCESAR A LOS ELEMENTOS EN SET:
thisSet = {'apple', 'banana', 'cherry'}
print('apple' in thisSet)


for fruit in thisSet:
    print(thisSet)

#   AGREGAR ELEMENTOS EN LOS 'SET', USANDO EL METODO ADD()
# SI DESEA AGREGAR VARIOS ELEMENTOS, SE UTILIZAR UPDATE(item1, item2, item3)
setT1.add('piña')
print(setT1)

setT2 = {'melon'}
setT2.update('naranja', 'melocoton', 'jocote')
print(setT2, '\n')


#ELIMINAR ELEMENTOS EN SET, UTILIZANDO REMOVE(), POP()
frutas = {"manzana", "banana", "naranja", "uva", "pera"}
frutas.pop() #eliminar datos ramdoms
print(frutas)

frutas.remove('banana') #elimina especificamente
print(frutas)

frutas.clear() #limpia, no borra el set, solo los elementos
print(frutas)
print()


# UNION DE CONJUNTOS
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8, 9}

set3 = set1.union(set2)
print(set3, '\n')


listaSet = [1, 2, 3, 4, 5, 't', 'y', 'r', 'r']
setConvert = set(listaSet) #no toma valores duplicados
print(setConvert, '\n')


# INTERSECCION DE CONJUNTOS
set1 = {1, 2, 3, 4}
set2 = {2, 5, 6, 7, 8, 9}

set3 = set1.intersection(set2)
print(set3)


# DIFERENCIA SEMETRICA EN CONJUNTOS
set3 = set1.symmetric_difference(set2)
print(set3, '\n')


# DICCIONARIOS-------------------------------------------------------------------------------------------------------- 
myfamily = {
    "childl" : {
    "name" : "Emil",
    "year": 2004
    },
    "child2" : {
    "name" : "Tobias",
    "year" : 2007
    },
    "child3" : {
    "name" : "Linus",
    "year" : 2011
    }
}

#print(myfamily)
#print(len(myfamily))

myfamily['childl'] = 'Jefte'
myfamily['year'] = 2002
print(myfamily)


# ELIMINAR DATOS EN DICCIONARIOS
#person.pop('adress')
#person.popitem() borra el ultimo elemento que se ingreso al diccionario
# del person  elimina todo el diccionario
