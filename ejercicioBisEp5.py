

def esbisiesto(year):
    year = int(year)
    if year % 4 == 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")


year = input("Ingrese el year: ")
esbisiesto(year)
