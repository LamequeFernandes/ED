class Stack:
   #Criar um construtor
   def __init__(self):
      self.itens = []

   # isEmpty → retorna True ou False caso a pilha esteja vazia ou não
   def isEmpty(self):
      return self.itens == []

   # pop → retorna e remove o elemento que está no topo da pilha
   def pop(self):
      return self.itens.pop()

   # pop → retorna e remove o elemento que está no topo da pilha
   def push(self, item):
      self.itens.append(item)

   # olhar o topo da pilha, sem remover o valor
   def peek(self):
      return self.itens[len(self.itens)-1]
      # ou return self.itens[-1]

   # retorna o tamanho da pilha
   def size(self):
      return len(self.itens)

s = Stack() 
s.push(0)
s.push(2)
s.push(0)
s.push(2)
s.push('D')
s.push('E')
for i in s.itens:
    print(i)