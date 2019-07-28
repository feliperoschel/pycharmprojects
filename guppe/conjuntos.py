"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à teoria dos conjuntos (matemática);
- Em python, os conjuntos são chamados de SETS:
- Aceita todos os tipos de dados, assim como listas;
- Sets são, da mesma forma que em matemática:
    - não possuem valor duplicados;
    - não possuem valores ordenados;
    - elementos não são acessados via índice, ou seja, não são indexados;

São interessantes para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordençação deles. Quando não precisamos se
preocupar com chaves, valores e itens duplicados;

- São referenciados em python com chaves {}

Diferenças entre conjuntes (set) e Mapas (dicionários) em python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;


"""

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Não considera as repetições
print(s)
print(type(s))

# Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3} # Não considera as repetições
print(s)
print(type(s))

# converter uma string para um set (conjunto)
s = set('felipe roschel')
print(s)

# Verificar se determinado elemento está contido no conjunto
s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}

n = 13

if n in s:
    print(f'tem o {n}')
else:
    print(f'não tem o {n}')


print('88888888888')

# Não temos valores duplicados e nem ordem

lista = [99, 2, 2, 34, 34, 23, 12, 1, 44, 5]
print(f'Lista: {lista} com {len(lista)} elementos') # Aceitam valores duplicados

tupla = 99, 2, 2, 34, 34, 23, 12, 1, 44, 5
print(f'Tupla: {tupla} com {len(tupla)} elementos') # Aceitam valores duplicados

dicionario = {}.fromkeys([99, 2, 2, 34, 34, 23, 12, 1, 44, 5], 'dict') # NÃO Aceitam valores duplicados
print(f'dicionario: {dicionario} com {len(dicionario)} elementos')

conjunto = {99, 2, 2, 34, 34, 23, 12, 1, 44, 5}
print(f'conjunto: {conjunto} com {len(conjunto)} elementos') # NÃO Aceitam valores duplicados, e NÃO segue uma ordenação como os anteriores


# Iterar em u Set

for valor in s:
    print(valor)


"""
Usos interessantes com sets

- imagine um formulário de cadastro de visitantes de um museu
- os visitantes informam manualmente a cidade de onde vieram
- Adicionamos cada cidade em uma lista python, já que podemos ter valores repetidos numa lista 
"""

# Quantas cidades visitaram o museu
cidades = ['bh', 'sp', 'sp', 'mt', 'sp', 'ms']
print(cidades)
print(len(cidades))

# Quantas cidades distintas visitaram o museu?
# Utilizando o set
print(len(set(cidades)))


# Adicionando elementos em um conjunto
s = {1, 2, 3}
print(s)
s.add(4)
print(s)


# Remover elementos de um conjunto
# Forma 1
s = {1, 2, 3}
print(s)
s.remove(2) # gera erro caso o valor não exista
print(s)

# Forma 2
s = {1, 2, 3}
print(s)
s.discard(1) # NÃO gera erro caso o valor não seja encontrado
print(s)


# Copiando um conjunto para outro

print('+++++')

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)
print(s)

print('+++++')

# Forma 2 - Shallow Copy
novo = s
novo.add(4)
print(novo)
print(s)

# Remover todos os itens de um conjunto
s.clear()
print(s)


# Métodos matemáticos de Conjuntos
# Imagine que temos dois conjuntos: Um contendo estudantes de java
# e outros do curso de python

estudantes_python = {'felipe', 'joao', 'elen'}
estudantes_java = {'fernando', 'gustavo', 'felipe'} # veja que alguns alunos estudaram em ambos cursos

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - utilizando Union - RECOMENDADA
print('88888')
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - utilizando o caractere | (pipe)
print('7777')
unicos1 = estudantes_python | estudantes_java
print(unicos1)

print('----')

# Gerar um conjunto de estudantes que estão em ambos cursos

# Forma 1 - utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

print('----')

# Forma 2 - utilizando &
ambos1 = estudantes_python & estudantes_java
print(ambos1)

print('----')

# Gerar um conjunto de estudantes que estão em um e não no outro
so_python = estudantes_python.difference(estudantes_java) # remove os estudantes que também estão em java além de python
print(so_python)

so_java = estudantes_java.difference(estudantes_python) # remove os estudantes que também estão em python além de java
print(so_java)


# soma, max, min, tamanho
s = {1, 2, 3, 4}
print(sum(s))
print(min(s))
print(max(s))
print(len(s))