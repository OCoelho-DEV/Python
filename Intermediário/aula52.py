def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia', 'Rafael')
)

print(
    executa(saudacao, 'Boa noite', 'Giovana')
)

def dobrar(num):
    return num * 2

def metade(num):
    return num / 2

print(
    executa(dobrar, 2)
)
print(
    executa(metade, 10)
)