"""Son colecciones ordenadas y mutables de elementos que permiten 
 almacenar múltiples valores en una sola variable.""" 

lista1 =  [ 1, 2, 3, 4, 5]
lista2 =  ["python", "rust", "typescript"]
lista3 = [1, 2, 3.14, True, "Hola"]

"""Acceder a los elementos de una lista"""

print(lista2[1]) 
#Output: rust
print(lista3[-1]) 
#Output: ultimo de la lista

"""Slicing (rebanado) de listas"""
print(lista1[1:4])
#Output: [2, 3, 4]

print(lista1[:3])
#Output: [1, 2]

print(lista1[3:])
#Output: [4, 5]

print(lista1[::2]) #(paso2)
#output: [1, 3, 5]

"""Modificar elementos de una lista"""
lista1[4] = 10
print(lista1)

"""Agregar elementos a una lista"""
lista1 = lista1 + [6, 7]
print(lista1)
#output: [1, 2, 3, 4, 10, 6, 7]

"""Obtener la longitud de una lista"""
print(len(lista1))
#Output: 7

"""Metodos de listas"""
lista = ["python"]

lista.append("Go")
print(lista)
#output: ['python', 'Go']

lista.insert(0, "C++")
print(lista)
#output: ['C++', 'python', 'Go']

lista.remove("Go")
print(lista)
#output: ['C++', 'python']

lista.pop(0) #por defecto elimina al ultimo elemento
print(lista)
#output: ['python']

print(lista.index("python"))
#output: 0

print(lista.count("python"))
#output: 1

lista2 = [5, 10, 2]
lista2.sort() #ordena la lista
print(lista2)

lista2.reverse() #invierte la lista
print(lista2)

lista2.clear() #elimina todos los elementos de la lista
print(lista2)
#output: []