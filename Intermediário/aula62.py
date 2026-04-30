import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = [
    numero * 2
    for numero in range(10)
]
# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 40, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

lista = [n for n in range(10) if n > 2]
p(novos_produtos)
print(lista)



