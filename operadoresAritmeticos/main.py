##crear una calculadora para los diferentes tipos de operaciones artimeticas que hay

print("Hola bienvenido, esta es una calculadora")
numero1 = int(input("Introduce el valor del primer numero de la operacion: "))
numero2 = int(input("Introduce el valor del segundo numero de la operacion: "))
operacion = input("Ahora que seleccionaste los dos numeros, indicame cual tipo de operacion deseas hacer: 1) suma 2) resta 3) multiplicacion 4) divison 5) modulo 6)divison de valor entero 7) Exponente ")



if operacion == '1':
    resultado = numero1 + numero2
    print(f'el resultado es {resultado}')
    
if operacion == '2':
    resultado = numero1 - numero2
    print(f'el resultado es {resultado}')
    
if operacion == '3':
    resultado = numero1 * numero2
    print(f"El resultado es {resultado}")
    
if operacion == '4':
    resultado = numero1 / numero2
    print(f"el resultado es de {resultado}")
    
if operacion == '5':
    resultado == numero1 % numero2
    print(f"El resultado es de {resultado}")
    
if operacion == '6':
    resultado = numero1 // numero2
    print(f"El resultado es {resultado}")
    
if operacion == '7':
    resultado = numero1 ** numero2
    print(f"El resultado es {resultado}")
    
