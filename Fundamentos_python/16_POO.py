
""" Las clases nos permiten implementar el paradigma de Programación
Orientada a Objetos (POO). Nos permite crear tipos de datos, encapsular
atributos y comportamientos, y organizar código de forma modular y reutilizable. """

# class Persona:
#     pass


# class vehiculo:
#     marca = "Audi"
#     color = "Rojo"
#     modelo = "A4"
    
# camioneta = vehiculo()
# print(camioneta.color)

# minibus = vehiculo()
# print(minibus.color)
class Persona:
    pass

class vehiculo:
    def __init__(self, marca, color, modelo):
        self.marca = "A4"
        self.color = "Rojo"
        self.modelo = "A4"
        
camioneta = vehiculo("toyota", "blanco", "hilux")
print(camioneta.color)

coche = vehiculo("VW", "negro", "golf")
print(coche.color)

#camioneta
#auto
#minibus

#VW
#Mitsubichi
#Toyota
