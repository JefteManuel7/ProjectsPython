
def validacion(passw):
    longitud = len(passw)
    if longitud >= 8:
        numbers = False
        letter = False
        number = list(range(1, 101))
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                                    'o', 'p', 'q', 'r', 's', 't', 'u', 
                                    'v', 'w', 'x', 'y', 'z']
        for iterador in passw:
            if number in passw:
                numbers = True
            if letters in passw:
                letter = True


        
        if numbers and letter == True:
            print('Validacion exitosa')
        else:
            print('Contraseña incorrecta: debe contener al menos una letra y un número')
        
                    
    else:
        print('Contraseña incorrecta')
            
