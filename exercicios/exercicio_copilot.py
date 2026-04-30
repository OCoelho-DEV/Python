def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


# numeros = [10, 15, 20, 25, 30, 35]

# # TODO: Use filter para pegar apenas os números pares

# filtro = filter(
#     lambda x: x if x % 2 == 0 else None,
#     numeros
# )

# print_iter(filtro)
# ---------------------------------------
# from functools import reduce

# numeros = [1, 2, 3, 4, 5]

# # TODO: Use reduce para calcular o produto de todos os números

# total = reduce(
#     lambda ac, x: ac + x,
#     numeros,
#     0
# )
# print(total)
# ----------------------------------------



# TODO: Crie uma função recursiva que calcule o fatorial de um número

def fatorial(n=5):

    if n <= 1:
        return 1
    
    return n * fatorial(n-1)

print(fatorial())