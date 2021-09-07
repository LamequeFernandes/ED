i = 0
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
    if entrada[0] == "E":
        prints.append(lista[int(entrada[1])-1])
        del(lista[int(entrada[1])-1])
    if entrada[0] == "T":
        while True:
            if lista[i] == entrada[1]:
                lista[i] = entrada[2]
                break
            i += 1

for i in prints:
    print(i)

print()

for i in lista:
    print(i)
