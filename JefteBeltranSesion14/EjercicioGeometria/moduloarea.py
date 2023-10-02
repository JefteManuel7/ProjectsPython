import math
# clase principal para calcular areas de figuras geometricas
class Figure:
    def Calcular_area(self):
        pass

#clase para calcular el area de un cuadrado
class Cuadrado(Figure):
    def __init__(self, lado):
        self.lado = lado


    def Calcular_area(self):
        return self.lado * self.lado
        

    
# clase para calcular el area de un rectangulo
class Rectangule(Figure):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def Calcular_area(self):
        return self.base * self.altura
    

# clase para calcular el area de un triangulo
class Triangule(Figure):
    def __init__(self, base, altura):
        self.base = base
        self.altua = altura

    def Calcular_area(self): 
        return self.base * self.altua / 2


# clase para calcular el area de un circulo
class Circule(Figure):
    def __init__(self, radio):
        self.radio = radio

    def Calcular_area(self):
        return math.pi * self.radio
