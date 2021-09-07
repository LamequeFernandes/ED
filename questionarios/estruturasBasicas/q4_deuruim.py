t, n = input().split()

i = 0
j = 0
h = 0
lista = []

xi = input().split()
while j < int(t):
    lista.append("[x]")
    j = j+1

if t >= n:

    for u in xi:
        if int(u) < int(t):
            lista[int(u)] = u    

    for g in lista:
        print(h, "-", g)
        h = h+1

else: 
    y = 0
    for u in xi:
        if int(u) < int(t):
            lista[int(u)] = u 
            del(xi[y])
        y += 1
    
    i = 0
    while i < int(t):
        if lista[i] == "[x]":
            lista[i] = xi[0]
            del(xi[0])
        i += 1
    
    n = len(xi) - 1
    for g in lista:
        if xi == []:
            print(h, "-", g)
        else:
            print(h, "-", g, "->" , xi[n])
            xi.pop()
            n -= 1
        h += 1



