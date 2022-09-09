
class Vehiculo:
    color = "Azul"
    ruedas = 4
    puertas = 5


class Coche (Vehiculo):
    velocidadKph = 120
    cilindrada = 4


coche = Coche()
print(coche.color)
print(coche.ruedas)
print(coche.puertas)
print(coche.velocidadKph)
print(coche.cilindrada)
