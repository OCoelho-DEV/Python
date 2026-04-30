import random

def multiplicador(n):
    def multiplicar(x):
        return n * x
    return multiplicar


dobro = multiplicador(2)
triplo = multiplicador(3)

numeros = []
for _ in range(10):
    novo_numero = random.randint(0, 9)
    numeros.append(novo_numero)

for numero in numeros:
    print(numero)
    print(dobro(numero))
    print(triplo(numero))
    print('----------')
