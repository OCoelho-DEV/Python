frase = 'Python é muito interessante, ' \
    'Python é multiparadigma.'

#print(frase.count('Python'))

i = 0
qtd_letra_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    qtd_atual = frase.count(letra_atual)
    #print(letra_atual, qtd_letra_apareceu_mais_vezes_atual)

    if qtd_letra_apareceu_mais_vezes < qtd_atual:
        qtd_letra_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'{letra_apareceu_mais_vezes} que apareceu '
    f'{qtd_letra_apareceu_mais_vezes}x'
)