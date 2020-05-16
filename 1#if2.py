'''
    EScribit un programa para una empresa que tiene salas de jeugos para todas las edades y quiere calcularde forma automatica el
    precio que debe cobrar a sus clientres por entrar. EL programa debe preguntaral usuariola edad del cliente y mostrar el precio
    de la entrada. SI el cliente es menos de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de
    18 años, 10€
'''

edad = input('Introduce tu edad: ')
edad = int(edad)

if edad < 4:
    print('El precio de la entrada es de 0€')
elif edad >= 4 and edad <= 18:
    print('El precio de la entrada es de 5€')
else:
    print('El precio de la entrada es de 10€')

if edad < 4:
    print('El precio de la entrada es de 0€')
elif 4 <= edad <= 18:
    print('El precio de la entrada es de 5€')
else:
    print('El precio de la entrada es de 10€')
