"""

Escrvendo em arquivos

Obs.: Quando abrimos um arquivo como leitura, não podemos realizar escrita.
      Da mesma forma que, ao abrirmos um arquivo para escrita, não conseguimos ler;

- Ao abrir o arquivo para escrita, o arquivo é criado no sistema operacional

- Caso o arquivo ja exista, o arquivo será removido e um novo criado, ou seja, o conteudo
  do arquivo existente será perdido, e um novo será criado. Existe uma função específica para
  incrementar o arquivo já existente que iremos ver na próxima aula;


# Exemplo de escrita

with open('novo.txt', 'w') as arquivo:  # Abertura em modo 'w' (write)
    arquivo.write('novos dados  \n')
    arquivo.write('outros dados segunda linha  \n')
    arquivo.write('bal bla bla bla \n')


with open('novo.txt') as arquivo:
    print(arquivo.read())



with open('geek.txt', 'w') as arquivo:
    arquivo.write('geek ' * 1000)


with open('geek.txt') as arquivo:
    print(arquivo.read())




with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + ' \n')
        else:
            break


with open('frutas.txt') as arquivo:
    print(arquivo.read())

"""

