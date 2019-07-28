"""
Funções com Retorno

-> return é a palavra reservada Python para retornar valores em funções
    - Ela finaliza a função, ou seja, sai da execução da função;
    - Podemos ter em uma função, diferentes returns;
    - Podemos retornar qualquer tipo de dado e até mesmo múltiplos valores;

"""

# Exemplos:

numeros = [1, 2, 3]
ret_pop = numeros.pop() # Com retorno
print(f'retorno de pop: {ret_pop}')
ret_pr = print(numeros)
print(f'retorno de print: {ret_pr}') # Sem retorno

# Exemplo 1 - Sem retorno

def quadrado_de_7():
    print(7 * 7) # função sem retorno, print apenas imprime


# Exemplo 2 - Com retorno

def quadrado_de_7():
    return 7 * 7 # Palavra reservada para retorno de funções


ret = quadrado_de_7()
print(f'retorno {ret}')

# ou
print(f'retorno {quadrado_de_7()}')


# Exemplo de 'Return' finalizando a execução da função
def diz_oi():
    return('oi! ')
    print('estou sendo executado após o retorno...') # Desta forma, este valor NUNCA será retornado, pois o return é o fim da função

print(diz_oi())


# Exemplo 2 - Funções com diferentes retornos
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3 - Funções com diferentes tipos de dados no retorno
def outra_funcao():
    return 2, 3, 4, 5

print(outra_funcao())
print(type(outra_funcao()))


print('-----')

# Exemplo 4 - Funções cara/coroa (jogar moeda)
from random import random

def joga_moeda():
    # Gera um número pseudo-rândomico entre 0 e 1
    if random() > 0.5: # utilizando 0.5 como margem, porém a função retorna valores entre 0 e 1 ex: 0.024546544, 0.779989898 etc...
        return 'Cara'
    return 'Coroa'


print(joga_moeda())


# Erros/codificação desnecessárias comuns na utilizaçao do 'return'
# Exemplo
def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    #else: # Este else é desnecessário, pois o contrário já será o outro return
        #return False
    return False

print(eh_impar())


