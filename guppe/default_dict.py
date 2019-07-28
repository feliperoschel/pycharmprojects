"""
Módulo Collections - Default Dict

- Diferenças para Dicinário:
    - Dicionário: Caso não hava um valor da chave buscada, é retornado erro;
    - Default Dict: É possível atribuir um valor default e a chave é criada, não gerando erro;
"""

#dicionario = {'curso': 'python'}
#print(dicionario)
#print(dicionario(['outro'])) # Retorna erro caso não exista

# Fazendo o import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'felipe roschel'
print(dicionario)

print(dicionario['outro']) # imprime o valor '0' que foia atribuido à função lambda caso a chave passada não exista. Adiciona a chave e o valor '0' definido

print(dicionario)




