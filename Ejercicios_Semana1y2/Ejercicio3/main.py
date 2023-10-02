import Modulo as m

num = int(input('Adivina el número: '))

while True:
    if num == m.adivinanumero(num):
        print('¡Adivinaste!')
        break
    else:
        print('Te equivocaste')
        num = int(input('Intenta de nuevo: '))


        