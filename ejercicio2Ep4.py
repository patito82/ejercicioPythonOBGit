inicio = input("Ingrese un numero para iniciar: ")
final = input("Ingrese un numero para finalizar: ")

inicio = int(inicio)
final = int(final)
while inicio < final:
    if inicio % 2 == 1:
        print(inicio)
    inicio = inicio + 1
