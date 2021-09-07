lista = []
prints = []
entrada = [1, 2]
while entrada[0] != "X":
    entrada = []
    entrada = input().split()
    if entrada[0] == "I":
        lista.insert(0, entrada[1])
    if entrada[0] == "F":
        lista.append(entrada[1])
    if entrada[0] == "P":
        prints.append(lista[-1])
        lista.pop()
    if entrada[0] == "D":
        prints.append(lista[0])
        del(lista[0])

for i in prints:
    print(i)

for i in lista:
    print(i)
