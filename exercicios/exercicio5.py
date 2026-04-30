"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
pedido = input("Digite um número inteiro: ")


if pedido.isdigit():
    numero_digitado = int(pedido)
    par_ou_impar = numero_digitado % 2 == 0
    par_impar_texto = 'ímpar'

    if par_ou_impar:
        par_impar_texto = 'par'
    
    print(f'{numero_digitado} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro!')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Que horas são? (use valores inteiros) ')

try:
    int_hora = int(hora) #Transformar em inteiro para verificar
    dia = int_hora >= 0 and int_hora <= 11
    tarde = int_hora >= 12 and int_hora <= 17
    noite = int_hora >= 18 and int_hora <= 23 

    if dia:
        print('Bom dia!')
    elif tarde:
        print('Boa tarde!')
    elif noite:
        print('Boa noite!')
    else:
        print('Não existe essa hora')
except:
    print('Não digitou hora em número inteiro!')
    


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

tamanho_nome = len(nome)
nome_curto = tamanho_nome <= 4
nome_normal = tamanho_nome >= 5 and tamanho_nome <= 6
#nome_grande = tamanho_nome > 6 -> não necessário

if not nome or nome.isdigit() or tamanho_nome <= 1:
    print('Você não digitou um nome')
else:
    if nome_curto:
        print(f'Seu nome é curto: {tamanho_nome} letras')
    elif nome_normal:
        print(f'Seu nome é normal: {tamanho_nome} letras')
    else:
        print(f'Seu nome é muito grande: {tamanho_nome} letras')

