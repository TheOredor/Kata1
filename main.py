'''
    Esto es un comentarioo en bloque
    que comenta varias lineas desde el principio 
    hasta el final
'''
#Esto es un comentario en linea

variableString1 = 'esto es una variable de string'
variableString2 = "esto es una variable de string"

variableNumerica = '25'
variableNumerica = int(variableNumerica) + 5

variableBoolean = True
variableBoolean = False

print('imprime por pantalla')
dato = input('Introduce un dato: ')
print(dato)

print('La variable de prueba contiene: ' + prueba)

if (variableNumerica == 30):
    prueba = 'variable de prueba'
    print('La variable numerica es igual que 30: ' + str(variableNumerica))
elif (variableNumerica > 30)):
    print('La variable numerica es menor que 30: ' + str(variableNumerica))
else:
    print('La variable numerica es mayor que 30: ' + str(variableNumerica))

for i in range(11):
    print(i)

while True:
    print('bucle infinito')

break  #Rompe el bucle
continue #salta el resto del ciclo del buble y continua desde el inicio del siguiente ciclo