"""
Tuplas (tuple)

- São semelhantes às listas;
- Diferenças básicas: Tuplas são representadas por parênteses () listas por colchetes [];
- Tuplas são imutáveis, toda operação em uma tupla, gera nova tupla;
- Tuplas são definidas por vírgula, pois os parênteses não são necessariamente essências;

# Por que utilizar tuplas?
- São mais rápidas que listas
- Deixam o código mais seguro - imutabilidade
"""

print(type(()))

# CUIDADO: Tuplas podem ser criadas com ou sem parênteses, exemplo, porém sem deixar
# de ser tupla, pois ao executar continuam representadas por ()

tupla1 = (1, 2, 3, 4)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4
print(tupla2)
print(type(tupla2))

# CUIDADO: Tuplas com apenas 1 elemento, não são tuplas. Exemplo:
tupla3 = (1) # não é uma tupla, é INT
print(tupla3)
print(type(tupla3))

tupla4 = (1, ) # é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 1, # é uma tupla
print(tupla5)
print(type(tupla5))


# Gerar tupla com range
tupla = tuple(range(11))
print(tupla)


# Desempacotamento de tupla
tupla = ('felipe roschel', 'curso codeacademy')
aluno, curso = tupla
print(tupla)
print(aluno)
print(curso)


# Métodos para adição e remoção de elementos nas tuplas não existem, pois elas são imutáveis
# Soma, Max, Min, Tamanho etc são iguais ao funcionamento nas listas;
tupla = (1, 2, 3, 10)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


# Concatenação de tuplas
tupla1 = 1, 2, 3
print(tupla1)
tupla2 = 4, 5, 6
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # Não é alterável porém podemos sobrepor seus valores;
print(tupla1)


# Verificar se determinado elemento está contido na tupla
tupla1 = 1, 2, 3
print(33 in tupla1) # Retornando False/True


# Iterando sobre uma tupla
tupla1 = 1, 2, 3
for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla = 'a', 'a', 'c', 'b', 'b', 'f', 'g'
print(tupla.count('c'))


aluno = tuple('felipe roschel')
print(aluno)


# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que NÃO precisamos modificar os dados contidos na coleção

# Exemplo 1 - Meses serão sempre os mesmos, não havendo necessidade de modificação por exemplo
meses = ('jan', 'fev', 'mar', 'abril', 'maio', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
print(meses)

# Acesso de elementos através de índices
print(meses[5])


# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1


# Verificar em qual índice um elemento está na tupla
print(meses.index('jul'))

print(meses[5:9])


# Copiando um tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla

print(tupla)
print(nova)

outra = (10, 11, 12)

nova = nova + outra
print(nova)
print(tupla)
