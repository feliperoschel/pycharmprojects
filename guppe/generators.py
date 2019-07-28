"""

Generators

Em aulas anteriores estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension, porque elas são chamadas de Generators, o qual veremos agora


# Exemplos

nomes = ['carlos', 'camila', 'vanessa']

# Como List Comprehension
res = [nome[0] == 'c' for nome in nomes]
print(type(res))
print(res)


# Como Generatos
res = (nome[0] == 'c' for nome in nomes)
print(type(res))
print(res)

# Visualmente a diferença é apenas o ( para o generator ao invés de [ para list;
# IMPORTANTE: O generator utiliza menos recurso de memória, portanto, é mais performático que o list comprehension, dictionary
  e demais


# Qual é a utilidade de getsizeof

from sys import getsizeof

# Mostra quantos bytes a string 'felipe' está ocupando em memória
print(getsizeof('felipe'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(99786876876876786))

print(getsizeof(True))



from sys import getsizeof

# List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Dictionary
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Generator
gen = getsizeof(x * 10 for x in range(1000))

print('para fazer a mesma tarefa gastamos em memoria:')
print(f'List: {list_comp} bytes')
print(f'Set: {set_comp} bytes')
print(f'Dic: {dic_comp} bytes')
print(f'Gen: {gen} bytes')


# Iterando sobre um Generator

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

    
"""
