###comparacion de edades

# Si el usuario es menor de 18 años, le saldrá, debajo de su nombre completo 
# y año de nacimiento, el mensaje:
# “Eres menor de edad, no podemos darte de alta hasta el año XXXX” 
# (XXXX será el año en que tendrá 18 años y que debermos calcular previamente)
# Si es mayor de 18 años y menor de 25, le saldrá el mensaje: 
# “Tienes un 10% de descuento”
# Si es mayor de 25 años, le saldrá el mensaje:
# “Lo sentimos, pero no tienes descuento”
# Si tiene justo 18 o 25 años, le saldrá el mensaje:
# “Premio, tienes un descuento especial del 20%”


nombre_usuario = input("Ingresa el nombre del usuario: ")
edad_usuario = int(input("Ingresa tu edad: "))


añoNacimiento = 2023-edad_usuario

print(f"Hola {nombre_usuario}  tu año de nacimiento es {añoNacimiento} ")


if(edad_usuario < 18):
    añosRestantes = 18 - edad_usuario;
    añoDescuento = 2023 + añosRestantes
    
    print(f"Eres menor de edad, no podemos darte de alta hasta el año {añoDescuento}")
    
if (edad_usuario > 18 and  edad_usuario  < 25):
    
    print("Tienes un descuento de 25 %")
    

if (edad_usuario > 25):
    print("No tienes descuento")

if (edad_usuario == 18 or edad_usuario == 25  ):
    print('premio !! tienes un descuento especial del 20%')