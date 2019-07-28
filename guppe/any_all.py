"""

Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou se o iterável está vazio

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna false


# Exemplo

# False
print(all([0, 1, 2, 3, 4]))  # Todos os numeros são verdadeiros?

# True
print(all([1, 2, 3, 4]))  # Todos os numeros são verdadeiros?

# True
print(all([]))  # Todos os numeros são verdadeiros?

# True
print(all(('geek')))  # Todos os numeros são verdadeiros?


nomes = ['carlos', 'camila', 'carla', 'cassiana', 'cristina', 'felipe']

print(all(nome[0] == 'c' for nome in nomes))

# OBS: Um iterável vazio convertido em Boolean é FALSO, mas o ALL entende como TRUE
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all(num for num in [4, 2, 10, 6, 8] if num % 2 == 0))

print(any([0, 1, 2, 3, 4]))  # True pois 1 ou mais elementos é verdadeiro

print(any([0, False, {}, [], ()]))  # False pois todos elementos são falsos

nomes = ['carlos', 'camila', 'vanessa']

print(any(nome[0] == 'c' for nome in nomes))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))


"""

