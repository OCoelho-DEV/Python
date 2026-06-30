# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
ORIGINAL_FOLDER = os.path.join(DESKTOP, 'Teste')
NEW_FOLDER = os.path.join(DESKTOP, 'nova_pasta')

os.makedirs(NEW_FOLDER, exist_ok=True)

for root, dirs, files in os.walk(ORIGINAL_FOLDER):

    for dir_ in dirs:
        new_path_directory = os.path.join(
            root.replace(ORIGINAL_FOLDER, NEW_FOLDER),
            dir_
        )
        os.makedirs(new_path_directory, exist_ok=True)

    for file in files:
        original_path = os.path.join(root, file)
        new_path = os.path.join(
            root.replace(ORIGINAL_FOLDER, NEW_FOLDER),
            file
        )
        shutil.copy(original_path, new_path)