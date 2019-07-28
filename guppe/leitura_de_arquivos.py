"""

Leitura de Arquivos

- Para ler o conteudo de um arquivo em Python, utilizamos uma função integrada
  open();
- A função open() na forma mais simples de utilização, passamos apenas o parâmetro de entrada, que e o nome do arquivo;
- Esta funçao retorna um '_IO.TextWrapper' e é com este objeto que trabalhamos;
- A função possui diversos outros parâmetros pocionais que podem ser verificados na documentação;
- Por padrão a função open() abre-o para leitura, caso não exista retora erro de filenotfound;

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>
code='r' -> modo de leitura;
encoding='utf-8' -> codificação do arquivo;
<class '_io.TextIOWrapper'> -> tipo do objeto no python



# Exemplo

arquivo = open('texto.txt')

# print(arquivo)
# print(type(arquivo))

#Para ler o conteúdo de um arquivo apos sua leitura, devemos utilizar a função read()

print(arquivo.read())

# print(arquivo.read())   # Caso imprima novamente, não será listado nada, pois o python utiliza um
# recurso chamado 'cursor', neste caso, o cursor estará em EOF, logo não tem mais nada para ser
# impresso

"""

arquivo = open('texto.txt')

ret = arquivo.read()

print(type(ret))

print(ret)