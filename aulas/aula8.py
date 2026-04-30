# IMC = peso / (altura x altura)
nome = "Rafael Coelho"
altura = 1.66
peso = 63
imc = peso / altura ** 2

linha_1 = f"{nome} tem {altura:.1f} de altura"
linha_2 = f"pesa {peso} quilos e seu IMC é:"
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)