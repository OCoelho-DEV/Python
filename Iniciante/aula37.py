#         0   1   2   3   4
lista = [10, 20, 30, 40]

print(lista)
# del lista[2]
# print(lista)

lista.append(50)
lista.append('ABC')
print(lista)

removido = lista.pop(3)

print(lista, 'Removido:', removido)