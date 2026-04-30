# nome = 'Rafael'
# print(nome[2])
# print("Rafa" in nome)
# print("Pepe" not in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")




