"""

Entendendo o *args

- É um parametro como outro qualquer, podendo receber qualquer nome, desde que inciado com *, exemplo:

por convenção a adoção da nomenclatura é a segunte:
*args, poderia ser *xis por exemplo ou qualquer outo nome.

O parametro *args utilizado em uma função, coloca os valores  informados como entrada em uma tupla,
então desde já lembre-se que tuplas são imutáveis.



# Exemplo


# Neste formado, para adicionar qualquer parametro, teriamos de acrescena-los na função
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))



# Utilizando  o *args, no formato abaixo, nao existe limitação de parametros, a função irá somar todos os valores passados na função
# é possível tambem passar parametros específicos como em qualquer função e incrementa-los com args
# sabendo que o args é um tupla, todas as caracteristicas de tuplas sao também aplicadas a ele

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

"""


def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6]

# print(soma_todos_numeros(numeros))  # neste formato é gerado erro pois a variavel numero é uma lista e não consegue converter para uma tupla para a operaçao, portanto, é preciso desempacotar estes dados antes.
print(soma_todos_numeros(*numeros))  # passando com o asterisco * o python entende que precisa antes desempacotar esta lista antes da operação, então não irá gerar erro neste formato, utilizando o *

