pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Coelho',
    'idade': 18,
    'altura cm': 1.66,
    'endereço': [
        {'rua': 'Rodolfo Galvão', 'número': 92},
        {'rua': 'outra rua', 'número': 123}
    ]
}

#print(pessoa['altura cm'])

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')