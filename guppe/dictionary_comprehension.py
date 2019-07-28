"""

Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

tupla = (1, 2, 3, 4) ou 1, 2, 3, 4

conjunto = {1, 2, 3, 4}

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4} # Chave e Valor


# Sintaxe

{chave:valor for valor in iteravel} # Dictionary Comprehension
[valor for valor in iteravel]  # List Comprehension



# Exemplos

# 1

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}  #  Pega o valor do dic e multiplica ao quadrado, por chave.

print(quadrado)


# 2


numeros = [1, 2, 3, 4, 5]  # Pode ser usado tupla, lista, set etc.

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)


# 3

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

"""


# 4 Exemplo com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num:('par' if num % 2 ==0 else 'impar') for num in numeros}

print(res)