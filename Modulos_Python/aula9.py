# os.listdir para navegar em caminhos
# /Users/CoelhoDEV/Desktop/EXEMPLO
# C:\Users\CoelhoDEV\Desktop\EXEMPLO
# caminho = r'C:\\Users\\CoelhoDEV\\Desktop\\EXEMPLO'
import os

path = os.path.join('/home/usuario', 'Documentos', 'Python')

for folder in os.listdir(path):
    folder_path = os.path.join(path, folder)
    print(folder)

    if not os.path.isdir(folder_path):
        continue

    for file in os.listdir(folder_path):
        print('  ', os.path.join(folder_path, file))