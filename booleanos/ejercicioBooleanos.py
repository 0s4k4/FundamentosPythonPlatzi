###comparaciones para saber si x es mayor, menor o igual a y


x = int(input("Cuanto es el valor de x: "))

y = int(input("Cuanto es el valor de y: "))


esMayor = x > y
esMenor = x < y
esIgual = x == y

print(f'x({x}) es mayor a y({y}): {esMayor}')
print(f"x({x}) es menor a y({y}): {esMenor}")
print(f" x({x}) es igual a y{y}: {esIgual}") 