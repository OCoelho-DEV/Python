pessoa = {}

chave = 'nome'
pessoa[chave] = 'Rafael'
pessoa['sobrenome'] = 'Coelho'

print(pessoa[chave])

pessoa[chave] = 'Adriana'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])