# s1 = set()
# s1 = {'Luiz', 1, 2, 3}

# l1 = [1, 1, 1, 3, 2, 3, 2]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# s1 = {1, 2, 3}
# print(3 not in s1)

# Métodos

s1 = set()
s1.add('Rafael')
s1.add(1)
s1.update(('Luiz', 1, 2, 3, 4))
# s1.clear()
# print(s1)
s1.discard('Luiz')
# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # Mostra a união dos conjuntos
s3 = s1 & s2 # Mostra a interseção dos conjuntos
s3 = s1 - s2 # Mostra os que estão apenas no da esquerda
s3 = s1 ^ s2 # Mostra itens que não estão em ambos os conjuntos
print(s3)