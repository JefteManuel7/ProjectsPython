# HERENCIA Y POLIMORFISMO EN PYTHON

class Person:
    
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname 
        
    def printname(self):
        print(self.fname, self.lname)

persona_1 = Person('John', 'Snow') 
persona_1.printname()


class Student(Person):
    def __init__(self, fname, lname): 
        #Person.__init__(self.fname, self.lname) Primer opción
        super().__init__(fname, lname) #Segunda opción

student_1 = Student('Albert', 'Einstein')
student_1.printname()
#------------------------------------------------

#CLASE PRINCIPAL
#CLASE PRINCIPAL
class Person:
    
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname 
        
    def printname(self):
        print(self.fname, self.lname)

# Agregar propiedades a la clase heredada
class Student(Person):
    def __init__(self, fname, lname, year): 
        #Person.__init__(self.fname, self.lname) Primer opción
        super().__init__(fname, lname) #Segunda opción
        self.graduationyear = year
    
    def Welcome(self):
        print('Bienvenido', self.fname, self.lname, 'a la clase del', self.graduationyear)


studen_1 = Student('Mike', 'Tyson', 2009)
studen_1.Welcome()



# Crear una clase animal y luego de la clase anima, crear una clase que herede las propiedades de la clase animal
class AnimaL:
    def __init__(self, name, nfeet, raza):
        self.name = name 
        self.nfeet = nfeet
        self.raza = raza
    

class Cat(AnimaL):
    def __init__(self, name, nfeet, raza):
        super().__init__(name, nfeet, raza)


cat = Cat('Minino', 4, 'Angora')
print('El nombre del gato es: ', cat.name)
print('El numero de patas es: ', cat.nfeet)
print('La raza del gato es: ', cat.raza, '\n')


class Dog(AnimaL):
    def __init__(self, name, nfeet, raza):
        super().__init__(name, nfeet, raza)

perrito = Dog('Scott', 4, 'Labrador')

print('El nombre del perro es: ', perrito.name)
print('El numero de patas es: ', perrito.nfeet)
print('La raza del perro es: ', perrito.raza)




# El POLIMORFISMO-----------------------------------
# Polinorfismo en funciones

x = 'Hola Mundo'
print(len(x))

myTuple = ('cat', 'dog', 'fish', 'horse')
print(len(myTuple))


mydict = {
    'Nombre': 'John',
    'Apellido': 'Doe'
}
print(len(mydict), '\n')

#------------------------------------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('A conducir!')
    
    
    def nomove(self):
        print('No se movio')

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    

    def move(self):
        print('A navegar!')

    
    def nomove(self):
        print('No se movio')


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('A volar!')

    def nomove(self):
        print('No se movio')


carro_1 = Car('Tojota', 'gorrola')
bote_1 = Boat('Bavaria', 'Yachts')
avion_1 = Plane('Boeng', 'AirBus')
        


for it in (carro_1, bote_1, avion_1):
    it.move()

for it in (carro_1, bote_1, avion_1):
    it.nomove()

        
# Polimorfismo para la clase Herencia
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model 
        self.year = year

    def moves(self):
        print('A conducir!')


class Car(Vehicle):
    pass

class Boat(Vehicle):
    def moves(self):
        print('A navegar!')

class Plane(Vehicle):
    def moves(self):
        print('A volar')


carro_1 = Car('Tojota', 'gorrola', 2009)
bote_1 = Boat('Bavaria', 'Yachts', 2010)
avion_1 = Plane('Boeng', 'AirBus', 2011)


for it in (carro_1, bote_1, avion_1):
    print(it.brand)
    print(it.model)
    it.moves()
