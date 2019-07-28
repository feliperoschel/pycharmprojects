"""
Funções com parâmetros de Entrada, ou seja, funções que recebem parâmetros para serem utilizados dentro da mesma.

Funções:
- Não necessarimanete possuem entrada / retorno;
- Podem ter N parâmetros, de acordo com a necessidade, sendo separados por vírgula;




def quadrado_de_7(numero): # função exige parâmetro
    return numero * numero

print(quadrado_de_7(7)) # passagem do parâmetro para a função.

print(quadrado_de_7(2))

print(quadrado_de_7(5))




def cantar_parabens(aniversariante):
    print('parabens pra vc')
    print('parabens pra vc')
    print('parabens pra vc')
    print(f'viva o/a {aniversariante}!')


cantar_parabens('Marcos') # chamada da função com parâmetro




def soma(a, b):  # em funções, se informarmos uma qtde inválida de argumentos, seja ela maior ou menor,  é gerado erro.
    return a + b


def multiplica(a, b):
    return a * b

def outra(a, b, msg):
    return (a + b) * msg


print(soma(1, 5))
print(multiplica(4, 5))
print(outra(5, 6, 'tst'))




def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}.'



nome = 'felipe'
sobrenome = 'roschel'

print((nome_completo(nome, sobrenome)))  # neste formado, a ordem dos argumentos importa


# Caso utilizemos nome dos parâmetros nos argumentos para informa-los, podemos utilizar qualquer ordem, exemplo:
# Argumentos nomeados - Keyword Arguments
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome=sobrenome, nome=nome))


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))


"""


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total
