###opciones de tuplas 
import random 
opciones = ('piedra','papel','tijera')

opcion_usuario = input('Ingresa una opcion, piedra,papel o tijera: ')
opcion_usuario = opcion_usuario.lower()

opcion_computadora = random.choice(opciones)

if not opcion_usuario in opciones:
    print ('esa opcion no es valida')
    quit()
    
print('Opcioon seleccionada del usuario: '+opcion_usuario)
print('Opcoon seleccionada por la computadora: '+ opcion_computadora)




if opcion_computadora == opcion_usuario:
    print('empate')

if opcion_usuario == 'piedra':
    if opcion_computadora == 'papel':
        print('Perdiste, el papel es debil a la pidra')
        print('Perdiste')
if opcion_usuario == 'piedra':
    if opcion_computadora == 'tijera':
        print('Ganaste, la piedra le gana la tijera')
        print('Ganaste')
if opcion_usuario == 'papel':
    if opcion_computadora == 'piedra':
        print('Ganaste, el papel le gana a la piedra')
        print('Ganaste')
if opcion_usuario == 'papel':
    if opcion_computadora == 'tijera':
        print('Perdiste, el papel es debil contra la tijera')
        print('Ganaste')

if opcion_usuario == 'tijera':
    if opcion_computadora == 'papel':
        print('Ganaste, la tijera es fuerte contra el papel')
        print('Ganaste')
if opcion_usuario == 'tijera':
    if opcion_computadora == 'piedra':
        print('Perdiste, la tijera es debil contra la piedra')
        print('Perdiste')
        