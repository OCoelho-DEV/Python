Condicao = True

while Condicao:
    nome = input('Digite seu nome: ')
    if nome == 'sair':
        break
    else:
        print(f'Seu nome é {nome}')

print('Acabou')