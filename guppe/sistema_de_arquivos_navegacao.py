"""

Sistema de Arquivos e Navegação

Para fazer o uso de manipulação de arquivos do sistema operacional, precisamos
importar e fazer o uso do módulo OS.

OS -> Operating System - Sistema Operacionals


# Fazer o import

import os

print(os.getcwd())  # Pega o current work directory

os.chdir('..')  # Volta um diretorio

print(os.getcwd())

os.chdir('..')  # Volta um diretorio

print(os.getcwd())

os.chdir('..')  # Volta um diretorio

print(os.getcwd())

os.chdir('..')  # Volta um diretorio

print(os.getcwd())


print(os.path.isabs('/home/froschel/'))  # Checar se um diretório é absoluto ou relativo

print(os.name)  # Identificar o sistema operacional
print(os.uname())  # Identificar o sistema operacional



print('-----')

print(os.getcwd())

res = os.path.join(os.getcwd(), 'geek')  # Acessar um diretório dinamicamente

os.chdir(res)

print(os.getcwd())


print(os.listdir('/home/froschel'))  # listar os diretórios

arquivos = print(os.scandir())  # lista diretório com mais detalhes



scanner = os.scandir()

arquivos = list(scanner)

#print(arquivos)

#print(dir(arquivos[0]))

print(arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].name)
print(arquivos[0].path)
print(arquivos[0].stat())

"""


