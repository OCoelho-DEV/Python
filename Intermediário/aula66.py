string = 'Rafa'
metodo = 'upper'
# print(dir(string))
if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)