nomes = ['Maria', 'João', 'Rafael']
#[(0, 'Maria'), (1, 'Joao'), (2, 'Rafael')]

# nome_enumerado = list(enumerate(nomes))
# print(nome_enumerado)

# for item in enumerate(nomes):
#     nome, indice = item
#     print(nome, indice)

for indice, nome in enumerate(nomes):
    print(indice, nome,nomes[indice])

# for tupla_enumerada in enumerate(nomes):
#     print('FOR da tupla:')
#     for item in tupla_enumerada:
#         print(f'\t{item}')