"""
Estruturas de Repetição

Loop:
For:

Utilizamos loops para iterar sobre sequências ou valores iteráveis. Exemplo:
    - String;
    - Lista;
    - Range;
"""


nome = 'felipe roschel'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)


# Exemplo de for 1 - Iterando sobre string
for letra in nome:
    print(letra)


# Exemplo de for 2 - Iterando sobre uma lista
for numero in lista:
    print(numero)


# Exemplo de for 3 - Iterando sobre um range
# Obs: O valor final não é inclusivo, ou seja, o loop vai do 1 ao 9 no exemplo abaixo
for numero in range(1, 10):
    print(numero)


# Exemplo de for com enumerate baseado em índices
# ((0, 'f'), (1,'e') ...)
for i, v in enumerate(nome):
    print(nome[i])


# ou
for indice, letra in enumerate(nome):
    print(nome[indice])


# ou utilizando o _ descartanto o índice, já que só queremos utilizar a letra, e não precisamos do índice
for _, letra in enumerate(nome):
    print(letra)


# ou retornando o índice e o valor do respectivo
for valor in enumerate(nome):
    print(valor)


qtd = int(input('Quantas vezes o loop deve rodar?'))

for n in range(1, qtd + 1):
    print(f'Imprimindo {n}')


qtd = int(input('Quantas vezes o loop deve rodar?'))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n} / {qtd} valor'))
    soma += num

print(f'A soma é {soma}')


nome = 'felipe roschel'
for letra in nome:
    print(letra, end='')

print('',)


# Imprimir emoji
# Tabela de emoji unicode: https://apps.timwhitlock.info/unicode
# Emoji Unicode: U+1F63B

for num in range(1, 11):
    print('\U0001F63B' * num) # Trocar o + por 3 zeros 0
