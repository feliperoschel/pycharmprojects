"""

Seek e Cursors

seek() -> é utilizado para movimentar o cursor dentro do arquivo


# Exemplos

arquivo = open('texto.txt')

print(arquivo.read())


print('---------')

# Movimentando o cursor pelo arquivo com a função seek()

arquivo.seek(0)  # Volta o cursor no início, esta função recebe o parâmetro de onde queremos posicionar o cursor

print(arquivo.read())


print('---------')

arquivo.seek(50)

print(arquivo.read())



arquivo = open('texto.txt')

print(arquivo.readline())   # readline lê o arquivo linha por linha, interessante para arquivos muito grande
print(arquivo.readline())
print(arquivo.readline())

arquivo = open('texto.txt')

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))



linhas = arquivo.readlines()  # lê todas linhas do arquivo

print(len(linhas))  # Conta a quantidade de linhas


# Obs.: Quando abrimos o arquivo com a função open, é criada uma conexão do arquivo com o programa;
# esta conexão é chamada de straming. Ao finalizar os trabalhos com o arquivo, é necessário
# fechar os trabalhos com o arquivo através da função close()
# 1-abre o arquivo;
# 2-trabalha com o arquivo;
# 3-fecha o arquivo;

arquivo = open('texto.txt')

print(arquivo.read())

arquivo.close()




arquivo = open('texto.txt')

print(arquivo.read())

print('---')

print(arquivo.closed)

arquivo.close()

print('---')

print(arquivo.closed)

print(arquivo.read())  # teremos um ValueError caso tentarmos manipular um arquivo já fechado.


arquivo = open('texto.txt')

print(arquivo.read(50))  # Limitando a quantidade de posições que iremos ler

"""




