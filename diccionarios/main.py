##diccionarios en python



mi_diccionario_pokemon = {
    
    'nombre': 'Dragonite',
    'tipo': 'Volador/Dragon',
    'nivel': 70,
    'pokeball': 'master ball'
}

##nos imprime un elemento de un diccionario
print(mi_diccionario_pokemon['nombre'])

##la cantidad de elementos en un diccionario
print(len(mi_diccionario_pokemon))
##con la funcion get si no existe el valor sale un mensaje
print(mi_diccionario_pokemon.get('region'))

##comprueba si existe la llave en el diccionario
print('nivel' in mi_diccionario_pokemon)