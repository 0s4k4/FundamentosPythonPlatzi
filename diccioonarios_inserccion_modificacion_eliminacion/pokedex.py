####

nombre = input('ingresa el nombre del pokemon: ')
tipos = input('introduce el tipo o tipos, si es mas de  uno lo separas por comas: ')
tipos = tipos.split(",")#se crea la lista con delimintador
lugarDeCaptura = input('introduce el lugar donde lo capturaste: ')

##se crea el diccionarios con los datos

datos = {
    'nombre': nombre,
    'tipos':tipos,
    'lugar de captura':lugarDeCaptura
}

print(datos)


##metodos

print(datos.keys())##muestra las llaves
print(datos.items()) ##muestra en tuplas los conjuntos de llave.valor
print(datos.values()) ##muestra solo los valores

