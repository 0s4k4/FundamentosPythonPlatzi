##CRUD CREATE , READ, UPDATE , DELETE

numbers = [1,2,3,4,5]

print(numbers)

print(numbers[1])

##cambiamos le ultimo elemento 
numbers[-1] = 10

print(numbers) 

numbers.append(799)
##ingresa un nuevo elemento al final de la lista
print(numbers)

numbers.insert(0,'hola') ##inserta donde el primer parametro indica la posicion y el segundo el elemento que se va añadir
print(numbers)

##fusionamos la listas

tasks = ['uno','dos','tres']

nueva_lista = numbers + tasks

print(nueva_lista)

##para saber la posicion en donde donde se encuentra la posicion del str uno
index = nueva_lista.index('uno')

##actualizamos la posicion de la lista print
nueva_lista[index] = 'cuatro'
print(nueva_lista)

##remover una lista

nueva_lista.remove('cuatro') #con el metodo remove le indicamos el parametro y lo eliminamos
print(nueva_lista)


nueva_lista.pop()##elimina la ultima posicion 
print(nueva_lista)

nueva_lista.pop(0) ##elimina el elemento segun la posicion que le indiques 
print(nueva_lista)

nueva_lista.reverse() ##invierte la lista
print(nueva_lista)


numeros = [5,10,2,8,1,30]

numeros.sort() ##ordena de manera ascendente los elementos de la lista
print(numeros)

letras = ['a','z','e']
letras.sort() ##ordena los strings
print(letras)