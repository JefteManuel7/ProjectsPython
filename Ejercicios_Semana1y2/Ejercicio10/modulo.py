def adivina_La_Palabra(letter):
    adivinar = 'museo'
    palabra_oculta = '_' * len(adivinar)
    print('La palabra es:', palabra_oculta)
    
    palabra_descubierta = list(palabra_oculta)  # Convertir en lista para modificar
    acertado = False

    while not acertado:
        if letter in adivinar:
            for i, char in enumerate(adivinar):
                if char == letter:
                    palabra_descubierta[i] = letter

            palabra_oculta = ''.join(palabra_descubierta)
            print(palabra_oculta)
            
            if palabra_oculta == adivinar:
                acertado = True
                print('Correcto, la palabra es:', adivinar)
                
        else:
            print('Incorrecto, vuelve a intentarlo.')
        letter = input('Ingrese una letra: ')


