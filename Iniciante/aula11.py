"""
if/elif      /else
se/ se não se/se não
"""

entrada = input("Você quer entrar[E] ou sair[S]? ")

if entrada == "E":
    print("Você escolheu entrar")
elif entrada == "S":
    print("Você escolheu sair")
else:
    print("Não escolheu entrar nem sair!")

print("FORA DOS BLOCOS")