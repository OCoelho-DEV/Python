# entrada = input('[E] Entrar [S] Sair? ')
# senha = input("Senha: ")

# senha_correta = '123'

# if (entrada == "E" or entrada == 'e') and senha == '123':
#     print('Entrou')
# else:
#     print('Saiu')

# Curto Circuito
senha = input("Senha:") or 'Sem senha'
print(senha)