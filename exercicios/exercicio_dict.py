# Sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['1', '2', '3', '4', '5'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 10*10?',
        'Opções': ['10', '100', '1000', '20', '0'],
        'Resposta': '100',
    },
]

def pegar_resposta(opcoes, resposta):
    for i, opcao in enumerate(opcoes):
        if opcao == resposta:
            return i


acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    print('Opções:')

    opcoes = pergunta['Opções']
    resposta_correta = pegar_resposta(
    opcoes,
    pergunta['Resposta']
)

    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
        # if opcao == pergunta['Resposta']:
        #     resposta_correta = i
    #print(resposta_correta)

    try:
        resposta = int(input('Escolha uma opção: '))
        if resposta < 0 or resposta >= len(opcoes):
            print('Opção inválida ❌')
            continue
    except ValueError:
        print('Errou ❌')
        continue
    

    
    if resposta == resposta_correta:
        print('Acertou ✅')
        print()
        acertos += 1
    else:
        print('Errou ❌')
        print()

print(f'Você acertou {acertos}\n\
de {len(perguntas)} perguntas.')

