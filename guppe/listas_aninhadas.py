"""
Listas Aninhadas


- Algumas linguagens de programação possuem uma estrutura de dados chamadas arrays:
  - Unidimensionais (Arrays/Vetores);
  - Multimensionais (Matrizes);
  - Geralmente possuem um tamanho pré-definido;
  - Geralmente é preciso declarar o tipo de campo, não sendo possível utilizar outro tipo diferente do declarado;


- Já em Python, temos as Listas
  - numeros = [1, 2, 3, 4, 5];
  - Não possui limitação e nem tipo de campo específico, aceita qualquer tipo;


# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)
print(type(listas))


#  Como fazemos para acessar os dados?
print(listas[0][1])  # Imprime a linha 0 e a coluna 1 da lista
print(listas[2][-2])  # Imprime a linha 2 e a coluna -2 (do fim para o início)



# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)


# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3


# Gerando um tabuleiro/matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1,4)]
print(tabuleiro)



# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 ==0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)


# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])

"""

