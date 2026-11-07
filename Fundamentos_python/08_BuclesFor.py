lista = ["python", "rust", "Java", "c++", "typescript"]

"""Iterar o recorrer sobre una lista"""
for lenguaje in lista:
    print(lenguaje)

    """Recorrer cadena de texto"""
    texto = "I love python" 
    for letra in texto:
        print(letra)

"""Recorrer una lista con indice"""
for index, lenguaje in enumerate(lista):
    print(index, lenguaje)  