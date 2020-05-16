'''
    Escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo

    *
    **
    ***
    ****
    *****
'''

lon = input('Elije el tamaño del arbol: ')

try:
    lon=int(lon)
except:
    print('solo se pueden poner numeros')

for i in range(lon):
    print('*' * (i + 1))