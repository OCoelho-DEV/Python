def soma(x, y):
    if x > 10:
        return [10, y]
    return x + y

variavel = soma(1, 2)
variavel2 = soma(3, 4)
print(variavel + variavel2)
print(soma(11, 5))