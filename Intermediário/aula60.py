def executa(funcao, *args):
    return funcao(*args)


def multiplicador(m):
    def multiplicar(n):
        return m * n
    return multiplicar

#duplica = multiplicador(2)
duplica = executa(
    lambda m: lambda n: m*n,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y,
        1, 2
    )
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5
    )
)