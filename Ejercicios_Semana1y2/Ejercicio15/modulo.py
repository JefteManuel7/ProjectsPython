
import random

dictionary = {
    'animal': 'leon',
    'objeto': 'carro',
    'dinosaurio': 't-rex',
    'nombre': 'rogelio',
    'pais': 'canada'
}

def palabra_aleatoria():
    return dictionary[random.choice(list(dictionary.keys()))]

def pista(result):
    pista = input('¿Desea que le demos una pista? (si/no): ')
    if pista.lower() == 'si':
        if result == dictionary['animal']:
            return 'Es un animal'
        elif result == dictionary['objeto']:
            return 'Es un objeto'
        elif result == dictionary['dinosaurio']:
            return 'Es un dinosaurio'
        elif result == dictionary['nombre']:
            return 'Es un nombre'
        elif result == dictionary['pais']:
            return 'País'
    return ''

def adivinar(palabra, pista_palabra):
    intentos_maximos = 5
    print('\n', 12*'-',' JUEGO AHORCADO', 12*'-', '\n')
    for _ in range(intentos_maximos):
        play = input('¿Desea jugar? (si/no): ')
        if play.lower() == 'si':
            print(pista_palabra)
            palabra_adivinar = input('Ingrese su adivinanza: \n')
            if palabra_adivinar != palabra:
                intentos_maximos -= 1
                print('Ups, te equivocaste')
                print('Te quedan:', intentos_maximos, 'intentos\n')
            else:
                print('¡Felicidades! Acertaste la palabra: \n', palabra)
                break
        else:
            print('Gracias por jugar.')
            break
    else:
        print('¡Agotaste tus intentos! La palabra era:', palabra)
