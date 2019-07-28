"""
Módulo Collection - Ordered Dict

"""

# Dicionário NÃO garante a ordenação
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for chave, valor in (dicionario.items()):
    print(f'chave={chave}:valor={valor}')


# Fazendo import
from collections import  OrderedDict

# Ordered dict é exatamente como o Dicionário porém GARANTE a ordenação
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
for chave, valor in (dicionario.items()):
    print(f'chave={chave}:valor={valor}')


# Entendendo a diferença entre dict e ordereddict

# Dicionário COMUM
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2) # Testa se dict1 é igual dict2 retornando True/False


# Dicionário OrderedDict
dict1 = OrderedDict({'a': 1, 'b': 2})
dict2 = OrderedDict({'b': 2, 'a': 1})

print(dict1 == dict2) # Testa se dict1 é igual dict2 retornando True/False

# **** No dicionário comum, como não considera ordem, o retorno é TRUE, já no OrderecDict, o retorno é FALSO, pois não obedecem a mesma ordem, portanto não são iguais, já que o ordereddict considera a ordem;
