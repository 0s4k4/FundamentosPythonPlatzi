###creacion de un sistema basico de rpg con python

##creamos dos contadores de vida, el de nuestro personajes y el del enemigo
import sys
import random

vidaEnemigo = 100
vidaProtagonista = 100

print('-----Vas caminando por la hierba-----')
print('-----¿Que es esto?-----')
EntrarEnBatalla = input('¿Deseas entrar en batalla?: 1) Si, 2) no: ')


if (EntrarEnBatalla == '1'):
    
    ##print("Decide lo que vas a hacer:\n\t1) Opción 1.\t2)Opción 2.\n\t3) Opción 3.\t4) Opción 4. ")

    MensajeBienvenida = "Has decidido entrado a una batalla"
    ancho_total = 125 # Ancho total deseado para el resultado

    texto_centralizado_bienvenida = MensajeBienvenida.center(ancho_total)
    print(texto_centralizado_bienvenida)
    
    
    while vidaEnemigo  > 0 and vidaProtagonista > 0:
            
        opcionBatalla = input("Decide lo que vas a hacer:\n\t1) Pelear .\t2)Comer .\n\t3) Escapar.\t4) Mirar. ")
        
        
        if opcionBatalla == '1':
            print('El enemigo a sufrido dañoooo')
            vidaEnemigo = vidaEnemigo - 50
            print(f'el enemigo ahora cuenta con {vidaEnemigo}') 
            
        
        if opcionBatalla == '2':
            print('----nuestro heroe ha comido----')
            vidaProtagonista = vidaProtagonista + 10
            print(f'la vida del heroe ahora es de: {vidaProtagonista} ')
            
        if opcionBatalla == '3':
            print('Has escapado de la batalla...')
            quit()
            
        if opcionBatalla == '4':
            print('te has quedado mirando')
            
        print('ha terminado tu turno')
        print('Ahora le toca al enemigo....')
        print('el decide atacarte')
        dañoEnemigo = random.randint(1, 90)
        vidaProtagonista = vidaProtagonista - dañoEnemigo
        print(f'tu vida actual es de {vidaProtagonista}')
    
else:
    print('has decidido salir de la batalla')
    exit()
    
    
if vidaProtagonista <= 0:
    print('game over')
    print('has muerto')
    
elif vidaEnemigo <= 0:
    print('has ganado')
    print('has derrotado al enemigo')
    