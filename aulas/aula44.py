"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda'],  # 2
]

# print(salas[0][1])
# print(salas[2][0])
# print(salas[2][3][2])

for num_sala, sala in enumerate(salas):
    print(f'A sala {num_sala} tem os alunos:')
    for num_aluno, aluno in enumerate(sala):
        print(num_aluno, aluno)