"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) como em outras linguagens
com a diferença de serem dinamicas, e também podermos colocar qualquer tipo de dado.

- C ou Java por exemplo:
    - Possuem tamanho e tipo pré-definidos, ou seja, você só poderá armazenar aquele
      tipo de dado e com aquela quantidade de valores;

- Python é Dinâmico:
    - Não possui tamanho fixo, podendo ser criada e ir recebendo elementos, até que
      exista memória disponível na máquina;
    - Não possui tipo de dado fixo;

Obs.: As listas em Python são representadas por [];
As listas são mutáveis, podem sofrer alterações normalmente;
"""


# Exemplo 1
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 42, 27]
lista2 = ['G', 'E', 'R', 'Y', 'u', 'l', 'j', 't', 'V', 'B']
lista3 = []
lista4 = list(range(11))
lista5 = list('felipe roschel')


# Podemos facilmente checar se determinado valor está contido na lista
num = 101
if num in lista4:
    print(f'Encontrei o número 8')
else:
    print('Não encontrei o número 8')


# Podemos ordenar também uma lista
lista1.sort()
print(lista1)


# Podemos contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))


"""
#Adicionar elementos em listas
 #- Para adicionar elementos em listas, utilizamos a função append;
 #- Só conseguimos adicionar um elemento por vez;
"""
print(lista1)
lista1.append(152)
print(lista1)

# Para adicionar mais de um elemento por vez, utilizamos uma lista dentro da prórpia lista
# desta maneira é gerada uma lista dentro da lista
print(lista1)
lista1.append([200, 201, 202])
print(lista1)


if [200, 201, 203] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')


# Utilizando a função extend, coloca cada elemento como um novo elemento, e nao uma lista
# dentro da lista ja existente como no append
lista1.extend([123, 44, 67])
print(lista1)

"""
#Podemos inserir um novo elemento na lista informando  uma posição no índice já que
#utilizando append e extend eles sempre adicionam o valor ao final da lista. O valor
#anterior não é substituído, o valor é deslocado.
"""
lista1.insert(2,'novo valor')
print(lista1)

print('espacos')

# Podemos juntar listas
lista6 = lista1 + lista2
print(lista6)

print('espacos')

# Forma 1 - Imprimir a lista na ordenação inversa
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

print('espacos')

# Forma 2 - Imprimir a lista na ordenação inversa
print(lista1[:: -1])
print(lista2[:: -1])
print(lista1)
print(lista2)

print('espacos')

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Verificar o tamnho de uma lista
print(len(lista5))

# Remover o último elemento de uma lista
# o pop também retorna o elemento removido, no caso do console
print(lista5)
lista5.pop()
print(lista5)

print('espacos')

# Também é possível remover o elemento através do índice
# Se não houver elemento no índice informado, teremos erro de index error
print(lista5)
lista5.pop(2)
print(lista5)

# Remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

print('******')

# Repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)



"""
# Converter uma string para uma lista
# Exemplo 1
# OBS.: O split separa os elementos através do espaço entre elas
"""
curso = 'programação em python - essencial'
print(curso)
curso = curso.split()
print(curso)

# É possível também determinar um separador para o split, que por padrão usa o espaço
curso = 'felipe,teste,separador' # separador como ','
print(curso)
curso = curso.split(',')
print(curso)


# Retornando uma lista para ums string
lista7 = ['felipe', 'teste', 'separador']
print(lista7)
curso = ' '.join(lista7) # inserir espaços entre cada elemento da lista 7
print(curso)

curso = '$'.join(lista7) # inserir um simbolo desejado entre cada elemento da lista 7
print(curso)

# Podemos inserir qualquer valor dentro de uma lista, exemplo:
lista8 = [1, 2.66, True, 'teste', 'd', [1, 2, 3], 4545646545645645]
print(lista8)


# Iterando sobre uma lista

# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)


# Exemplo 2 - Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digita 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# Acessar os elementos da lista de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[2])
print(cores[-1]) # imprime na ordem inversa

print('******')

# Exemplo de impressão com for
for cor in cores:
    print(cor)

print('******')

# Exemplo de impressão com while
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

print('******')

# Como gerar indices em um for
for indice, cor in enumerate(cores):
    print(indice, cor)


# Encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 8, 9, 10]
print(numeros.index(10))

print('******')

# Podemos fazer busca dentro de um range, escolhendo onde começar e terminar
# reduzindo assim o intervalo de busca
print(numeros.index(9, 3)) # buscando 9 a partir do indice 3
print(numeros.index(8, 3, 6)) # buscando 8 entre 3 e 6


# Revisão de Slicing
lista = [1, 2, 3, 4]
print(lista[1:]) # iniciando no indice 1 e imprimindo os demais
print(lista[:2]) # iniciando no indice 0 e imprimindo até o 2
print(lista[::]) # imprimindo todos indices
print(lista[1:2]) # imprimindo do 1 ate 2
print(lista[1::2]) # imprimindo do 1 ate o final pulando de 2 em 2


print('***********')
# Realizar SOMA, procurar valor Máximo, Mínimo, Tamanho etc
# Obs: para realizar soma os valores devem ser inteiros

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) # soma
print(max(lista)) # máximo
print(min(lista)) # mínimo
print(len(lista)) # tamanho

print('*********')

# Transformar lista em tupla
print(lista)
print(type(lista))

print('     ')

tupla = tuple(lista)
print(tupla)
print(type(tupla))

print('     ')


# Desempacotamento de listas
# Se tivermos mais elementos do que variáveis para receber os valores, teremos erro
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)




# Copiando uma lista para outra
# Shallow copy e Deep copy
# Ao copiar lista, e modificar uma, não modifica a outra (deep copy)

# Deep Copy - as modificações não se refletem para a outra lista
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

nova.append(4)

print(lista)
print(nova)


print('-------')

# Shallow copy - uma modificação reflete na outra
lista = [1, 2, 3]
print(lista)

print('-------')

nova = lista # Copia via atribuição, de uma para a outra
print(nova)

nova.append(4)

print('-------')

print(nova)
print(lista)
