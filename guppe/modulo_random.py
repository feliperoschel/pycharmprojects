"""

Módulo Random

- Em python, módulo são nada mais do que os outros arquivos Python;
- Serve para reaproveitarmos trechos de código;
- Pode ser importando módulos da comunidade python, git etc;


Random (integrado): Possui várias funções para geração de números pseudo-aleatórios;


# Obs: Existem duas formas de se utilizar o módulo ou uma função dele apenas


# Forma 1 - Importando todo o módulo
# Obs: O módulo integral fica disponível para utilização, ficando alocado em memória,
# portanto, não recomendado

import random

print(random.random())  # Nome do <módulo>.<função()>  esta função gera um número entre 0 e 1


# Forma 2 - Importando apenas a função desejada (Recomendado)

from random import random  # importando apenas a função desejada

for i in range(10):
    print(random())


from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 Não é incluído. Gera um número pseudo randomico reais dentro do range estabelecido


from random import randint  # gera numeros inteiros dentro do range

for i in range(6):
    print(randint(1, 61), end=', ')


from random import choice  # mostra um valor aleatório entre um iterável

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))


from random import shuffle  # tem a função de embaralhar dados

cartas = ['k', 'q', 'j', 'a', '2', '3', '4']
shuffle(cartas)
print(cartas)

"""



