'''
    Crear un programa donde le pases un numero, y te devuelva su tabla de multiplicar
'''

tabla = input('Dime un numero: ')

try: #como el try del try catch
    tabla=int(tabla)
except: #como el catch del try catch
    print('Solo se pueden introducir numeros del 0 al 10...')


if(isinstance(tabla, int)):
    # range() -> Empieza por 0 va sumando hasta el numero que se le indica - 1
    #range(1, 11, 2) -> empieza en 1 y va hasta el 10 de 2 en 2
    #range(0, 11, 1) -> Es igual que va por defecto empieza en 0 y va hasta el 10 de 1 en 1
    for i in range(11):
        print(str(tabla) + ' x ' + str(i) + ' = ' + str((tabla*i)))
