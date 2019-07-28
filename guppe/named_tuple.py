"""
Módulo Collections - Named Tuple

- São tuplas diferenciadas onde, especificamos um nome para a mesma
e também parâmetros

"""

# Revisando tupla
tupla = (1, 2, 3)
print(tupla[1]) # Impressão através do índice


# Fazendo o import
from collections import namedtuple

# Forma 1 - Declaração da Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome') # Nome da tupple e três valores separados por espaços


# Forma 2 - Declaração da Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome') # Nome da tupple e três valores separados por vírgula - RECOMENDADO


# Forma 3 - Declaração da Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome']) # Nome da tupple e três valores

# Usando a named tuple

ray = cachorro(idade=2, raca='chow-chow', nome='ray')
print(ray)

# Acessando os dados da Tuple

# Forma 1 - Através de índices
print(ray[0])
print(ray[1])
print(ray[2])

print('----')

# Forma 2 - Recomendada
print(ray.idade)
print(ray.raca)
print(ray.nome)


# Forma 3
print(ray.index('chow-chow'))
