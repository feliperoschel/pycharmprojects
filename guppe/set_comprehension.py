"""
Set Comprehension (Conjuntos)

Mesmo princípio dos demais *Comprehension

lista = [1, 2, 3, 4]

tupla = (1, 2, 3, 4) ou 1, 2, 3, 4

conjunto = {1, 2, 3, 4} (set)

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4} # Chave e Valor



# Exemplos

# 1
numeros = {num for num in range(1, 7)}
print(numeros)


# 2
numeros = {x ** 2 for x in range(10)}
print(numeros)

# 3 Alterando a estrutura anterior para gerar um dicionário ao invés de SET
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# 4
letras = {letra for letra in 'felipe roschel'}
print(letras


"""
