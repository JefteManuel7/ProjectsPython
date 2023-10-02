

import  moduloarea as ma

cuadrado =ma.Cuadrado(4)
print(f'El are de un cuadrado es: ', cuadrado.Calcular_area())


rectangulo = ma.Rectangule(5, 4)
print(f'El area de un rectangulo es: ', rectangulo.Calcular_area())


triangulo = ma.Triangule(5, 4)
print(f'El area de un triangulo es: ', triangulo.Calcular_area())


circulo = ma.Circule(4)
print(f'El area de un circulo es:  {circulo.Calcular_area() : .2f}')