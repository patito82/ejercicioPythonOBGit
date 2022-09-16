import string

paises = input("Ingrese los paises que desea ordenar separados por comas: ")
abc = string.ascii_lowercase
listapaises = paises.split(",")
serepite = set()
for i in listapaises:
    serepite.add(i)

listapaises = list(serepite)
listapaises.sort()
listapaises = ",".join(listapaises)
listapaises = listapaises.lower()
print(listapaises)
