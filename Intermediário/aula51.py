def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


variavel_123 = 1, 2, 3
print(variavel_123)

soma_variavel = soma(*variavel_123)
print(soma_variavel)

#print(sum((1, 2, 3)))