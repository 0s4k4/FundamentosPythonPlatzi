##operaciones con diccionarios

persona = {
    'nombre':'Jorge',
    'apellido':'piña',
    'lenguajes':['python','C#'],
    'edad': 25
}


print(persona)

##actualizamos el nombre 
persona['nombre'] = 'luis'
print(persona)

persona['edad'] -= 5
print(persona)

persona['lenguajes'].append('php')
print(persona)


##eliminar elemento

persona.pop("edad")
print(persona)


##imprime todas las llaves depython
print(persona.keys())

##imprime todos los valores
print(persona.values())

##crea una una lista que contiene por tupla los keys y valores correpondientes
print(persona.items())


