import os

lista = []

while True:

    print('Selecione uma opção')
    escolha = input('[i]nserir [a]pagar [l]istar: ').lower()

    if escolha == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif escolha == 'a':
        os.system('cls')

        apagar_indice = input('Digite um índice para apagar: ')

        try:
            int_indice = int(apagar_indice)
            item_removido = lista.pop(int_indice)
            print(f'Item removido: {item_removido}')

        except ValueError:
            print('Digite um ÍNDICE.')

        except IndexError:
            print('Digite um índice válido.')

        except Exception:
            print('Erro desconhecido.')

    elif escolha == 'l':
        os.system('cls')

        if not lista:
            print('Nada para listar.')

        else:
            for indice, valor in enumerate(lista):
                print(indice, valor)

    else:
        print('Por favor digite apenas [i] [a] ou [l].')
    