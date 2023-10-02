# CLASES EN PYTHON
class Myclass:
    x = 5
    y = 10.1
    z = 'Hola, estoy dentro de una clase'


objeto_1 = Myclass()
print(objeto_1.z)

# FUNCION _init_()

# ejemplo crear una clase llamada persona y que asignemos nombre y edad
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person('John', 23)
person2 = Person('Mara', 36)

print(person1.name)


# cambiando self por p
class Person:
    def __init__(P, name, age):
        P.name = name
        P.age = age


person1 = Person('John', 23)
person2 = Person('Mara', 36)


# FUNCION _str_()
class Person:
    def __init__(self, name, age):
        self    .name = name
        self.age = age

    def __str__(self):
        return f'{self.name} has {self.age} year old'

person_1 = Person('John', 36)
print(person_1)




#
class Person:
    def __init__(self, name, age):
        self    .name = name
        self.age = age

    def __str__(self):
        return f'{self.name} has {self.age} year old'
    
    def Myfunc(self):
        print(f'Hello my name is {self.name}')



person_1 = Person('John', 36)

person_1.Myfunc()



#--------------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    def __str__(self):
        return f'Nombre: {self.name}, Edad: {self.age}'
        
    def add_skills(self, skill):
        self.skills.append(skill)

# Crear una instancia de la clase persona
person_1 = Person('John', 34, )

# Agregar habilidades a la instancia
person_1.add_skills('Python')

lst = ['SQL', 'Java', 'Javascript', 'PHP']
for skill  in lst:
    person_1.add_skills(skill)

    
# Obtener la informacion
print(person_1)
print('Habilidades: ', person_1.skills)



# cambiando a get_info-----------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    def get_info(self):
        return f'Nombre: {self.name}, Edad: {self.age}'
        
    def add_skills(self, skill):
        self.skills.append(skill)

# Crear una instancia de la clase persona
person_1 = Person('John', 34, )

# Agregar habilidades a la instancia
person_1.add_skills('Python')

lst = ['SQL', 'Java', 'Javascript', 'PHP']
for skill  in lst:
    person_1.add_skills(skill)


# Obtener la informacion
print(person_1.get_info())
print('Habilidades: ', person_1.skills)





# cambiando a get_info---------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    def get_info(self):
        return f'Nombre: {self.name}, Edad: {self.age}'
        
    def add_skills(self, skill):
        self.skills.append(skill)

# Crear una instancia de la clase persona
person_1 = Person('John', 34, )

# Agregar habilidades a la instancia
person_1.add_skills('Python')

lst = ['SQL', 'Java', 'Javascript', 'PHP']
for skill  in lst:
    person_1.add_skills(skill)


# Obtener la informacion
print(person_1.get_info())
print('Habilidades: ', person_1.skills)



# cambiando la edad
person_1.age = 25
print(person_1.get_info())

person_1.name = 'John Connor'
print(person_1.get_info())



# eliminar propiedades de una clase
del person_1.age
print(person_1.get_info())
print(person_1.age)


# Eliminar person_1
#del person_1
#print(person_1)


# EJEMPLO CLASE CARRO
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


# Instanciando la clase Car y creando un objeto 
carro = Car('tollota', 'korrola', '2023')
print(f'Descripción del Carro: {carro.brand}, {carro.model}, {carro.year}')



# EJEMPLO CLASE ESTUDIANTE
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def __str__(self):
        return f'{self.name}, {self.age}'
    
    def add_grade(self, grade):
        self.grades.append(grade)

    def print_info(self):
        print(f'El nombre del estudiante: {self.name}, Edad: {self.age} y sus calificaciones son: {self.grades}')
        
# instanciando la clase
estudiante = Student('Jefte', 21)

print(estudiante)

estudiante.add_grade(10)
estudiante.add_grade(5)
estudiante.add_grade(7)
estudiante.add_grade(8)
estudiante.add_grade(9)

print(estudiante.print_info())




# EJERCICIO 3: clase circulo

import math

class Circule():
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
# instanciando la clase
circulo = Circule(3)
print(f'El perimetro es: {circulo.calculate_perimeter() : .2f}') 
print(f'El area es: {circulo.calculate_area() : .2f}')       



# EJERCICIO 4: Clase libro

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f'El titulo es: {self.title}, Autor: {self.author}, Año de publicación: {self.year}')

libro = Book('La Selva', 'Jefte', '2020')
print(libro.get_info())



# EJERCICIO 5: Clase Banco

class Bank:
    def __init__(self):
        self.accounts = {}

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]+= amount
        else:
            self.accounts[account_number]= amount


    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number]-= amount
            else:
                print('fondos insuficientes')

        else:
            print('Cuenta no encontrada o invalidad')
        

    def get_balance(self, account_number):
        return self.accounts.get(account_number, 0  )
        

banco = Bank()

(banco.deposit('C0007', 200))

#print(banco.get_balance('C0007'))

#print(banco.withdraw('C0007', 5000))


banco.deposit('C006', 500)
print(banco.get_balance('C006'))