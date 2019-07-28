"""

Reduce

OBS: A partir do Python 3+ a função reduce não é mais uma função integrada (built-in)
então temos que importar esta função do módulo 'functools'

Guido Van Rossum, criado do Python diz: Utilize a função reduce se você realmente precisa delas.
Em todo caso, 99% das vezes um loop for é mais legível.

Para entender o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# E vocÊ tem uma função que recebe dois parâmetros

def funcao(x, y):
    return x * y


Assim como map() e filter() a função reduce() recebe dois parâmetros, a função e o iterável.

reduce(funcao, dados)

A função reduce() funciona da seguinte forma:

    passo 1: res1 = f(a1, a2)  # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    passo 2: res2 = f(res1, a3)  # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda do resultado;
             E isso é repetido até o final


    ou seja, em cada passo ele aplica a função  passando como primeiro argumento o resultado  da aplicação anterior. No final
    reduce() irá retornar o resultado final.


Alternativamenteo, poderíamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ..., an)



# Exemplo:

# Vamos utilizar a função reduce para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)


# Mesma execução porém com loop

res = 1
for n in dados:
    res = res * n

print(res)


"""

