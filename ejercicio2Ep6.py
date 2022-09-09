
class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def estaaprobado(self):
        if self.nota >= 4:
            print("Estas aprobado", self.nombre)
        else:
            print("Buena suerte la proxima")


alumno = Alumno("jorge", 5)
alumno.estaaprobado()
