###Un programa de inicio de sesion donde el nivel de usuario sea 
# A me envie al dasbhboard de admin y si es usuario al ui de usuario normal


## s = admin
## u == user

nombre = input('ingresa el usuario: ')
nivel = input('ingresa en nivel del  usuario: ')



if nivel == 's' or nivel == 'u':
    print('---------------------------------------------------')
    print('|                                                  |')
    print('|                                                  |')
    print('|                                                  |')
    print('|                                                  |')
    print('|                                                  |')
    print('|                                                  |')
    print(f'|       Bienvenido al sistema {nombre}                |')
    print('|                                                  |')
    print('|                                                  |')
    print('|                                                  |')
    print('|                                                  |')
    print('|                                                  |')
    print('---------------------------------------------------')
    
else:
    print('acceso no autorizado')