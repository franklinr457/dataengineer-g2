users = [
    ["Juan", 25, "m", "juan@example.com"],
    ["maria", 45, "f", "maria@example.com"],
    ["yoni", 28, "m", "yoni@example.com"],
    ["Aana", 19, "f", "aana@example.com"]
]

user_format = {
    "id": 1,
    "name": "Juan",
    "age": 25,
    "gender": "m",
    "email": "juan@example.com"
}

new_users = []
i = 1
for user in users:
    user_dict = {
        "id": i,
        "name": user[0],
        "age": user[1],
        "gender": user[2],
        "email": user[3]    
    }
    i += 1
    new_users.append(user_dict)

#print (new_users)

vehiculo = {
    "marca": "Toyota", 
    "modelo": "Corolla",
    "año": 2020  
}

"""Modificar un valor en un diccionario"""
vehiculo["modelo"] = "HONDA"
vehiculo["color"] = "rojo"
print(vehiculo)

"""Eliminar un valor en un diccionario"""
del vehiculo["color"]
vehiculo.pop("año")
print(vehiculo)

"""metodos utiles de diccionarios"""
print(vehiculo.keys())#devuelve las claves del diccionario
print(vehiculo.values())#devuelve los valores del diccionario
print(vehiculo.items())#devuelve una lista de tuplas con las claves y valores del diccionario

"""Iterar sobre un diccionario"""
for clave, valor in vehiculo.items():
    print(clave, valor)

for clave in vehiculo:
    print(clave, vehiculo[clave])