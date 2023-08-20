##programa para login, si el username y la password son correctas nos autoriza, sino nos denega el acessor


usuario = input('Ingresa tu usuario: ')
contraseña = input("Ingresa tu contrasela: ")



user = 'vegetta777'
password = '1234'

if usuario == user and password == contraseña:
    print('Login correcto')
    print("Disfruta de la red social :)")
    
else:
    print('Acceso denegado')