# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil
from time import sleep

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
ORIGINAL_FOLDER = os.path.join(DESKTOP, 'Teste')
NEW_FOLDER = os.path.join(DESKTOP, 'nova_pasta')

shutil.rmtree(NEW_FOLDER, ignore_errors=True)
sleep(5)
shutil.copytree(ORIGINAL_FOLDER, NEW_FOLDER)