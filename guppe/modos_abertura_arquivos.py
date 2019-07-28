"""

Modos de abertura de arquivos

r -> abre para leitura (default);
w -> abre para escrita - sobrescreve caso o arquivo já exista;
x -> abre para escrita somente se o arquivo não existir, falha caso exista;
a -> abre para escrita, adicionando o conteudo ao final do arquivo;
+ -> abre o arquivo para atualização, leitura e escrita;

https://docs.python.org/3/library/function.html#open


with open('university.txt', 'x') as arquivo:
    arquivo.write('teste. \n')  # Ao exeuctar novamente, gera erro.


Exemplo A


with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('informe uma fruta ou sair')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break


with open('frutas.txt', 'r') as arquivo:
    print(arquivo.read())



# Exemplo 2

with open('outro.txt', 'a') as arquivo:
    arquivo.write('sssssno topo do arquivo! \n')
    arquivo.write('fffffno topo do arquivo 1! \n')
    arquivo.write('ggggno topo do arquivo 2! \n')


with open('outro.txt', 'r') as arquivo:
    print(arquivo.read())


# Utilizando o parametro +

# with open('outro_1.txt', 'a+') as arquivo:
# with open('outro_1.txt', 'w+') as arquivo:
# with open('outro_1.txt', 'r+') as arquivo:
    arquivo.write('linha nova \n')
    arquivo.write('3 nova linha! \n')
    arquivo.write('3 mais uma linha \n')


with open('outro_1.txt', 'r') as arquivo:
    print(arquivo.read())


"""




