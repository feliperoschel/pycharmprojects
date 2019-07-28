"""
Tipo Boleano

Algebra Booleana, criado por George Boole

2 Constantes, Verdadeiro ou Falso

Obs: Sempre com inicial maiúscula, é case sensitive!

"""


ativo = True
print(ativo)

logado = False

# Operações básicas:

"""
not - Negação: Fazendo a negação, se o valor booleano for verdadeiro o resultado será 
               falso, se o resultado for falso o resultado será verdadeiro. Ou seja 
               sempre o contrário.
"""
print(not ativo)

"""
or - Ou: É uma operação binária, ou seja, depende de dois valores. Ou um Ou outro deve
         ser verdadeiro.

True or True = True
True or False = True
False or True = True
False or False = False         
"""
print(ativo or logado)


"""
and - E: É uma operação binária, ou seja, depende de dois valores. Ambos devem
         ser verdadeiros.
         
True and True = True
True and False = False
False and True = False
False and False = False         
"""
print(ativo and logado)