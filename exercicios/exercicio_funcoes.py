# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

conta_1 = multiplica(1, 2, 3, 4, 5)
print(conta_1)


# Crie uma função que fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar

def par_ou_impar(num):
    par = num % 2 == 0

    if par:
        return f'{num} é par'
    return f'{num} é ímpar'
    
print(par_ou_impar(24))