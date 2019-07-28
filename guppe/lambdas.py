"""

Utilizando Lambdas


- Lambdas são funções sem nome, ou seja, funções anônimas.


# Função normal em Python Exemplo

def funcao(x):
    return 3 * x + 1

print(funcao(4))


# Exemplos


# Podemos ter expressões lambdas com múltiplas entradas ou nenhuma entrada.

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('felipe', 'roschel'))

amar = lambda: 'como não amar python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))


# Exemplo de ordenação através do sobrenome dentro de uma lista, utilizando lambda:

autores = ['isaac', 'ray bradbury', 'robert hailen', 'arthur c. clark', 'frank robert', 'douglas adams', 'h. g. wells', 'overson scot card']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())  # utiliza a lista como sort e lambda com funções de ordenação baseado no ultimo elemento da lista, no caso, sobrenome

print(autores)


# Função quadrática
#f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c


print(geradora_funcao_quadratica(3, 0, 1)(2))  #  Os três proimeiros são os parÂmetros da função a, b e c, o último é o parâetro da lambda x


"""




