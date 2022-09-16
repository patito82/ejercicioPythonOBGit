from functools import reduce

lista = [23, 4643, 678, 234, 786, 1434, 2, 3]


def sacareleimpar(x):
    if x % 2 == 1:
        return True
    else:
        return False


def sumar(a, b):
    return a + b


filtrado = filter(sacareleimpar, lista)
a = []
for j in filtrado:
    print(j)
    a.append(j)

print('El resultado de sumar todos es', reduce(sumar, a))
