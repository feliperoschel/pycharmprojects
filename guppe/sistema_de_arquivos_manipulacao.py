"""

Sistema de Arquivos - Manipulação


import os

# Descobrindo se um arquivo/diretório ou diretório existe
# Path relativo
print(os.path.exists(('frutas.txt')))  # True or False
print(os.path.exists('geek/universisty'))
print(os.path.exists('outro'))

# Path absoluto
print(os.path.exists('/home/froschel/Imagens'))




# Formas não recomendadas:

open('arquivo_teste.txt', 'w').close()  # Já cria e fecha o arquivo criado

open('arquivo_teste2.txt', 'a').close()  # Já cria e fecha o arquivo criado

with open('arquivo_teste3.txt', 'w') as arquivo:  # Já cria e fecha o arquivo criado
    pass  # comando utilizado para não fazer nada dentro do bloco



# Formas recomendadas

os.mknod('arquivo_teste_novo.txt')

os.mknod('/home/froschel/arquivo_teste_novo5.txt')


os.mkdir('templates')  # Cria o diretorio

os.mkdir('templates/geek')  # Cria o diretorio

os.makedirs('templates/geek/university')  # Cria os diretórios caso alguma das pastas não exista, também será criada

os.makedirs('templates/geek/university', exist_ok=True)  # Cria os diretórios caso alguma das pastas não exista, também será criada

os.rename('templates2', 'templates2')  # Acusa erro caso o diretório não estiver vazio

# ATENÇÃO - Ao deletar um arquivo eles não vão para a lixeira, são apagados completamente.

os.remove('tst.txt')

# ATENÇÃO - Ao deletar um diretório eles não vão para a lixeira, são apagados completamente.

os.rmdir('tst')


# Removendo uma árvore de diretório

for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)


# Removendo uma árvore de diretórios vazia

os.removedirs('geek2/outro/mais')  # Se algum diretório estiver arquivos ou outros diretórios o processo pára.


from send2trash import send2trash

send2trash('tst.txt')  # Utilizando esta biblioteca de terceiros, o arquivo vai para a lixeira




#  Trabalhando com arquivos e diretórios temporários

import os
import tempfile


# Estamos criando um diretório temporário, abrindo-o e criando
# um arquivo para escrevermos um texto, no final utilizamos o
# input() apenas para mantermos os arquivos temporários "vivos"
# dentro dos blocos with

with tempfile.TemporaryDirectory() as tmp:
    print(f'criei o diretorio temporario em {tmp}')
    with open(os.path.join(tmp,'geek university'), 'w') as arquivo:
        arquivo.write('geek university \n')
    input()


import os
import tempfile

# Criando apenas um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'teste felipe \n')  # b serve para escrever em binário
    tmp.seek(0)
    print(tmp.read())


https://docs.python.org/3/library/os.html?highlight=os#module.os

"""






