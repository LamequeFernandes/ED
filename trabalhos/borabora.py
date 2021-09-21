# play - começa a tocar as músicas da lista, na ordem da lista, a partir da música atual, caso já não esteja tocando (não tem efeito caso contrário). ---> ESTA NA MAIN

# stop - interrompe a execução da música atual. ---> ESTA NA MAIN

# list mostra os ids das músicas na lista, separados por vírgula, ou a mensagem "[vazia]" caso a lista esteja vazia. ---> ESTA NA MAIN

# add - id acrescenta a música id ao final da lista.

def add_(id, f):
    f.append(id)
    return f

# del - id retira a primeira ocorrência da música id na lista, se houver e desde que não esteja tocando. Não interrompe a execução da música atual.
def del_(id, f):
    f.remove(id)
    return f

# next id - define que a música id, se presente na lista, será a próxima a ser tocada, desde que não seja a que esteja sendo tocada no momento. A ocorrência de id na lista é realocada para tanto.
def next_(id, f, rodando):
    if f[0] != id and id in f and rodando == 3:
        aux = id
        f.remove(id)
        f.insert(0, aux)
        return f

    if f[0] != id and id in f:
        aux = id
        f.remove(id)
        f.insert(1, aux)
        return f

# list - mostra os ids das músicas na lista, separados por vírgula, ou a mensagem "[vazia]" caso a lista esteja vazia.
def list_(f):
    if f != ["stop"] or f != ["play"]:
        for musicas in f:
            print(musicas, end=" ")

# current - mostra o id da música atual (sendo tocada no momento), ou da próxima a ser tocada, caso nenhuma esteja no momento. Se a lista estiver vazia, apresente a mensagem: "Toque! Toque, Dijê!".
def current_(f, rodando, deuPlay):
    if len(f) < 1:
        return "Toque! Toque, Dijê!"
    else:
        if deuPlay == False or rodando == 0:
            return f[0]
        if rodando == 1:
            return f[0]
        else:
            return f[1]

# ended - indicando que a reprodução dela terminou (obviamente, apenas uma música que estava sendo tocada pode terminar). Quando uma música termina, a próxima inicia imediatamente, e não é mais possível desfazer as instruções anteriores. O sistema recomeça a tocar a lista do início caso a última música termine e a batalha não tenha começado. 
def ended_(f, rodando):
    if rodando == 1:
        a = f[0]
        del(f[0])
        f.append(a)
        return f
    

# undo [*] - desfaz os efeitos de uma instrução add, del, next ou play. Isoladamente, desfaz o efeito da última instrução. Havendo o argumento opcional *, desfaz o efeito de todas as instruções dadas até aquele ponto.
# def undo(f) ---> ESTA NA MAINS


entrada = [0]
saida = []
saida_orig = []
prints = []
pilha = []
rodando = 3
nextt = 0
deuPlay = False

while entrada[0] != "fight":
    
    entrada = []
    entrada = input().split()

    if entrada[0] == "play":
        deuPlay = True
 #       pilha.append("play")
        rodando = 1
    if entrada[0] == "stop":
        rodando = 0

    if entrada[0] == "add":
        add_(entrada[1], saida)
        saida_orig = saida[:]
        aux = saida[:]
        pilha.append(aux)

    if entrada[0] == "del":
        del_(entrada[1], saida)
        saida_orig = saida[:]
        aux = saida[:]
        pilha.append(aux)

    if entrada[0] == "next":
        next_(entrada[1], saida, rodando)
        saida_orig = saida[:]
        aux = saida[:]
        pilha.append(aux)
        nextt += 1

    if entrada[0] == "list":
        if saida == []:
            prints.append("[vazia]")
        else:
            copia_saida = saida_orig[:]
            prints.append(copia_saida)

    if entrada[0] == "current":
        prints.append(current_(saida, rodando, deuPlay))
        #prints.append(current_(saida_orig, rodando, deuPlay))

    if entrada[0] == "undo":
        if len(entrada) == 2:
            saida = []
        else:            
            pilha.pop()
            saida = pilha[len(pilha)-1]
            saida_orig = pilha[len(pilha)-1]
    
    if entrada[0] == "ended":
        saida_orig = saida[:]
        ended_(saida, rodando)
        if rodando == 1: 
            pilha = []

for strings in prints:
    if type(strings) == str:
        print(strings)
    else:
        i = 0
        while i < len(strings):
            print(strings[i], end="")
            if i < len(strings)-1:
                print(",", end="")
            i += 1

        #for i in strings:
        #    print(i, end="")

        print()
print("Jedi Wagner, assuma o comando!")


#for i in pilha:
#    print(i)

'''
Staralfur,Untitled#8,OlsenOlsen
Staralfur
Untitled#8
Untitled#8
Staralfur,Untitled#8,OlsenOlsen
Jedi Wagner, assuma o comando!
'''