import sys
sys.set_int_max_str_digits(10000)
# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.html

def recursiva(inicio=0, fim=10):
    print(inicio, fim)

    if inicio >= fim:
        return fim
    
    inicio += 1

    return recursiva(inicio)

recursiva()
    