import pickle


class Vehiculo:
    name = None
    year = None

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def getname(self):
        print(self.name)


ficheroobjeto = open('paraEjercicio2.bin', 'rb')
bajadaarchivo = pickle.load(ficheroobjeto)
ficheroobjeto.close()
bajadaarchivo.getname()
