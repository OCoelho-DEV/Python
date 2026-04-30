from itertools import zip_longest

lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_b = [5, 6, 7, 8]

# lista c = [6, 8, 10, 12]

lista_c = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_c) # -> [6, 8, 10, 12]



lista_d = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_d) # -> [6, 8, 10, 12, 5, 6, 7, 8, 9, 10] 