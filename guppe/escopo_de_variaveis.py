"""
Escopo de Variáveis

-> Limitação de algo:
 Ini-------Fim -> Entende-se por escopo de variáveis o espaço entre Ini e Fim;

 1 - Variáveis globais:
     São reconhecidas, ou seja, seu escopo compreende todo o programa;

 2 - Variáveis locais:
     São reconhecidas apenas no bloco onde foram declaradas, ou seja seu escopo está limitado
     ao bloco onde foi declarada;


OBS.: Python é uma linguagem de tipagem dinâmina, isso significa que não definimos
um tipo à ela, o seu tipo é inferido ao valor que atribuímos à ela;

"""

# Exemplo de variável global
numero = 42
print(numero)
print(type(numero))

# Exemplo de reatribuição, onde inserimos uma string numa variável
# anteriormente usada como int
numero = 'felipe'
print(numero)
print(type(numero))

numero = 2

"""
A variável 'novo' está declarada dentro do bloco do if, portanto é uma variável local, 
caso não entre no bloco do if, não será possível a utilização dela no restante do 
código, pois ela não terá sido criada
"""

if numero > 10:
    novo = numero + 10
    print(novo)
