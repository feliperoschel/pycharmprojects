"""

Trabalhando com módulos Builtin - Módulos integrados (já instalados no Python)


# Utilizando alias (apelidos) para os módulos/funções

import random as rdm

print(rdm.random())


from random import *

print(random())


from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())


from random import (
    random,
    randint,
    shuffle,
    choice
)

print(randint(5, 89))
print(random())

"""




