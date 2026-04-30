# v1 = 'a'
# v2 = 'a'
# print(id(v1))
# print(id(v2))

Condicao = True
passou_no_if = None

if Condicao:
    passou_no_if = True
    print("...")
else:
    print("---")

# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')