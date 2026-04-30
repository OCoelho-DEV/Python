# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')] 

from itertools import zip_longest

lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_estados = ['BA', 'SP', 'MG', 'RJ']

# def zipper(l1, l2):
#     intervalo_maximo = min(len(l1), len(l2))

#     return [(l1[i], l2[i]) for i in range(intervalo_maximo)]

# print(zipper(lista_cidades, lista_estados))

print(list(zip_longest(lista_cidades, lista_estados, fillvalue='Sem Cidade')))
print(list(zip(lista_cidades, lista_estados)))