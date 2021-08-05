def maior_norma(lista1, lista2):
   maior1 = 0
   maior2 = 0   
   i = 0
   j = 0
   while i < 3:
      if abs(lista1[i]) >= maior1:
         maior1 = abs(lista1[i])
      i += 1
   while j < 3:
      if abs(lista2[j]) >= maior2:
         maior2 = abs(lista2[j])
      j += 1
   
   if maior1 > maior2:
      return print("PRIMEIRO")
   else:
      return print("SEGUNDO")

maior_norma([1, 2, -2], [3, -1, 2])
maior_norma([10, 10, 10], [5, -15, 10])
maior_norma([3, 14003, 0], [10, 909, -1])
maior_norma([0, 0, 0], [0, 0, 1])
maior_norma([1, 2, 3], [1, 2, 4])
maior_norma([3, 3, 3], [2, 4, 5])
maior_norma([1, 2, 3], [3, 2, 10])