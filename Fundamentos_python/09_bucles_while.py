from time import sleep

lista = ["python", "rust", "Java", "c++", "typescript"]#puede mutar
tupla = ("ruby", "go", "c#", "c++", "javascript")#no puede mutar

contador = 0
while contador < 10:
    contador += 1
    sleep(1)
    print(contador)

"""salir de un bucle while con break"""
while True:
    print(contador)
    contador += 1
    if contador == 15:
        break #rompe el bucle while cuando el contador es 15

"""saltar una iteracion con continue"""
while True:
    contador += 1
    if contador == 5:
        continue #salta la iteracion cuando el contador es 5
    print(contador)

    if contador == 10:
        break #rompe el bucle while cuando el contador es 10