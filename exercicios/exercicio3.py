primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")


if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}')
elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor=} é maior que {primeiro_valor=}')
else:
    print(f'{primeiro_valor=} é igual a {segundo_valor=}')



# frase = "{} é maior que {}"

# if primeiro_valor > segundo_valor:
#     print(frase.format(primeiro_valor, segundo_valor))
# elif primeiro_valor < segundo_valor:
#     print(frase.format(segundo_valor, primeiro_valor))
# else:
#     print("São iguais")

