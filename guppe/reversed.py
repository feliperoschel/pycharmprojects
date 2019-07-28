"""

Reversed

OBS.: NÃO confunda com a função reverse() que estudamos nas listas. A função reverse funciona apenas com listas
já a função Reversed funciona com qualquer coisa.


A função reversed() retorna um iterável chamado List Reversed Iterator


lista = [1, 2, 3, 4, 5]


res = reversed(lista)

print(res)
print(type(res))


# Podemos converter o elemento retornado para  uma lista, tupla ou conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto (set) Obs: Em conjunstos, não definimos a ordem dos elementos
print(set(reversed(lista)))


# Podemos iterar sobre o reversed

for letra in reversed('felipe roschel'):
    print(letra, end='')


print('\n')


# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('felipe roschel'))))


# Já vimos como fazer isso mais facilmente com o slice strings
print('felipe roschel'[::-1])


# POdemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

"""



