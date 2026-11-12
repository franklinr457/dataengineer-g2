"""Definicion de funciones"""
def saludar():
    print("HOLAAAAAAAAAAAAA")

"""Llamada a la funcion"""
saludar()

"""Funcion con paramertros"""
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

"""Llamada a la funcion"""
resultado = sumar(3, 5)
print(resultado)

"""Funcion con parametros y valor de defecto"""
def saludar_persona(nombre="invitado"):
    print(f"Hola, {nombre}")

saludar_persona()

"""Funciones con numero variable de argumentos"""
"""*ARGS"""
def mostrar_numeros(*args):
    for numero in  args:
        #args:(1, 2,  3)
        print(numero)

mostrar_numeros(1, 2,  3)

"""**KWARGS"""
def mostrar_informacion(**kwargs):
    #kwargs:(nombre="Esduardo", edad=30)
    for clave in kwargs:
        print(clave,  kwargs[clave])
mostrar_informacion(nombre="Esduardo", edad=30)