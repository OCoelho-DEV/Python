# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

counter = count()
path = os.path.join('/home/usuario', 'Documentos', 'Python')

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, 'Folder:', root)

    for dir_ in dirs:
        print('\t', the_counter, 'Dir:', dir_)

    for file_ in files:
        full_path = os.path.join(root, file_)
        print('\t', the_counter, 'File:', full_path)