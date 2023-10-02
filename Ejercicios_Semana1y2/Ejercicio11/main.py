

dictionary = {
        '1-Nombre la capital de EE.UU?':'washington',
        '2-El nombre del pais mas grande del mundo?':'Rusia',
        '3-El pais con mayor poblacion en el mundo?':'China'
    }

for pregunta, respuesta_correcta in dictionary.items():
    print(pregunta, '\n')
    respuesta_ingresada = input('Ingrese su respuesta: ')

    if respuesta_ingresada.lower() == respuesta_correcta.lower():
        print('Respuesta correcta', '\n')
    else:
        print(f'Incorrecto. La respuesta correcta es: {respuesta_correcta}', '\n')