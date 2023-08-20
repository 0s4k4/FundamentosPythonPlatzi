numero = int(input("Ingresa el numero "))

comprobacionPar = numero % 2


if (comprobacionPar == 0):
    print (f"El numero {numero} es par")
    
else:
    print(f"el numero {numero} no es par ")