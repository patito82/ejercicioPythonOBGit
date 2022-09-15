import time

print(time.strftime('%d/%m/%y'))
print(time.strftime('%H:%M:%S'))
tiempoh = time.strftime('%H:%M:%S')
tiempo = tiempoh.split(":")


def jornadalaboral(tiempo):
    horas = None
    min = None
    seg = None
    horasf = -1
    minf = 0
    segf = 0
    for i in tiempo:
        horas = int(tiempo[0])
        min = int(tiempo[1])
        seg = int(tiempo[2])
    if horas >= 7:
        print("Fuera de jornada laboral")
    else:
        if horas >= 0:
            while horas < 7:
                horas += 1
                horasf += 1
        if min != 0:
            while min < 60:
                min += 1
                minf += 1
        if seg != 0:
            while seg < 60:
                seg += 1
                segf += 1
        faltantrabajar = [str(horasf), str(minf), str(segf)]
        faltantrabajarstr = ":".join(faltantrabajar)
        print("Te quedan trabajar", faltantrabajarstr)


jornadalaboral(tiempo)
