
##libreria random
import random
##creamos una lista con las opciones del juego
opciones = ['piedra','papel','tijera']

opciones_aleatorias = random.sample(opciones, 1)

opciones_aleatorias_str = ' '.join(map(str, opciones_aleatorias))

opcion_usuario = input('Ingresa piedra, papel o tijera: ')

print('usuario selecciono: '+opcion_usuario)
print('computadora selecciono: '+opciones_aleatorias_str)


if opciones_aleatorias_str == opcion_usuario:
    print('A sido un empate')
elif opcion_usuario == 'piedra':
    if opciones_aleatorias_str == 'tijera':
        print('Piedra le gana ')
        print('Usted gano')
    else:
        print('papel le gana')
        print('computadora gano')
elif opcion_usuario == 'papel':
    if opciones_aleatorias_str == 'piedra':
        print('Papel gana  a piedra')
        print('usuario gano')
    else:
        print('tijera gana a papel')
        print("computadora gano")
        
elif opcion_usuario == 'tijera':
    if opciones_aleatorias_str == 'papel':
        print("tijera  gana a papel")
        print("usuario gano")
    else:
        print("piedra gana a tijera")
        print("computadora gano")