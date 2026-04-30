# lista = [10, 20, 30, 40]
# lista.clear()
# print(lista)
# lista = [10, 20, 30, 40]
# del lista[-1]
# print(lista)
# lista.insert(2, "Rafael")
# print(lista)

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b

# lista_a.extend(lista_b)
# print(lista_a)

lista_a = ['Rafael', 'Coelho']
lista_b = lista_a.copy()

lista_a[0] = 'Nada'
print(lista_a)
print(lista_b)