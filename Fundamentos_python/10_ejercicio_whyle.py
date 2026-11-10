"""1. validar que una contraseña tenga al menos 8 caracteres """
#INPUT ":12345678"
#OUTPUT : "Introduce minimo 8 caracteres"

#INPUT ":12345678"
#OUTPUT : "Introduce minimoaracteres"-


"""2 Ingresar un numero y crear una tabla de multiplicar hasta el 10"""
#INPUT "1"
#OUTPUT : 1x1 ,2x2, 3x3


#1
while True:
    password = input("Ingrese una contraseña: ")
    if len(password) < 8:
        print("Introduce minimo 8 caracteres")
    else:
        print("Contraseña valida")
        break

"""#2 
while True:
    numero = input("Ingrese un número para crear su tabla de multiplicar: ")

    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {int(numero) * i}")
        i=i+1
    
"""