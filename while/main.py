### iteracion while


contador = 0  ##definimos un contador o variable de contador


while contador < 20:  ##condicional, si while es menor a 20 se repite
    contador += 1  ###indica que cada vez que entre en el bucle, se va asumar 1
    print(contador) ##imrprime el contador
    if contador == 15: ###si el contador es 15
        print(contador) 
        break ##va a romper la iteracion
    
    
print('contador2')
contador2 = 0
while contador2 < 15:
    contador2 += 1
    if contador2 < 10:
        continue
    
    print(contador2)
    